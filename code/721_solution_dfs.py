class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # build adj_lists  # O(\Sigma{a_i})
        email_to_name = dict()
        adj_lists = collections.defaultdict(set)
        for acc in accounts:
            for email in acc[1:]:
                adj_lists[acc[1]].add(email)
                adj_lists[email].add(acc[1])
                email_to_name[email] = acc[0]
        
        # dfs to gather connected components  O(\Sigma{a_ilog_{a_i}})
        visited = set()
        result = []
        for email in adj_lists:
            if email in visited: continue
            visited.add(email)
            stack = [email]
            emails = []
            while stack:
                email = stack.pop()
                emails.append(email)
                for alt_email in adj_lists[email]:
                    if alt_email in visited: continue
                    visited.add(alt_email)
                    stack.append(alt_email)
            result.append([email_to_name[email]] + sorted(emails))
            
        return result
            
        