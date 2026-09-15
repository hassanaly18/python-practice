# f = open("geek.txt", "r")
# print(f.name)     # 'geek.txt'
# print(f.mode)     # 'r'
# print(f.closed)   # False
# f.close()
# print(f.closed)   # True


#Safer version
file = None
try:
    file = open("geek.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("Error:", e)
finally:
    if file:
        file.close()