password = input("Enter new password:")
result = {}
if len(password) >= 8:
    result["len"] = True
else:
    result["len"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digit"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True

result["upper"] = upper

print(result)

if all(result.values()):
    print("Strong")
else:
    print("Weak")
