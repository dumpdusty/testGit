from user import User

user_1 = User('Jack', 'Sparrow', 29, 'captain')
user_2 = User('Will', 'Turner', 19, 'sailor')

print(user_1.role)

user_1.get_info()
user_2.get_info()



user_2.change_role('skipper')
user_2.get_info()



