all_ops = {}

def binary_op(token):
    def make_binop(func):
        def redef(stack):
            if len(stack) < 2:
                raise ValueError

            b = stack.pop()
            a = stack.pop()
            result = func(a, b)

            stack.append(result)

            return result

        all_ops[token] = redef
        return redef
    return make_binop


@binary_op('+')
def add(a, b):
    return a + b


@binary_op('-')
def sub(a, b):
    return a - b


def calculate(exp: str) -> float:
    stack = []
    for token in exp.split():
       operation = all_ops.get(token, None)

       if operation is not None:
           operation(stack)
       else:
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError

    if len(stack) != 1:
        raise ValueError

    return stack.pop()

if __name__ == "__main__":
    print(all_ops)