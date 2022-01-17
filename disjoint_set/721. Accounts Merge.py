# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:        
        def findRoot(email):
            while parent[email]!=email:
                email = parent[email]
            return email
            
        def union(e1, e2):
            r1,r2 = findRoot(e1), findRoot(e2)
            if height[r1]==height[r2]:
                parent[r2]=r1
                height[r1]+=1
            elif height[r1]>height[r2]:
                parent[r2]=r1
            else:
                parent[r1]=r2
        
        height = {}
        parent = {}
        owner = {}
        for account in accounts:
            for email in account[1:]:
                height[email]=0
                parent[email]=email
                owner[email]=account[0]
        
        for account in accounts:
            for e1,e2 in zip(account[1:], account[2:]):
                union(e1,e2)
                
        register = defaultdict(list)
        for account in accounts:
            for email in account[1:]:
                root = findRoot(email)
                if email not in register[root]:
                    register[root].append(email)
                
        ans = []
        for root in register:
            register[root].sort()
            ans.append([owner[root]]+register[root])
        return ans
