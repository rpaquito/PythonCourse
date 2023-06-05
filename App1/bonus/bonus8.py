date = input("Enter date: ")

rate = input("Rate your mood: ")

journal = input("Thoughts: \n")

with open(f"../journal/{date}.txt", "w") as file:
    file.write(rate + 2 * "\n")
    file.write(journal)
