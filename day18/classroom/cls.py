def myfind(collection, valuetofind):
    for index in range(len(collection)):
        if collection[index] == valuetofind:
            return index
print(myfind(["luka", "lile", "nia"], "lile"))