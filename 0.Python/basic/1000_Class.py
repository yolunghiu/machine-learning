class Car(object):
    def __init__(self, name):
        self.name = name

    def run(self, faster=False):
        if faster:
            print('The ' + self.name + ' car is running faster')
        else:
            print('The ' + self.name + ' car is running fast', self.name)

qq = Car('qq')
qq.run()

bmw = Car('bmw')
bmw.run(True)

