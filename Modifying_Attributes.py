#Example code to show the value of attributes can be changed based on some behavior
# Added a method to send an email, which updates the is_sent variable to True.
class Email:
    def __init__(self):
        self.is_sent = False
    def send_email(self):
        self.is_sent = True

my_email = Email()
my_email.is_sent
#returns False
my_email.send_email()
my_email.is_sent
#returns True
