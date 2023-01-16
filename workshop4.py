class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

# Task 2: Add User class instance methods
    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password
# Task 3: Create BankUser subclass


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

# Task 4: Add BankUser class instance methods
    def show_balance(self):
        print(f"{self.name} has a balance of: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def transfer_money(self, amount, user_recieving_money):
        print(f"{self.name} is transferrinig ${amount} to {user_recieving_money.name}")
        print("Authentication required.")
        pin_to_validate = int(input(f"{self.name} input your pin: "))
        if pin_to_validate == self.pin:
            print("Transfer authorized.")
            user_recieving_money.deposit(amount)
            self.withdraw(amount)
            return True
        else:
            return False

    def request_money(self, amount, user_sending_money):
        print(f"{self.name} is requesting ${amount} from {user_sending_money.name}")
        print("User authentication is required...")
        pin_to_validate = int(input(f"Enter {self.name}'s PIN: "))
        password_to_validate = input(f"{self.name} enter your password: ")
        if pin_to_validate == self.pin:
            if password_to_validate == self.password:
                print(f"{self.name} your request has been authorized")
                self.transfer_money(amount, user_sending_money)
                return True
        else:
            print("Invalid PIN. Transaction canceled")
            return False


# Driver Code for Task 1 """
# user = User("Bob", 1234, "password")
# print(user.name, user.pin, user.password)

# Driver Code for Task 2
# user = User("Bob", 1234, "password")
# print(user.name, user.pin, user.password)
# user.change_name("Nicole")
# user.change_pin(4321)
# user.change_password("newpassword")
# print(user.name, user.pin, user.password)


# Driver Code for Task 3
# user = BankUser("Nicole", 1234, "Password")
# print(user.name, user.pin, user.password, user.balance)


# Driver Code for Task 4
# user = BankUser("Nicole", 1234, "password")
# user.show_balance()
# user.deposit(50)
# user.show_balance()
# # print(user.balance)
# user.withdraw(10)
# user.show_balance()


# Driver Code for Task 5
user1 = BankUser("Nicole", 1234, "password")
user2 = BankUser("Bob", 4321, "newpassword")
user1.deposit(500)
user2.deposit(5000)
user2.show_balance()
user1.show_balance()
# print()
# # user1.transfer_money(1000, user2)
# print()
# user2.show_balance()
# user1.show_balance()
# print()
if user2.transfer_money(500, user1) is True:
    user2.show_balance()
    user1.show_balance()
    user2.request_money(100, user1)
else:
    print("not valid")

user2.show_balance()
user1.show_balance()
# user2.request_money(500, user1)
# print()1234
# user2.show_balance()
# user1.show_balance()
