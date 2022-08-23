store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",35.00)]
to_rupees = lambda data:(data[0],data[1]*79)

store_rupees = list(map(to_rupees,store))
for i in store_rupees:
    print(i)