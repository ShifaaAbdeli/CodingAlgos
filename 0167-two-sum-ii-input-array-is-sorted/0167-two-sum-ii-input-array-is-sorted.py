class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Use two pointers approch
        l = 0
        f = len(numbers) - 1
        while l < f:
            sum = numbers[l] + numbers[f]
            if sum == target:
                return [l+1, f+1]
            elif sum > target:
                # shift right
                f -=  1
            else:
                # shift left
                l += 1
            


        