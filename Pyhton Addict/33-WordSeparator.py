# Ask user to enter a word, a separator and number of repetitions. Write a Python code displaying the word with repetition times and having each word separated with separator character
word, sep, repeat = map(str, input().split())
def text(word,sep,repeat):
    return sep.join(word.split()*int(repeat))
    
print(text(word,sep,repeat))

##############################################################

word = input("word : ")
separator = input("separator : ")
repetitions = int(input("repetitions : "))
liste = []
for i in range(repetitions):
    liste.append(word)
print(separator.join(liste))

print(separator.join([word for i in range(repetitions)]))
