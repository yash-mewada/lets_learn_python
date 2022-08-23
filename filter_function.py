friends = [("rachel",19),
           ("monica",18),
           ("phoebe",20),
           ("ross",16),
           ("joey",17),
           ("chandler",20)]

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age,friends))
for i in drinking_buddies:
    print(i)