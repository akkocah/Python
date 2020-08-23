def correct_spacing(sentence):
    return (" ".join(sentence.split()))

print(correct_spacing(" Always look on    the bright   side of  life."))

def correct_spacing(sentence):
    return " ".join([i for i in sentence.split(" ") if i != ""])

print(correct_spacing(" Always look on    the bright   side of  life."))