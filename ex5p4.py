class Soldier():
    def __init__(self, name):
        self.name = name

class Act_of_Shooting(Soldier):
    def __init__(self,name):
        super().__init__(name)
        self.bullets = 3
    def fire(self):
        if self.bullets <= 0:
            print('Bullets are not. Use metod reloads.')
        else:
            self.bullets -= 1
            print('tigi-tigitishh')
            print('Bullets in magazine: ', self.bullets)
    def reloads(self):
        self.bullets = 3
        print('Ready to fire!')

a = Act_of_Shooting('Ryan')
a.fire()
a.fire()
a.fire()
a.fire()
a.reloads()
a.fire()
