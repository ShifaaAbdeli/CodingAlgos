class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arrStack = []

        for oper in operations:
            if oper == "C":
                arrStack.pop()
            elif oper == "D":
                arrStack.append(arrStack[-1] * 2)
            elif oper == "+":
                arrStack.append(arrStack[-1] + arrStack[-2])
            else:
                arrStack.append(int(oper))

        return sum(arrStack)

        # time complexity O(n), space complexity O(n)

