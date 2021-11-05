qwerty = []


class Stack:
    def __init__(self, qwerty_):
        self.qwerty = qwerty_

    def isEmpty(self):
        if not self.size():
            return True
        else:
            return False

    def push(self, i):
        qwerty.append(i)

    def pop(self):
        if self.isEmpty():
            return 'Стек пустой'
        else:
            self.qwerty.pop()
            return self.qwerty[-1]

    def peek(self):
        if self.isEmpty():
            return 'Стек пустой'
        else:
            return self.qwerty[-1]

    def size(self):
        return len(self.qwerty)


def balance_test(list_for_test):
    random_list = []
    symbol_list = ['(', ')', '[', ']', '{', '}']
    symbol_dict = {'(': ')', '{': '}', '[': ']'}
    test_list = Stack(random_list)
    for i in list_for_test:
        if i in symbol_list:
            if test_list.isEmpty():
                test_list.push(i)
            else:
                if symbol_dict.get(test_list.peek()) == i:
                    test_list.pop()
                else:
                    test_list.push(i)
        else:
            print(f"Такого символа в списке не существует")

    if test_list.isEmpty():
        return 'Сбалансированн'
    else:
        return 'Несбалансированн'


def main():
    print(balance_test('()'))
    print(balance_test('(((([{}]))))'))
    print(balance_test('[([])((([[[]]])))]{()}'))
    print(balance_test('{{[()]}}'))
    print('--------------')
    print(balance_test('}{}'))
    print(balance_test('{{[(])]}}'))
    print(balance_test('[[{())}]'))


if __name__ == '__main__':
    main()
