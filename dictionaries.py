capitals = {"usa":"washington dc",
            "india":"new delhi",
            "china":"beijing",
            "russia":"moscow"
           }
#capitals.update({"germany":"berlin"})
#capitals.update({"usa":"texas"})
#capitals.pop("china")
#capitals.clear()

print(capitals["russia"])
print(capitals.get("brazil"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
for key,value in capitals.items():
    print(key,value)