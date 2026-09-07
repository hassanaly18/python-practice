import csv 

filename = input()

with open(filename, "r") as file:
    words = list(csv.reader(file))[0]

for i, word in enumerate(words):
    count = words.count(word)

    if word not in words[:i]:
        print(word, "-", count)
