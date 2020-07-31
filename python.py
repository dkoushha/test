import sys
print(sys.version)
print('something')


def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting


# print(greet('World'))
# print(greet('Name'))
# print(greet('Name'))
