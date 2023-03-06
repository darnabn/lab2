commentators = set()
while True:
    line = input()
    if line == "":
        break
    name, comment = line.split(": ")
    commentators.add(name)

print("Количество уникальных комментаторов: ", len(commentators))