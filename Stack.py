

class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if self.stack:
            return False
        else:
            return True

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        last = self.stack[-1]
        del(self.stack[-1])
        return last

    def peek(self):
        last = self.stack[-1]
        return last

    def size(self):
        return len(self.stack)


my_st = '[{}'
open_list = ['(', '{', '[']
close_list = [')', '}', ']']
stack = Stack()


def is_balance(my_str):
    for i in my_str:
        if i in open_list:
            stack.push(i)
        elif i in close_list:
            i_ind = close_list.index(i)
            if (stack.size() > 0) and (open_list[i_ind] == stack.stack[-1]):
                stack.pop()
            else:
                return 'Несбалансированно!!!'
    if stack.size() == 0:
        return 'Сбалансированно!'
    else:
        return 'Несбалансированно!!!'


print(is_balance(my_st))


