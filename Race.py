class bike:
    def start(self):
        print("Bike is Starting Now")
    def stop(self):
        print("Bike is Stops Now")
class Glamer(bike):
    def race(self):
        print("Bike is running ")

mybike = Glamer()
mybike.start()
mybike.stop()
mybike.race()
