from flatonacci import flatonacci


def str_to_list(string: str):
    separated_list = list(string.split(","))
    return [int(s) for s in separated_list]


if __name__ == '__main__':
    valid = False
    while not(valid):
        try:
            signature = str(
                input('Please enter the signature separated by a comma (e.g. 1, 2, 3): '))
            n = int(input('Please enter the size of the sequence: '))
            print('The calculated sequence is: {}'.format(
                flatonacci(str_to_list(signature), n)))
            valid = True
        except (NameError, RuntimeError, TypeError, ValueError) as error:
            print('Something went wrong. Please verify the input data and try again.\nError description: {}\n\n'.format(error))
