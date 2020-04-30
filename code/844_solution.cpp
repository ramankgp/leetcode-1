class Solution {
public:
    int getNext(string S, int loc){
        for (int skip=0;loc>=0;loc--){
            if (S[loc] == '#') skip++;
            else if (skip) skip--;
            else return loc;
        }
        return -1;
    }
    
    bool backspaceCompare(string S, string T) {
        int s,t;
        for (s=S.size()-1,t=T.size()-1;s*t>=0;s--,t--){
            s = getNext(S, s);
            t = getNext(T, t);
            if (s < 0 and t < 0) return true;
            if (s < 0 or t < 0) return false;
            if (S[s] != T[t]) return false;
        }
        return getNext(S, s) == getNext(T, t);
    }
};