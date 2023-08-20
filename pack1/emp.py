class employee():
    def __init__(self,eid,ename,sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal
    def display(self):
        print("empid:{} emname:{} emsal:{}".format(self.eid,self.ename,self.sal))