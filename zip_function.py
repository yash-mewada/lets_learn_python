usernames = ["dude","bro","mister"]
passwords = ("p@ssword","abc1234","guest")

users = dict(zip(usernames,passwords))
for key,value in users.items():
    print(key+" : "+value)