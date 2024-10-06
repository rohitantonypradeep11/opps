class student:
    grade = 8
    name = "rohit"
    def intro(self):
        print("hi i am a student") 
    def deatail(self):
        print ("my name is ",self.name)  
        print ("i am in grade ",self.grade)    
ob = student()
ob.intro()
ob.deatail()