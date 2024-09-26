len("12345")

print(type("123"))
print(type(123))
print(type(3.14159))
print(type(True))

print("Number of letters in your name: " + str(len(input("Enter your name"))))

print(int(123.3)+456) # la parte decimal es ignorada

print(int("123.3")+456) # Genera un error

print(int(float("123.3"))+456) # solucionando el error anterior

