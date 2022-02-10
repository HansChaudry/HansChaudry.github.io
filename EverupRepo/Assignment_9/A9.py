# PART A
myList = ['One', 'Uno', '01101111 01101110 01100101', 'un']
myList2 = []
for x in myList:
    myList2.append(x)

myList2.append('een')
del myList[2]

myList3 = myList2


# PART B
txt = 'hi there how are you'
# counts amount of times the substring appears in the string
print('Part B:')
print(txt.count('h', 0, len(txt)))

# //check if the strings end with the specified suffix
print(txt.endswith('dog', 0, len(txt)))

# Finds the index where the specified substring begins
print(txt.find('how', 0, len(txt)))

words = ('Stop', 'Go', 'Slow')
# Combines a sequence of elements in a container with the given being in the middle of each word
print('+'.join(words))

# Replaces a substring
print(txt.replace("there", "john !"))

# Splits the string whenever the substring appears and stores each piece in a list
print(txt.split(' '))

# Splits the string when newline keyword is found and stores lines in a list
newTxt = 'hi john!\nhow are you?'
print(newTxt.splitlines())

# Checks if string start with the given prefix
print(newTxt.startswith('hi'))

# Removes the  first instance of the substring from the string
print(txt.strip('h'))


# PART C
def isPrime(num):
    if num <= 0:
        return False

    for n in range(2, num):
        if num % n == 0:
            return False

    return True


# PART D
def disStuInfo(schoolID, *firstname, **lastEmail):
    x = 0
    for n in lastEmail:
        print(schoolID)
        if x == (len(firstname)):
            print("'unmatched'")
        else:
            print(firstname[x])
        print(n, '\n' + lastEmail[n] + '\n')
        x += 1
