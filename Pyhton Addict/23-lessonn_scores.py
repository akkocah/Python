from random import randint
scores = dict((f"Student-{x}", dict((f"Lesson-{y}", randint(35,100)) for y in range(1,6))) for x in range(1,6))

print(scores)

print("********************************")

from random import randint
print({f'Student-{x}': {f'Lesson-{y}': randint(35, 100)
                        for y in range(1, 6)} for x in range(1, 6)})

print("*************************")
from random import randint
test = {}
for i in range(1,6):
    test[f"student- {i}"] = {f"lesson-{j}" : randint(35,100) for j in range(1,6)}
print(test)