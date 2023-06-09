def convert(feet_inches_arg):
    parts = feet_inches_arg.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters


feet_inches = input("Enter feet and inches: ")

result = convert(feet_inches)

if result < 1:
    print("Too small")
else:
    print("Can use")
