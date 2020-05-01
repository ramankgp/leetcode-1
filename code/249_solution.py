# "acef" -> "bdfg" -> ""      
#  0245  ->  1356     2467    25,1,3,4
#            0245     0245    0 -24, -22, -21 % 26
#                             0,2,4,5
 
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def hash(s):
            return tuple([(ord(c) - ord(s[0])) % 26 for c in s])
        groupby = collections.defaultdict(list)
        for s in strings:
            groupby[hash(s)].append(s)
        return groupby.values()
        