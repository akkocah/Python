def rearranged_difference(num):
    max_num = int("".join(sorted(str(num), reverse =True)))
    min_num = int("".join(sorted(str(num))))
    return (max_num - min_num)
    

rearranged_difference(972882)

    