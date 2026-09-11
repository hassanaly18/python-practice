"""
Memory leak demo: EventBus with an append-only listeners list,
plus a closure that unintentionally captures a large object.

Requires: pip install objgraph
Optional: graphviz (system package, provides the `dot` binary) if you
want show_backrefs() to render backrefs.png.
"""

import gc


class Request:
    """Simulates a request object carrying a chunk of data."""

    def __init__(self, req_id):
        self.req_id = req_id
        self.payload = "x" * 10_000  # pretend this is meaningful data


class EventBus:
    """The culprit: listeners accumulate and are never removed."""

    def __init__(self):
        self.listeners = []

    def on_request_processed(self, callback):
        self.listeners.append(callback)  # BUG: nothing ever removes these

    def fire(self, request):
        for cb in self.listeners:
            cb(request)


bus = EventBus()


def process_request(req_id):
    """Clean version: log_it doesn't capture `req`, so nothing leaks."""
    req = Request(req_id)

    def log_it(r):
        pass  # doesn't touch `req` at all -> no closure cell created for it

    bus.on_request_processed(log_it)
    bus.fire(req)


def process_request_v2(req_id):
    """Leaky version: log_it closes over `req` instead of using the
    parameter `r` that fire() already passes in. Since bus.listeners
    never shrinks, `req` (and its 10,000-char payload) is kept alive
    forever."""
    req = Request(req_id)

    def log_it(r):
        print(req.req_id)  # BUG: should use `r`, not `req`

    bus.on_request_processed(log_it)
    bus.fire(req)


def process_request_v2_fixed(req_id):
    """Fixed version: use the parameter passed by fire(), so no closure
    over `req` is needed at all."""
    req = Request(req_id)

    def log_it(r):
        print(r.req_id)

    bus.on_request_processed(log_it)
    bus.fire(req)


if __name__ == "__main__":
    import tracemalloc
    import objgraph

    tracemalloc.start()

    # --- Establish a baseline before anything runs -------------------
    gc.collect()
    objgraph.show_growth(limit=1)  # sets the baseline; output not very useful yet

    # --- First batch: trigger the leak --------------------------------
    for i in range(1000):
        process_request_v2(i)

    gc.collect()
    print("\n--- Most common types after first 1000 calls ---")
    objgraph.show_most_common_types(limit=10)

    print("\n--- Growth after first 1000 calls (vs baseline) ---")
    objgraph.show_growth(limit=5)

    # --- Second batch: confirm it keeps growing -----------------------
    snap1 = tracemalloc.take_snapshot()

    for i in range(1000, 2000):
        process_request_v2(i)

    gc.collect()
    snap2 = tracemalloc.take_snapshot()

    print("\n--- Growth after second 1000 calls ---")
    objgraph.show_growth(limit=5)

    print("\n--- tracemalloc: where the extra memory was allocated ---")
    diff = snap2.compare_to(snap1, "lineno")
    for stat in diff[:5]:
        print(stat)

    # --- Find why a leaked Request is still alive ----------------------
    leaked = objgraph.by_type("Request")[0]

    print("\n--- Referrers keeping a leaked Request alive ---")
    referrers = gc.get_referrers(leaked)
    for r in referrers:
        print(type(r), r)

    # Requires graphviz's `dot` binary on PATH; comment out if unavailable
    try:
        objgraph.show_backrefs([leaked], max_depth=5, filename="backrefs.png")
        print("\nWrote backrefs.png")
    except Exception as e:
        print(f"\nCould not render backrefs.png ({e}). "
              f"Install graphviz to enable this.")

    # --- Prove the fix works: run the fixed version and check growth ---
    print("\n--- Verifying process_request_v2_fixed does NOT leak ---")
    bus.listeners.clear()  # reset the bus so the earlier leak doesn't skew this
    gc.collect()
    objgraph.show_growth(limit=1)  # reset baseline

    for i in range(1000):
        process_request_v2_fixed(i)

    gc.collect()
    objgraph.show_growth(limit=5)  # should show little to no Request growth