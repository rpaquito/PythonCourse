member = input("Add new member:")

file = open('../files/exercise4.txt', 'r')
members = file.readlines()
file.close()

members.append(member + "\n")

file = open('../files/exercise4.txt', 'w')
file.writelines(members)
file.close()
