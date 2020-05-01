// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int l=1, h=n, m;
        while (l<h){
            m = (h-l) / 2 + l;
            if (isBadVersion(m)) h = m;
            else l = m + 1;
        }
        return l;
    }
};