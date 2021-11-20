people = {"Rachel": 21, "Sean": 22}
print(type(people))
empty_dict = dict()
people["William"] = 21
print(people)
print(people["William"])
print(list(people))
print(len(people))
names = list(people.keys())
for name in names:
    print(name)
people_old = {"Daryl": 22, "Mildred": 23}
print(people_old)
people.update(people_old)
print(people)
for i in  range(1, 11):
    print(i)
numbers2 = [i for i in range(1, 101)]
print(numbers2)
numbers3 = [i for i in range(1, 101) if i % 2 == 0]
print(numbers3)
numbers4 = [i*i for i in range(1, 101) if i % 2 == 0]
print(numbers4)