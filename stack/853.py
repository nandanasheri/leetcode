# https://leetcode.com/problems/car-fleet/
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            arr.append((position[i], speed[i]))
        arr = sorted(arr)

        stack = []

        for p,s in arr[::-1]:
            time = (target-p) / s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)