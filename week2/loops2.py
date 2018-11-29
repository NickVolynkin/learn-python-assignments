import datetime


def ask_user():
    while True:
        try:
            user_input = input("\nКак дела?\n").lower()
            answer = get_answer(user_input)
        except (KeyboardInterrupt, EOFError) as exc:
            # Ctrl+C is KeyboardInterrupt,
            # Ctrl+D is EOFError
            answer = get_answer(type(exc))

        if type(answer) is list:
            for a in answer:
                process_answer(a)
        else:
            process_answer(answer)


def process_answer(answer):
    if callable(answer):
        print(answer())
    else:
        print(answer)


def get_answer(user_input):
    known_questions = {
        "время": time,
        "дата": date,
        "learn": "python",
        "хорошо": ['Пока!', quit_program],
        KeyboardInterrupt: ['Пока!', quit_program],
        EOFError: ['Пока!', quit_program],
        None: '¯\_(ツ)_/¯'
    }

    if user_input in known_questions:
        answer = known_questions[user_input]
    else:
        answer = known_questions[None]

    return answer


def time():
    return datetime.datetime.now().time()


def date():
    return datetime.datetime.now().date()


def quit_program():
    exit(0)


if __name__ == '__main__':
    ask_user()
