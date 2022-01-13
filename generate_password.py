import random

size = int(input("What is the size of your password? "))
string = "ABCDEFGHIJJLMNOPQSRTUVWXYZ" \
         "abcdefghijklmnopqrstvwxyz" \
         "1234567890" \
         "!£$%&*()=+[]{}@#<>?/"

# Use the .join for receive the array random
password = "".join(random.sample(string, size))
print(password)
