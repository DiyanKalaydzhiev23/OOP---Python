class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
            return
        raise ValueError('The username must be between 5 and 15 characters.')

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.check_length(value) and self.check_upper(value) and self.check_digits(value):
            self.__password = value
            return
        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    @staticmethod
    def check_length(password):
        return len(password) >= 8

    @staticmethod
    def check_upper(password):
        return [letter for letter in password if letter.isupper()]

    @staticmethod
    def check_digits(password):
        return [letter for letter in password if letter.isdigit()]

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*"*len(self.password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
