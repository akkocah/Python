n = int(input())
arr = map(int, input().split())
arr=list(arr)
print(arr)
arr=sorted(arr)
print(arr[arr.index(max(arr))])
print(arr[arr.index(max(arr))-2])
print(arr[arr.index(max(arr))-1])

# n = int(input())
# arr = map(int, input().split())
# print(list(arr))
# score = []
# for i in arr: score.append(i)
# score.sort(reverse = True)
# for i in range(len(score)):
#     if score[i] > score[i + 1]:
#         print(score[i + 1])
#         break