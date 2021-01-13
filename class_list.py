classes = []

class_name = input('Enter classs name? Enter to quit. ')

while class_name:
    classes.append(class_name)
    class_name = input('Enter class name? Enter to quit. ')

print(classes)

for c in classes:
    print(c)

# can enumerate with any sequence with 

# for index, c in enumerate(classes):
#   print(index, c)