import random

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 7

def guess_the_number():
    """
    Реалізує гру "Вгадай число".
    Програма випадковим чином обирає число, а гравець намагається його вгадати
    за обмежену кількість спроб, отримуючи підказки.
    """

    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    print(f"Вітаю! Я загадав число від {MIN_NUMBER} до {MAX_NUMBER}. Спробуйте вгадати його за {MAX_ATTEMPTS} спроб.")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            guess = int(input(f"Введіть ваше припущення ({attempt}/{MAX_ATTEMPTS}): "))

            if guess < secret_number:
                print("Занадто маленьке!")
            elif guess > secret_number:
                print("Занадто велике!")
            else:
                print(f"Ви вгадали! Це число {secret_number}. Вам знадобилося {attempt} спроб.")
                return 
        except ValueError:
            print("Будь ласка, введіть дійсне ціле число.")
            continue


    print("\nНа жаль, ви вичерпали всі спроби.")
    print(f"Загадане число було: {secret_number}.")

# Run the game
if __name__ == "__main__":
    guess_the_number()