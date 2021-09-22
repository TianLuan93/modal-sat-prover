def shunting_yard(string):
    current_token = ''

    output_queue = []
    stack = []

    it = iter(range(0, len(string)))
    for i in it:
        ch = string[i]
        operator_char = (ch in ["-", "&", "|", "^", ">", " ", "(", ")", "[", "]", "<", "*"])

        if current_token and operator_char:
            output_queue.append(current_token)
            current_token = ''

        elif current_token and i == len(string) - 1:


            if not operator_char:
                current_token += ch

            output_queue.append(current_token)
            current_token = ''

        if ch in ["-", "&", "|", "^", '>', '<', '[', ']', '*']:

            # don't let unary '-' operator pop a binary operator from the stack
            # give parens a high precedence
            if stack and ch != "-" and stack[-1] != '(' and ch != "[" and ch != "<":
                output_queue.append(stack.pop())

                if output_queue[-1] == "-" and stack and stack[-1] != '(':
                    output_queue.append(stack.pop())
                if output_queue[-1] == "[]" and stack and stack[-1] != '(':
                    output_queue.append(stack.pop())
                if output_queue[-1] == "<>" and stack and stack[-1] != '(':
                    output_queue.append(stack.pop())

            if ch == ">" and string[i + 1] != ">" and string[i - 1] != ">":
                print("Error: single '>' is not allowed")
                return
            if ch == "<" and string[i + 1] != ">":
                print("Error: single '<' is not allowed")
                return
            if ch == "[" and string[i + 1] != "]":
                print("Error: single '[' is not allowed")
                return

            if ch == ">" and string[i + 1] == ">":
                stack.append(">>")
                next(it)
            elif ch == "<" and string[i + 1] == ">":
                stack.append("<>")
                next(it)
            elif ch == "[" and string[i + 1] == "]":
                stack.append("[]")
                next(it)
            elif ch == "*":
                stack.append("<->")
            else:
                stack.append(ch)

        if ch == "(":
            stack.append("(")

        if ch == ")":
            while True:
                next_operator = stack.pop()
                if next_operator == "(":
                    break
                output_queue.append(next_operator)

        if ch not in ["-", "&", "|", "^", '>', "(", ")", " ", "<", "[", "]", "*"]:
            current_token += ch

    while stack:
        output_queue.append(stack.pop())

    return output_queue
