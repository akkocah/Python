# Sayılardan oluşan bir String içinde bulunan [tek, çift, tek,...] veya 
# [çift, tek, çift,...] 
# şeklinde var olan en uzun patterni çıktı veren program.
# longest_substring("225424272163254474441338664823") ➞ "272163254"
# # substrings = 254, 272163254, 474, 41, 38, 23

# longest_substring("594127169973391692147228678476") ➞ "16921472"
# # substrings = 94127, 169, 16921472, 678, 476




def longest_substring ( n ):
    txt=''
    for i in range(len(n)-1):
        if int(n[i])%2==int(n[i+1])%2:
            txt=txt[:-1]+n[i]+" "+n[i+1]
        else: txt=txt[:-1]+n[i]+n[i+1]
    return sorted(txt.split(),key=len,reverse=True)[0]
print(longest_substring ( "844929328912985315632725682153" ))  # 56327256

