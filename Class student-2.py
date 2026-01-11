class student:
    grade=10
    name="penguin"

    def introduction (self):
        print("Hi i am a student")
        
    def details(self):
        print("My name is", self.name)
        print("I study in grade", 10)

ob = student()
ob.introduction()
ob.details()