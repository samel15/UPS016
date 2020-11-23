def ask_yes_no(question):
    """
    Asks the question you can answer yes or no, if the user enters different characters than y/Y or n/N, asks again.
    :param question: Enter a question that can be answered with yes or no(y/n)
    :return: user response
    """
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """
    Asks about the number of winners, if the user enters a number out of range, asks again.
    :param question: Enter a question about the number of winners to draw, add information about the established range
    :param low: the minimum number in the established range
    :param high: the maximum number in the established range
    :return: number of winners to draw from the established range, chosen in the console by the user.
    """
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response
