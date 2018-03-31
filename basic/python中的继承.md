```
class human():
    def __init__(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        print("my age is ", self.age)

class man(human):
    def power(self):
        print("man has strong power")

class woman(human):
    def hello(self):
        print("women say hello")

if __name__ == "__main__":
    man = man("小明")
    man.setAge(16)
    man.getAge()
    print(man.name)
    man.power()
 ```
