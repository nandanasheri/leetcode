# https://leetcode.com/problems/daily-temperatures/description/
# o(n)
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        output = [0] * len(temperatures)
        stack = []

        for i in range(0, len(temperatures)):
            temp = temperatures[i]
            while len(stack) > 0 and stack[-1][0] < temp:
                top = stack.pop()
                ind = top[1]
                output[ind] = i - ind
            stack.append((temp, i))
        return output