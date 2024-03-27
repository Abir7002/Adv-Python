class RBI:
    def Interest(self):
        return 7

class SBI(RBI):
    def Interest(self):
        return 10

class PNB(RBI):
    def Interest(self):
        return 15

mysbi = SBI()
print("SBI Interest is : ",mysbi.Interest(),"%")
