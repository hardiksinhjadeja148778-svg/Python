class AgeError(Exception):
    def __init__(self, message="Age must be 18 or above"):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise AgeError()
    print("Eligible to vote")

try:
    check_age(int(input("Enter age: ")))
except AgeError as e:
    print("Error:", e)