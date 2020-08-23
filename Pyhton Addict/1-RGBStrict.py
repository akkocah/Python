# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], 
# it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
list = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
newlist = []
for i in list:
    if i == 'R':
        newlist.append(i)
for i in list:
    if i == 'G':
        newlist.append(i)
for i in list:
    if i == 'B':
        newlist.append(i)
######################################################
print(newlist)

newlist = ["R"] * list.count("R") + ["G"] * list.count("G") + ["B"]*list.count("B")

print(newlist)

############################################################333##################

newlist = [x for x in list if x == "R"] + [y for y in list if y == "G"] + [z for z in list if  z == "B"]

print(newlist)
###########################################################################################3
my_rgb = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
def array_rgb(my_rgb):
    r_count = 0
    g_count = 0
    b_count = 0
    for i in range(len(my_rgb)):
        if my_rgb[i] == 'R':
            r = my_rgb.pop(i)
            my_rgb.insert(r_count, r)
            r_count += 1
        elif my_rgb[i] == 'G':
            g = my_rgb.pop(i)
            my_rgb.insert(r_count+g_count, g)
            g_count += 1
        else :
            my_rgb[i] == 'B'
            b = my_rgb.pop(i)
            my_rgb.insert(r_count+g_count+b_count, b)
            b_count += 1        
    return my_rgb

print(array_rgb(my_rgb))

#################################################################333

chars = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
new_chars = []
for i in (sorted(set(chars))):
    i_index = chars.count(i)
    for j in range(i_index):
        new_chars.insert(j,i)
print(new_chars)

##############################################################33
data = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
data = [*[i for i in data if i=="R"],*[i for i in data if i=="G"],*[i for i in data if i=="B"]]
print(data)

#######################################################
array=["G","B","R","R","B","R","G"]
array_2=[]
def line(array, letter):
    array_1=[x for x in array if x==letter]
    array_2.extend(array_1)
    return array_2
for i in "R","G","B":    
    line(array,i)
print(array_2)