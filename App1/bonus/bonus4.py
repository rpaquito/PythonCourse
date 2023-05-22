filenames = ["1.fsdfsadf.txt", "2.dasfsdf.py", "3.dfsfassfd.doc"]

for file in filenames:
    filename = file.replace('.', '-', 1)
    print(filename)
