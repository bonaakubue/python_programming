#user-defined exceptions
class CustomError(Exception):
    def __init__(self, message="custom error"):
        self.message = message

#catching user-defined exception
try:
	raise CustomError
except CustomError:
	print('Custom Exception')

