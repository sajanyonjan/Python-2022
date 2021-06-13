class Person:
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email
    def info(self):
        return f'Your name is {self.first} {self.last}. Your can be mailed at {self.email}'
class Sajan(Person):
    def __init__(self, college):
        super().__init__(self, first, last, email)
        self.college = college
    def college(self):
        return f'Hey Mr. {self.name} your college is {self.college}'
bio = Person('sajan', 'tamang', 'sajanyounjan14@gmail.com')
print(bio.info())
bio1 = Sajan('Sajan', 'Tamang', 'sajanyonjan14@gmail.com', 'Trichandra')
print(bio1.college())
