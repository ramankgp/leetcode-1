class LRUCache {
private:
    int _capacity;
    list<pair<int, int>> l;
    unordered_map<int, list<pair<int, int>>::iterator> m;
public:
    LRUCache(int capacity) { _capacity = capacity; }
    
    int get(int key) {
        if (not m.count(key)) return -1;
        l.splice(--l.end(), l, m[key]);
        return m[key]->second;
    }
    
    void put(int key, int value) {
        if (l.size() == _capacity and not m.count(key)) {
            m.erase(l.front().first);
            l.pop_front();            
        }
        if (m.count(key)) l.erase(m[key]);
        l.push_back({key, value});
        m[key] = --l.end();
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */