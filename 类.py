class Student():
    name = "dana"
    age = 18
    
    # 注意say的写法，参数由一个self
    def say(self):
        self.name = "aaaa"
        self.age = 200
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))
        
    def sayAgain(s):
      
        print("My name is {0}".format(s.name))
        print("My age is {0}".format(s.age))
          
yueyue = Student()
yueyue.say()
yueyue.sayAgain()
print()
print("*" *20)
class Teacher():
    name = "dana"
    age = 19
    
    def say(self):
        self.name = "yaona"
        self.age = 17
        print("My name is {0}".format(self.name))
        # 调用类的成员变量需要用 __class__
        print("My age is {0}".format(__class__.age))
    def sayAgain():
        print(__class__.name)
        print(__class__.age )
        print("Hello, nice to see you again")
        
t = Teacher()
t.say()
# 调用绑定类函数使用类名
Teacher.sayAgain()