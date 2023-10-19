# Import library
from faker import Faker

# Init fake object 
fake = Faker()
profile = fake.simple_profile()

# Print fake data
KEY_COLOR = '\033[91m'
END = '\033[0m'
for i in profile:
    print(f"{KEY_COLOR}{i.upper()}{END}: {profile[i]}")