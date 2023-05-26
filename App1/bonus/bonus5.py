wait_list = ["sen", "ben", "john"]
#wait_list.sort()
wait_list.sort(reverse=True)

for index, item in enumerate(wait_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)
