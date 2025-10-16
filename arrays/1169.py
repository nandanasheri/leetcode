class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trans = defaultdict(list)
        invalid = [False] * len(transactions) 

        # build map and check for amount exceeding 1000
        for i,each in enumerate(transactions):
            items = each.split(",")
            trans[items[0]].append([i, items[0], items[1], items[2], items[3], each])
            if int(items[2]) > 1000:
                invalid[i] = True
        
        for name in trans:
            translist = trans[name]
            for i in range(len(translist)):
                for j in range(i+1, len(translist)):
                    if abs(int(translist[i][2]) - int(translist[j][2])) <= 60 and translist[i][4] != translist[j][4]:
                        # print(translist[i], translist[j])
                        invalid[translist[i][0]] = True
                        invalid[translist[j][0]] = True

        # print(invalid)
        res = []
        for i in range(len(invalid)):
            if invalid[i]:
                res.append(transactions[i])
        return res
            
        
        
        

            

