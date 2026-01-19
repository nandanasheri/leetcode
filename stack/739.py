class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = deque()

        if len(temperatures):
            stack.append((temperatures[0],0))

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                # print(stack)
                temp, ind = stack.pop()
                res[ind] = i - ind
                # print(res)
            stack.append((temperatures[i], i))
        return res