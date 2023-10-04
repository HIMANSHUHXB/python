#Class Inheritence 
class Dog:
    _legs=4
    def __init__(self,name):
        self.name=name

    def speak(self):
        print(self.name +'says Bark!!')

    def legs(self):
        return self._legs
   
class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says:Yap yap yap!!')
    def wagTail(self):
        print('Vigorous wagging!!')

dog = Chihuahua('Roxy')
dog.speak()
dog.wagTail()