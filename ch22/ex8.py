# Validating user inputs
#validations

class User:
    def __init__(self):
        self._username = ""

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if len(value) >= 3:
            self._username = value
        else:
            raise ValueError("name must be at least 4 characters long.")

user = User()
user.username = 'adams'
print(user.username)
user.username = 'ad'
