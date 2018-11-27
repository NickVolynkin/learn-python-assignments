

def get_summ(num_one, num_two):
    try:
        one = int(num_one)
        two = int(num_two)
        return one + two
    except ValueError:
        return 0

