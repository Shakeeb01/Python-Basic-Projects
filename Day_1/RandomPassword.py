import random

Length = int(input("What should be the length of Password : "))

characters = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

password = ''

for i in range(Length):
    random_index = random.randint(0,len(characters) - 1)
    password = password + characters[random_index]
    
print(f"Your Password is {password}")    