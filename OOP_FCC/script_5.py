# property
from datetime import datetime

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
        
    @property
    def email(self):
        print("Email accessed")
        return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
    
user1 = User("DarkVad0r", "DarkVador@gmail.com", "156")
user1.email = "this is not an email"
print(user1.email)