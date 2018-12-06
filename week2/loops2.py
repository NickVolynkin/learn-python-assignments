import datetime
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='ask_user.log')


def ask_user():
    while True:
        try:
            user_input = input("\nКак дела?\n")
            logging.info('input: "{}"'.format(user_input))
            answer = get_answer(user_input.lower())
        except (KeyboardInterrupt, EOFError) as exc:
            # Ctrl+C is KeyboardInterrupt,
            # Ctrl+D is EOFError
            logging.info(str(type(exc)))
            answer = get_answer(type(exc))
        except Exception as exc:
            logging.error(exc)
            answer = get_answer(Exception)

        if type(answer) is list:
            for a in answer:
                run_answer(a)
        else:
            run_answer(answer)


def run_answer(answer):
    if callable(answer):
        logging.info('calling: {}'.format(str(answer)))
        output = answer()
    else:
        output = answer

    logging.info('output: "{}"'.format(output))
    print(output)


def get_answer(user_input):
    known_questions = {
        "время": time,
        "дата": date,
        "learn": "python",
        "хорошо": ['Пока!', lambda: exit(0)],
        KeyboardInterrupt: ['Пока!', lambda: exit(1)],
        EOFError: ['Пока!', lambda: exit(1)],
        Exception: ['Что-то пошло не так.', lambda: exit(2)]
    }

    answer = known_questions.get(user_input, '¯\_(ツ)_/¯')

    return answer


def time():
    return datetime.datetime.now().time()


def date():
    return datetime.datetime.now().date()


if __name__ == '__main__':
    ask_user()
