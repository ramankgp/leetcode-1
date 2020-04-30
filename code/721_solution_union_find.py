class UnionFind(object):
    def __init__(self, n):
        self.ids = list(range(n))
        
    def find(self, i):
        while i != self.ids[i]:
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]
        return i
    
    def union(self, p, q):
        p, q = self.find(p), self.find(q)
        self.ids[p] = self.ids[q]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # email to name mapping
        email_to_name = dict()
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
        
        # get email to int id mapping
        email_to_ids = {email: idx for idx, email in enumerate(email_to_name.keys())}
        n = len(email_to_ids)
        
        # union the nodes
        uf = UnionFind(n)
        for account in accounts:
            for email in account[2:]:
                uf.union(email_to_ids[account[1]], email_to_ids[email])
        
        # gather the connected components
        clusters = defaultdict(list)
        for email in email_to_name:
            clusters[uf.find(email_to_ids[email])].append(email)
        
        # construct merged accounts
        result = []
        for emails in clusters.values():
            result.append([email_to_name[emails[0]]] + sorted(emails))
            
        return result
