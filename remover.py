import os
x = int(input('meddig?'))
for i in range(x):
    név=str(str(i)+'.txt')
    os.remove(név)
