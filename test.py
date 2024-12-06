import curseforge

print(dir(curseforge))
for item in dir(curseforge):
    print(item, ":", getattr(curseforge, item))
