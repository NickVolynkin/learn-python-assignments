import datetime


def ask_user():
    known_questions = {
        "время": time,
        "дата": date,
        "learn": "python"

    }
    while True:
        try:
            user_input = input("Как дела?\n").lower()
            print('({})'.format(user_input))
            if user_input == "хорошо":
                print("Пока!")
                break
            elif user_input in known_questions:
                answer = known_questions[user_input]
                if callable(answer):
                    print(answer())
                else:
                    print(answer)
        except KeyboardInterrupt:
            print("\nПока!")
            break


def time():
    return datetime.datetime.now().time()


def date():
    return datetime.datetime.now().date()


if __name__ == '__main__':
    ask_user()
