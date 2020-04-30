# call stack []
# time spent [2 + 1, 5]
# prev_start_time = 6

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ftimes = [0] * n
        stack = []  # the ids of function calls
        prev_start_time = 0
        
        for log in logs:
            fid, typ, ftime = log.split(':')
            fid, ftime = int(fid), int(ftime)
            
            if typ == 'start':
                if stack:
                    ftimes[stack[-1]] += ftime - prev_start_time
                stack.append(fid)
                prev_start_time = ftime
            else:
                ftimes[stack.pop()] += ftime - prev_start_time + 1
                prev_start_time = ftime + 1
                
        return ftimes
                 
            