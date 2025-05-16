# setter & getter
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
    
    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email
    
    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email
        
        
user1 = User("DarkVador", " Ddarkvador0@gmail.com", "156")
print(user1.email)
