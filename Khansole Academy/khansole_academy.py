import random

def main():
    '''
    print("Khansole Academy")
    num1, num2, answer = generate_question()
    print("What is", num1, "+", num2, "?")
    user_answer = int(input("Your answer: "))
    result = check_answer(user_answer, answer)
    print(result)
    '''
    print("Khansole Academy")
    correct_count = 0
    while correct_count < 3:
        num1, num2, answer = generate_question()
        print("What is", num1, "+", num2, "?")
        user_answer = int(input("Your answer: "))
        if check_answer2(user_answer, answer):
            correct_count += 1
            print("Correct! You've gotten", correct_count, "correct in a row.")
        else:
            correct_count = 0
            print("Incorrect. The expected answer is", answer)
    
    print("Congratulations! You mastered addition.")

def generate_question():
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    answer = num1 + num2
    return num1, num2, answer

def check_answer2(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return "Correct!"
    else:
        return "Incorrect. The expected answer is " + str(correct_answer)
    
if __name__ == '__main__':
    main()
