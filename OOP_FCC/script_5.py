# property
from datetime import datetime

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
    @property
    def email(self):
        print("Email accessed")
        return self.email
    
user1 = User("DarkVad0r", "DarkVador@gmail.com", "156")
print(user1.email)