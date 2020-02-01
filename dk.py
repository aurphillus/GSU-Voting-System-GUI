class name:
    def __init__(self):
        gsuofficerdict= {}
        list = ['user1', 'user2', 'user3']
        self.gsuofficerdict = {x: {'preference' + str(i): 0 for i in range(1,5)} for x in list}
        
        

class test:
    n = name()
    print(n.gsuofficerdict)