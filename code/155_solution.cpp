class MinStack {
private:
    stack<int> vals;
    // stack<int> mins;
    stack<tuple<int, int>> mins;
public:
    /** initialize your data structure here. */
    MinStack() {
        vals = {};
        mins = {};
    }
    
    void push(int x) {
        vals.push(x);
        // mins.push(mins.empty() ? x : min(x, getMin()));
        // if (mins.empty() or x <= getMin()) mins.push(x);
        if (mins.empty() or x < getMin()) mins.push({x, 1});
        else if (x == getMin()) get<1>(mins.top())++;
    }
    
    void pop() {
        // if (vals.top() == getMin()) mins.pop();
        if (vals.top() == getMin()) {
            if (get<1>(mins.top()) == 1) mins.pop();
            else get<1>(mins.top())--;
        }
        vals.pop();
        // mins.pop();
    }
    
    int top() { return vals.top(); }
    
    int getMin() { return get<0>(mins.top()); }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */