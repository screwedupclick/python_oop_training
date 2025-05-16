class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
    

        
user1 = User("DarkVador", " Darkvador@gmail.com", "156")


# En Python, _variable est "protégée" (convention : usage interne ou sous-classes), __variable est "privée" (name mangling pour limiter l'accès direct).
# Ces mécanismes reposent sur des conventions et n'empêchent pas techniquement l'accès extérieur.
