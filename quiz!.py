#---------------------------------------------
guesses =[]
def new_game():
    guesses =[]
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------------------------")
        print(key)
        for i in options[question_num-1 ]:
            print(i)
        guess = input("Enter (A, B, C,or D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses, guesses)
#---------------------------------------------
def check_answer(answer,guess):
    if answer == guess:
        print(" CORRECT! ")
        return 1
    else:
        print(" WRONG! ")
        return 0
 
#----------------------------------------------
def display_score(correct_guesses, guess):
    print("----------------------------------")
    print(" RESULTS ")
    print("-----------------------------------")
    
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
#-----------------------------------------------
def play_again():

    response = input("Do you want to play again?(yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
     
#------------------------------------------------

questions ={
    "Who created Python? : ": "A",
    "What year was Python created? :":"B",
    "Python is tributed to which comedy group?: ": "C",
    "Is python a two snakes ?: " : "A"}


options =[["A. Guido van Rossum", "B. Dennis Ritchie", "C. James Gosling", "D. Linus Torvalds"],
          ["A. 1985", "B. 1991", "C. 2000", "D. 1995"],
          ["A. The Marx Brothers", "B. The Three Stooges", "C. Monty Python", "D. Saturday Night Live"],
           ["A. No", "B. Yes", "C. Maybe", "D. Not Sure"]]
new_game()

while play_again():
    new_game()

print("THANK YOU!")