# words_file = open('CROSSWD.txt','r')

# print(type(words_file))

# words = []

# for line in words_file:
#     print(line.strip())
#     #words.append(line)

# print(words)

# print([x for x in dir(words_file) if "_" != x[0]])
#print(words_file.readline())

# data = [1, 3, 2, 8, 5, 6, 10]
# print([2*x for x in data if x % 2 == 0])

# print(words_file.readline())
# print(words_file.readline())
# while True:
#     print(words_file.readline())



def more_than_20(file):
    words = []
    data = open(file, 'r')
    for word in data:
        if len(word.strip()) > 20:
            words.append(word.strip())
            print(word)
    # words = [x.strip() for x in data if len(word) > 20]
    return words
print(more_than_20("CROSSWD.txt"))

# word = 'Abracadabra'
# for x in word:
#     print(x)
 
def has_no_e(word):
    if 'e' not in word:
        return True
    
    return False
    # check = True
    # for letter in word:
    #     if 'e' == letter:
    #         check = check and False
    # return check

    # words = 'Abracadabra'
    # for x in words:
    #     if 'e' in words:
    #         return False
    #     else:
    #         return True
    # return words
print(has_no_e("Abracadabra"))

def uses_only(word,letters):
    for x in word:
        if x not in letters:
            return False
    return True
print(uses_only("abracadabra", "abr"))
    # if letters in word:
    #     return True
    # else:
    #     return False

def all_uses_only(file, letters):
    words = []
    data = open(file, 'r')
    for word in data:
        if  True == uses_only(word.strip(), letters):
         words.append(word.strip())
         #words.apend(data)
         #uses_only(word, letters) == True
         
         
  
    return words
            
print(all_uses_only('CROSSWD.txt', 'abrz'))