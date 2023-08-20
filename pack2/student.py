class Dispstu():
    def __init__(self,sid,sname,sal):
        self.sid = sid
        self.sname = sname
        self.sal = sal
    def display(self):
        print("sid:{} sname:{} sal:{}".format(self.sid,self.sname,self.sal))