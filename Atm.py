class atm():
    def __int__(self):
        self.c = int(input("Enter card no"))

    def deposite(self):
        self.pin = int(input("Enter a Pin"))
        if(getpin(self.c) == self.pin):
            updateAmount(self.atm)

ICICI = atm()

if ICICI:
    while 1:
        print("-----------------ATM----------------- \n Choose Your Option \n Press 1 =>Withdrawl \n Press 2 =>Deposite \n Press 3 =>Set pin \n Press 4 =>Check Balance \n Press 5 =>Exit")
        op = int(input("Enter your Choise : "))
        if op>0 and op<6:
            if op == 1:
                ICICI.Withdrawl()
            elif op == 2:
                ICICI.Deposite()
        #     elif op == 3:
        #         ICICI.Set pin()
        #     elif op == 4:
        #         ICICI.Check Balance()
        # else:
            print("***************** Wrong Input *****************")
else:
    print("************** ATM Out of Servise **************")



