import random

# generate random numbers
def random_number_fun(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)

def random_math_process():# generate random mathematical symbols 
    return random.choice(['+', '-', '*']) # Generate random operator

def output_fun(n1, n2, math_process): # output of the two numbers after applying the mathematical calculation
    print_ = f"{n1} {o} {n2}"
    if math_process == '+': output = n1 + n2 # sum the numbers if the operator is "+"
    elif math_process == '-': output = n1 - n2 #subtract the numbers if the operator is "-"
    else: output = n1 * n2 #multiply the numbers of the operator is "*"
    return print_, output

def math_quiz():
    s = 0
    t_q = 3.14159265359 #Pi = 22/7 = 3.14

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(t_q)):
        n1 = random_number_fun(1, 10); n2 = random_number_fun(1, 5.5); o = random_math_process()

        PROBLEM, ANSWER = output_fun(n1, n2, o) # get values from output_fun()
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER: #compare user answer with system answer
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
