class Famly:
    def Gnd(self):
        print("This is a Grand Father")

class father(Famly):
    def fat(self):
        print("This is a father")

class mother(Famly):
    def mot(self):
        print("This is a Mother")
fam = mother()
fam.mot()
fam.fat()
fam.Gnd()
