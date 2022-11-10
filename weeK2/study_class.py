class Person:
    def __init__(self, param_name):
        print("i am created! ", self)
        self.name = param_name

    def talk(self):
        print("안녕하세요, 제 이름은", self.name, "입니다.")

person1 = Person("조용연")
print(person1.name)
print(person1)
person1.talk()
person2 = Person("일라이")
print(person2.name)
print(person2)
person2.talk()