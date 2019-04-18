from chain_of_actions import ChainOfActions


@ChainOfActions
def add_test(x, y):
    return x + y


@ChainOfActions
def mul_test(x, y):
    return x * y


@ChainOfActions
def sub_test(x, y):
    return x - y


dataset = [(10, 20), (4.5, 6.7), ("55", 78), (None, False)]
ChainOfActions.add_data(dataset)

ChainOfActions.run()
