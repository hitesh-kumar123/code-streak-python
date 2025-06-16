f = open("file.txt")

print(f.read())

f.close()

# with statement

with open("file.txt") as f:
    print(f.read())

#you dont have to explicity close the file
