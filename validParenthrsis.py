def validParenthesis(str):
    stack = []
    for i in range(len(str)):
        if str[i] in "{([":
            stack.append(str[i])
        else:
            if len(stack)==0:   
                 return False
            if str[i] == ")" and stack[-1]=="(":
                stack.pop()
            if str[i] == "}" and stack[-1]=="{":
                stack.pop()
            if str[i] == "]" and stack[-1]=="[":
                stack.pop()

    if len(stack)==0:
            return True
    return False
    
print(validParenthesis("{{()}}())"))
 