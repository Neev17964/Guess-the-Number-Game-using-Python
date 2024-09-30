import random 
random_number = random.randint(1,100)

print("The System has randomly generated an number \n Now Guess the Number!!")

Name = input("Enter Your Name for Scoreboard: ")

user = int(input("Enter Your Guess: "))

count1 = 0
count2 = 0

while user < random_number:
    print("The Number is higher than this") 
    user = int(input("Enter Your Guess Again: "))

    while user > random_number:
         print("The Number is lower than this")    
         user = int(input("Enter Your Guess Again: ")) 
         count2 += 1

    count1 += 1 

count = count1 + count2 + 1  # The Extra plus one for the correct guess

print("Congrats You Guessed the Number!!!!")    
print(f"The total number of guesses it took you is {count}")     


# ScoreCard 

content = f"\n{Name}:{count}\n"
with open("scoreboard.txt", "a") as f:
     f.write(content)