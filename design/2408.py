'''
dict {one : 2, two: 3, three: 1}
values {two : {1: [first, second, third]}}
'''
class SQL:

    def __init__(self, names: list[str], columns: list[int]):
        self.tables = {}
        self.maxIds = {}
        for i in range(len(names)):
            self.tables[names[i]] = columns[i]
            self.maxIds[names[i]] = 0
        self.values = {}
        

    def ins(self, name: str, row: list[str]) -> bool:
        # print(name, row, self.values)
        if name not in self.tables or self.tables[name] != len(row):
            return False
        if name not in self.values:
            self.values[name] = {}
        self.values[name][self.maxIds[name]+1] = row
        self.maxIds[name] += 1
        return True
        

    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.values or rowId  not in self.values[name]:
            return
        self.values[name].pop(rowId)
        

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables or name not in self.values or rowId not in self.values[name] or columnId > self.tables[name]:
            return "<null>"
        return self.values[name][rowId][columnId-1]

    def exp(self, name: str) -> list[str]:
        if name not in self.values:
            return []
        final = []
        for rowId in self.values[name]:
            result = [str(rowId)]
            for val in self.values[name][rowId]:
                result.append(val)
            result = ",".join(result)
            final.append(result)
        return final


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)