"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def __init__(self):
        self.buf4 = [''] * 4
        self.curr_used = 0
        self.curr_read = 0
        self.EOF = False
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        num_read = 0
        while num_read < n and not self.EOF:
            if self.curr_used == self.curr_read:
                self.curr_read = read4(self.buf4)
                self.curr_used = 0
                if self.curr_read == 0: self.EOF = True
            else:
                delta = min(self.curr_read - self.curr_used, n-num_read)
                buf[num_read:num_read+delta] = self.buf4[self.curr_used:
                                                         self.curr_used+ delta]
                num_read += delta
                self.curr_used += delta
        return num_read
            
        