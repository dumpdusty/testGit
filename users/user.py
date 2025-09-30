class User():
    def __init__(self, firstName, lastName, age, role):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.role = role

    def get_info(self):
        print(f'User info: name: {self.firstName} {self.lastName}, age: {self.age}, role: {self.role}')
    
    def change_role(self, new_role):
        self.role = new_role