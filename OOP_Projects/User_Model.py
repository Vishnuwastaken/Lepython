class User:
    def __init__(self, username, password, email, isAdmin = False):
        self.username = username
        self.password = password
        self.email = email
        self.isAdmin = isAdmin
        # self.passwordHint

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def is_admin(self):
        return self.isAdmin

    def set_username(self, new_username, exist_pass):
        # you should do some validation before setting it to a new value
        # like check password whether user exists or not, etc.
        self.username = new_username
        self.username = exist_pass

    def set_password(self, new_pass):
        # do some validation before setting up a new value
        self.password = new_pass

    def set_email(self, new_email):
    #     # do some validation before setting up a new value
        self.email = new_email

    def set_admin(self):
        # do some validation before setting up a new value
        self.isAdmin = True
