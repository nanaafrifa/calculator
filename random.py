import random

cars = ["volvo","toyota","vw","nissan","jaguar","land rover"]
old = random.sample(cars,4)
new = [x for x in cars if x not in old]
print(old)
print(new)
