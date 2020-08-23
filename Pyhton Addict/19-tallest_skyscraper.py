# def tallest_skyscraper(lst):
#     a = zip(*(lst))
#     print(list(a))
#     b = max([i.count(1) for i in a])
#     return b
    
 
def tallest_skyscraper(lst):
    a = zip(*lst)
    #b = max([i.count(1) for i in a])
    b = []
    for i in a:
        b.append(i.count(1))
                
    return max(b), b





print(tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]))