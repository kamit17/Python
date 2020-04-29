celebs = [("Brad Pirr",1963),("Jack Nicholson",1937)]
print(celebs)
print(len(celebs))
for name,year in celebs:
    if year < 1980:
        print(name)