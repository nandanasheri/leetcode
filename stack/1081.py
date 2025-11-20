class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq_map = defaultdict(int)
        seen = {}
        stack = []

        for i in s:
            freq_map[i] += 1
            seen[i] = False

        for i in range(0,len(s)):
            freq_map[s[i]] -= 1
            if seen[s[i]]:
                continue
            while stack and stack[-1] > s[i] and freq_map[stack[-1]] > 0:
                top = stack.pop()
                seen[top] = False
            stack.append(s[i])
            seen[s[i]] = True

        return "".join(stack)



        