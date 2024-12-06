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

engine = curseforge.CurseForgeAPI("$2a$10$wY4AcSOcrrRN20zLIYhFaeWS8f9oE.XcxoRHxLH3pbL0Zib6NYyFG")

x = engine.fetch("/v1/games/432", curseforge.json())

print(x)