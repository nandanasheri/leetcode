class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort()
        stack = []
        
        for i in range(len(cars)-1, -1, -1):
            pos, speed = cars[i]
            t = (target - pos) / speed
            if stack:
                time = stack[-1][2]
                if t > time:
                    stack.append((pos, speed, t))
            else:
                stack.append((pos, speed, t))
        
        return len(stack)