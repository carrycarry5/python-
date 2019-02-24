# persons = {
#     "carry" : "19",
#     "miku": "16"
# }
# persons2 = {
#     "rin": "15"
# }

# for name in persons:
#     print(name + persons[name])
#

# for name in persons.items():
#     print(name)

# print(persons + persons2)

# def test():
#     '''
#     这是一个函数
#     :return:
#     '''
#
# help(test())
#
# class Person:
#     new_person = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.new_person:
#             cls.new_person = object.__new__(cls)
#         return cls.new_person
#
# p1 = Person()
# p2 = Person()
# print(id(p1))
# print(id(p2))


#

# a = 5
# print(0 <= a <= 10)

# for i in range(3,11):
#     print(i)

#
# print("*"*10)

# print("miku".index("i"))

# def length(str):
#     return len(str)
#
# print(length("miku"))
#
# arr = [[1,2,3], ["m", "i", "k", "u"]]
# for i in arr:
#     for j in i:
#         print(j)

# arr = [1,2,4,5,3]
# arr.reverse()
# print(arr)
#
# def x (a,b):
#     return b,a
#
# print(type(x(1,2) ))

try:
    print(1)
except:
    print("错了")
else:
    print("没错")

