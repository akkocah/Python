# QUESTION:
# This is an interview question asked by Microsoft.
# Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.
# For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.


text = "Hello world"
index = 0
def read7():
    global index
    temp = text[index:index+7]
    index += len(temp)
    return temp
print(read7())

class fileread:
    def __init__(self):
        self.leftover = ""
    def readN(self, n):
        value = self.leftover
        text = None
        while len(value) < n and (text is None or len(text) == 7):
            text = read7()
            value += text
        self.leftover = value[n:]
        return value[:n]

############################################################

class Reader():
    def __init__(self, txt):
        self.index = 0
        self.txt = txt
    def read7(self):
        temp = self.txt[self.index:self.index+12]
        self.index += len(temp)
        return temp
myreader = Reader("Hello world hasan")
print(myreader.read7())

leftover = ""
def readN(n):
    global leftover
    value = leftover
    text = None
    while len(value) < n and (text is None or len(text) == 7):
        text = read7()
        value += text
    leftover = value[n:]
    return value[:n]

