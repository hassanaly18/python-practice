class MyContext:

    def __enter__(self):
        return "Hello World"

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Finished")

with MyContext() as value:
    print(value)




# class MyContext:

#     def __enter__(self):
#         print("Entering")

#     def __exit__(self, exc_type, exc_value, exc_tb):
#         print("Exiting")

# with MyContext():
#     print("Hello")