# class User:
#     def __init__(self, name):

# make a instance
# tom = User("")
# tom.name = "Tom"
# tom.score = 20
#
# bob = User()
# bob.name = "Bob"
# bob.score = 40
#
# print(tom.score)

class User:
    count = 0
    # default constructor
    def __init__(self, name):
        User.count += 1
        # instance variable
        self.name = name

    # instance method
    def print_name(self):
        print(self.name)
    # class method
    @classmethod
    def show_info(cls):




print(User.count)
tom = User("tom")
tom.print_name()
