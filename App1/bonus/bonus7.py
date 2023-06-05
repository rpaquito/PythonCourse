filenames = ["1.aaaaaa", "2.bbbbb", "3.cccccccc"]

filenames = [filename.replace(".", "-") + ".txt" for filename in filenames]

print(filenames)
