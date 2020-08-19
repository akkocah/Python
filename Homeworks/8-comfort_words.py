sentence = input("Please write your sentences: ")
left_hand = ("q", "a", "z", "w", "s", "x", "e", "d",
             "c", "r", "f", "v", "t", "g", "b")
right_hand = ("y", "h", "n", "u", "j", "m", "ı", "k",
              "ö", "o", "l", "ç", "p", "ş", "ğ", "i", "ü")
a = set(sentence.lower())
b = set(right_hand)
c = set(left_hand)


#comfort_words = (bool((a.intersection(b)) and (a.intersection(c)))) buda kullanılabilir.
comfort_words = (bool((a & b) and (a & c)))
print("This sentences is comfort words." * (comfort_words))
print("This sentences is not comfort words." * (not comfort_words))
