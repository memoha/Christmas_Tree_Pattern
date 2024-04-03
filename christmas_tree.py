height = 10
for i in range(1, height+1):
 spaces = ' ' * (height-i)
 stars = '*' * (2*i - 1)
 print(spaces + stars)

 space2 = ' ' * (height-i)
 decor = '.' * (2*i-1)
 print(space2 + decor)

 space3 = ' ' * (height-2)
 trunk = '|_|'
 print(space3 + trunk)
