utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

utensils.add("napkin")
#adds the value napkin in the set utensils
utensils.remove("fork")
#removes the value fork from the set utensils
utensils.clear()
#clears the set utensils
dishes.update(utensils)
#adds one set to another
dinner_table = utensils.union(dishes)
#joins 2 or more sets together

print(dishes.difference(utensils))
#finds if there is any similar data in the sets dishes and utensils
print(utensils.intersection(dishes))
#this will return any values that are common in both the sets

for x in utensils:
    print(x)