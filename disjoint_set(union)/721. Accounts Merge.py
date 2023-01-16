class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:        
        def find(acc):
            if root[acc] == acc:
                return acc
            root[acc] = find(root[acc])
            return root[acc]     
        
        def union(acc1, acc2):
            r1, r2 = find(acc1), find(acc2)            
            if r1!=r2:
                root[r2] = r1                
        
        #account owner
        names = {}
        for account in accounts:
            for email in account[1:]:
                names[email] = account[0]
        root = {name:name for name in names}
        
        #find unions
        for account in accounts:
            for e1, e2 in zip(account[1:], account[2:]):
                union(e1, e2)
        
        #register accounts in root account
        reg = defaultdict(list)
        for email in names:
            r = find(email)
            reg[r].append(email)
        
        return [[names[acc]] + sorted(reg[acc]) for acc in reg]
