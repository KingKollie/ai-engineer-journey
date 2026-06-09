# write to a file
with open("Goal.tx", "w") as f:
    f.write("Goal 1: Learn Python\n")
    f.write("Goal 2: Build AI app\n")
    f.write("goal 3: Get hired as AI Engineer\n")

# read the file back 
with open("goals.txt", "r") as f:
    content = f.read()
    print(content)     


