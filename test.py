class MyClass(object):
    def __init__(self, number, color):
        self.number = number
        self.color = color


my_objects = []

for i in range(32):
    if i % 2 == 0:
        my_objects.append(MyClass(i, "w"))
    else:
        my_objects.append(MyClass(i, "b"))

# later

for obj in my_objects:
    if obj.number % 3 == 0:
        del obj
    else:
        print(f"{obj.number} {obj.color}")
