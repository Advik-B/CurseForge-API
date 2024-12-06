import curseforge
# import json
# from curseforge import json

def inspect(obj):
    for item in dir(obj):
        if type(getattr(obj, item)) == callable:
            inspect(getattr(obj, item))
        else:
            print(item, ":", getattr(obj, item))


inspect(curseforge)
