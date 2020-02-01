lst = ['user1', 'user2', 'user3']
d = {x: {'preference' + str(i): 0 for i in range(1,5)} for x in lst}

print(d)

print(d['user1']['preference1'])