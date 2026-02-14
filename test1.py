import random
import time


print("Welcome to the password generator!")
time.sleep(3)
print("We will give you a password shortly!")
time.sleep(3)



adjectives = ["Big", "Small", "Tall", "Short", "Fast", "Slow", "Hot", "Cold",
    "Happy", "Sad", "Good", "Bad", "New", "Old", "Young", "Clean",
    "Dirty", "Loud", "Quiet", "Bright",
    "Brave", "Calm", "Clever", "Creative", "Curious", "Dangerous",
    "Delicious", "Elegant", "Fancy", "Friendly", "Gentle", "Grumpy",
    "Honest", "Kind", "Lazy", "Nervous", "Polite", "Proud",
    "Silly", "Wise",]
  
nouns = ["dino", "car", "computer", "cat", "dog", "fish", "thing", "hammer", "toaster", "fan", "panda", "dragon"]

def fun_test():
    print("this is func_test")
    a = 10
    print("end of fun_test")

while True:
    time.sleep(3)
    print("Thinking...")
    time.sleep(2.5)
    
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    character = "!"
    password = adjective + noun + str(number) + character
    
    print(f"Your password is [{password}]!")
    time.sleep(2.5)
    response = input("Would you like another password? Type y or n: ")
    
    
    
    if response == "n" or response == "N":
        time.sleep(2.3)
        print("Okay bye!")
        break

