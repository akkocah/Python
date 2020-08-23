# QUESTION:
# Write a Python function to process all mathematical operations in below list.
# operations = ["5 + 6", "2 * 3", "8 / 4", "4 - 5"]
operations = ["51 + 6", "2 * 3", "8 / 4", "4 - 5"]
a = [eval(i) for i in operations]

print(a)

operations = ["51 + 6", "2 * 3", "8 / 4", "4 - 5","100 * 5"]
result_operations = []
for i in operations:
    a,b,c = i.split(" ")
    if b == "+" :
        result = int(a) + int(c)
    elif b == "*":
        result = int(a) * int(c)
    elif b == "/":
        result = int(a) / int(c)
    else:
        result = int(a) - int(c)

    result_operations.append(result)
print(result_operations)
###############################################
##############################################3
def operate(text):
    for i in range(len(text)):
        args = text[i].split()
        a = (lambda x,opr,y : int(x)+int(y) if opr == '+' else \
            (int(x)-int(y) if opr == '-' else (int(x)*int(y) if opr == '*' else int(x)/int(y)))) \
            (args[0],args[1],args[2])
        print(f"{text[i]} = {a}")
operations = ["51 + 6", "2 * 3", "8 / 4", "4 - 5","100 * 5"]
operate(["51 + 6", "2 * 3", "8 / 4", "4 - 5","100 * 5"])