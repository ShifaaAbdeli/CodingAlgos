class Solution:
    def isValid(self, s: str) -> bool:

        #def is_match(p, q):
        #    if p == "(" and q == ")":
        #        return True
        #    if p == "[" and q == "]":
        #        return True
        #    if p == "{" and q == "}":
        #        return True
        #    else:
        #        return False
        # Using stack to approach this problem
        #st = []
        #is_balanced = True
        #idx = 0

        #while idx < len(s) and is_balanced:
        #    parent = s[idx]
        #    if parent in "([{":
        #        st.append(parent)
        #    else:
        #        if len(st) == 0:
        #            is_balanced = False
        #            break
        #        else:
        #            ele = st.pop()
        #            if not is_match(ele, parent):
        #                is_balanced = False
        #                break
        #    idx += 1
        #if len(st) == 0 and is_balanced:
        #    return True
        #else:
        #    return False

        ##Second approach with stack and is_match function
        #def is_match(p, q):
        #    if p == ")" and q == "(":
        #        return True
        #    elif p == "]" and q == "[":
        #        return True
        #    elif p == "}" and q == "{":
        #        return True
        #    else:
        #        return False

        #stPar = []
        #is_balanced = True
        #idx = 0

        #for idx in range(len(s)):
        #    if s[idx] in "([{":
        #        stPar.append(s[idx])
        #    else:
        #        if len(stPar) == 0:
        #            is_balanced = False
        #            break
        #        else:
        #            q = stPar.pop()
        #            if not is_match(s[idx], q):
        #                is_balanced = False
        #                break
        #if len(stPar) == 0 and is_balanced:
        #    return True
        #else:
        #    return False


        ## 3rd approach with hashMap and Stack
        stackArr = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for par in s:
            if par in closeToOpen:
                if stackArr and stackArr[-1] == closeToOpen[par]:
                    stackArr.pop()
                else:
                    return False
            else:
                stackArr.append(par)

        return True if not stackArr else False




