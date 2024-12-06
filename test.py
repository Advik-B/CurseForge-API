import curseforge

print(dir(curseforge))
for item in dir(curseforge):
    print(curseforge.__getattribute__(item))
# print(curseforge.add(1, 2))