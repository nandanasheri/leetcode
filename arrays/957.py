class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        cell_combs = set()
        # do we have so many number of days where we reach a cycle?
        isCycle = False
        currCells = cells
        for i in range(n):
            next_state = ['0'] * 8
            for j in range(1,7):
                if currCells[j-1] == currCells[j+1]:
                    next_state[j] = "1"
            str_state = "".join(next_state)
            # when you hit a cycle, you stop iterating
            if str_state in cell_combs:
                isCycle = True
                break
            cell_combs.add(str_state)
            currCells = next_state
        
        result = []
        if isCycle:
            ind = n % len(cell_combs)
            # we simulate it again but now just to get to our desired state in our repeated loop
            for i in range(ind):
                next_state = ['0'] * 8
                for j in range(1,7):
                    if currCells[j-1] == currCells[j+1]:
                        next_state[j] = "1"
                str_state = "".join(next_state)
                currCells = next_state
        
        result = currCells
        for i in range(len(result)):
            result[i] = int(result[i])
        
        return result


            