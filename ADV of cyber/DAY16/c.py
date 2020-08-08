import os
ListFile = os.listdir('decom2')
for l in ListFile:
    f = open('decom2/' + l, 'r')
    data = f.read()
    f.close()
    if "password" in data:
        print(l)
