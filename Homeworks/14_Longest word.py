sentence = input("Enter your sentence : ")
sentence = sentence.split()

longest_word = []
longest =0
i = 0

while i < len(sentence):
    if len(sentence[i]) > longest:
        longest = len(sentence[i])
        longest_word = sentence[i]
    i += 1
print(f"The longest word of your sentence is: {longest_word} and \
it's lenght is : {longest} characters.")
