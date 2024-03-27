class Bank:
    def __init__(self,name,account,balance):
        self.name = name
        self.account = account
        self.balance = balance

    def mybank(self):
        print(self.name,self.account,self.balance)
        
b1 = Bank("SBI",654465416435,10)
b2 = Bank("PNB",254854644455,20)
b3 = Bank("UNION",12315687584,10000)

b1.mybank()
b2.mybank()
b3.mybank()
