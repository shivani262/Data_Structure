def balanced(exp):
    stack=[]
    for char in exp:
        if char in ["(","{","["]:
            stack.append(exp)
        else:
            if not stack:
                return False
            current_char=stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
                else:
                    return True
            if current_char == '{':
                if char != "}":
                    return False
                else:
                    return True
            if current_char == '[':
                if char != "]":
                    return False
                else:
                    return True

    if stack:
        return False
    return True
if __name__ == "__main__" :  
    exp="{[(()]}"
    if balanced(exp):
       print("balanced")
    else:
        print("not balanced")
