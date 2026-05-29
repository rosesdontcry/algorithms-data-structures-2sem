class Node:
    def __init__(self, data, previous_node = None):
        self.data = data
        self.previous_node = previous_node


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if not self.is_empty():
            _return = self.top.data
            self.top = self.top.previous_node
            return _return
        else:
            raise IndexError("stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            raise IndexError("stack is empty")


def main():
    stack = Stack()
    flag = True
    opening_parenthesis = '('
    closing_parenthesis = ')'

    for i in input():
        if i in opening_parenthesis:
            stack.push(i)
        elif i in closing_parenthesis:
            if stack.is_empty():
                flag = False
                break
            else:
                stack.pop()
        else:
            flag = False
            break


    if flag and stack.is_empty():
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

