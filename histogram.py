import random, re, time, math, csv
from random import shuffle
from sys import argv



#create function to determine whether letter is before or after in alphabet
#insert item into a binary search tree
#when adding a new item, insert into the tree or find new spot

def histogram():
    histogram = {}
    startTime = time.time()
    txt = open("/Users/ownernopassword/Desktop/Tweet-Generator-Course-Algorithms-Practice-master/harry.txt")

    filteredText = txt.read().replace('\n', '')
    removeCharacters = ['.','!','?','\"', '\"',',','[',']','-',"{", "}", ';', '\t']
    removeCharacters

    for ch in removeCharacters:
        filteredText = filteredText.replace(ch, "")

    words = []
    words = filteredText.split()

    for word in words:
        try:
            count = histogram[word]
            histogram[word] = histogram[word] + 1
        except:
            histogram[word] = 1

    return histogram


def frequency():
    histogram = {}
    startTime = time.time()
    txt = open("/Users/ownernopassword/Desktop/Tweet-Generator-Course-Algorithms-Practice-master/harry.txt")

    filteredText = txt.read().replace('\n', '')
    removeCharacters = ['.','!','?','\"', '\"',',','[',']','-',"{", "}", ';', '\t']
    removeCharacters

    for ch in removeCharacters:
        filteredText = filteredText.replace(ch, "")

    words = []
    words = filteredText.split()

    for word in words:
        try:
            count = histogram[word]
            histogram[word] = histogram[word] + 1
        except:
            histogram[word] = 1

    for i in range (0,100):
        randomIndex = random.randint(0,len(words) - 1)
        randomWord = words[randomIndex]
        probability = float(histogram[randomWord])/float(len(words))
        print randomWord + " " + str(probability)

#save space
    count = 0
    randomIndex = random.randint(0,len(words) - 1)
    randomWord = words[randomIndex]
    for w in words:
        if w == randomWord:
            count = count + 1

    print float(count)/float(len(words)), randomWord




    for i in range (0,100):
        randomIndex = random.randint(0,len(words) - 1)
        randomWord = words[randomIndex]
        probability = float(histogram[randomWord])/float(newTotal)
        print randomWord + " " + str(probability)

    count = 0
    output = []
    for key, value in histogram.iteritems():
        count = count + value - 1
        data = (key, count - 1)
        output.append(data)




# same array and store the number of times that word appears in a variable



frequency()


if __name__ == "__main__":
    app.run()
