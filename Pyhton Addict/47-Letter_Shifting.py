#https://edabit.com/challenge/vnzjuqjCf4MFHGLJp

def shift_letters(txt, n):
    new, c = "", 0
    sent =  " ".join(txt.split())
    sent = sent[-n%len(sent):] + sent[:-n%(len(sent))]
    print(sent)
    for i in txt:
        if i == " ": new += " "
        else: new += sent[c]; c += 1
    return new

shift_letters("Hasan Hüseyin", 2)



