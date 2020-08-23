#reorder_digits([515, 341, 98, 44, 211], "asc")

def reorder_digits(lst, direction):
    new=[]
    for i in lst:
        if direction == "asc":
            new.append(int("".join(sorted(str(i)))))
        elif direction == "desc":
            new.append(int("".join(sorted(str(i), reverse= True))))
    return new
print(reorder_digits([515, 341, 98, 44, 211,42], "desc"))

##############################################################################
def reorder_digits(lst, direction):
    
    return [int("".join(sorted(str(i), reverse = direction=="desc"))) for i in lst]

print(reorder_digits([515, 341, 98, 44, 211,42], "desc"))
print(reorder_digits([1, 2, 3, 4], "asc"))

##########################################################################3

def reorder_digits(lst, direction): 
    return [int(''.join(sorted(str(i),reverse=direction=="desc"))) for i in lst]
print(reorder_digits([515, 341, 98, 44, 211,895], "asc"))

#################################################################################33

def reorder_digits(lst, order):
    return ["".join(sorted(str(x),reverse=0)) if order=="asc" else "".join(sorted(str(x),reverse=1)) for x in lst]
print(reorder_digits([515, 341, 98, 44, 211,895], "desc"))

########################################################################################

def reorder_digits(lst, reverse):
    final_lst = list()
    a = ''
    if reverse == "desc":
        rev = True
    else: rev = False
    for i in lst:
        for j in sorted(str(i), reverse = rev):
            a += j
        final_lst.append(int(a))
        a = ''
    print(final_lst)
reorder_digits([515, 341, 98, 44, 211], "desc")    