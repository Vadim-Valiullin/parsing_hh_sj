def decorator(function):
    def sum_on_str(object, other):
        if type(other) == int:
            return function(object, other)
        elif type(other) == str:
            num_dict = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
            if other in num_dict:
                return function(object, num_dict[other])
            elif other not in num_dict:
                raise Exception('TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.')
        else:
            return function(object, None)
    return sum_on_str


class Int(int):
    def __init__(self, arg):
        self.arg = arg

    @decorator
    def __add__(self, other):
        return super().__add__(other)



x = Int(5)
# print(x + '5')
# print(x + 'один')
# print(x + 'пять')
# print(x + 'шесть')
# print(x + 'a')
print(x + (1,))