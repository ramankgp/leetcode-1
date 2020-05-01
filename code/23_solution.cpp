/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
private:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode ret(0);
        ListNode* trav = &ret;
        while (l1 and l2){
            if (l1->val < l2->val) {
                trav->next = l1;
                l1 = l1->next;
            } else {
                trav->next = l2;
                l2 = l2->next;                
            }
            trav = trav->next;
        }
        trav->next = l1 ? l1 : l2;
        return ret.next;
    }
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        queue<ListNode*> q;
        for (auto node:lists) q.push(node);
        while (q.size() > 1) {
            ListNode* l1 = q.front(); q.pop();
            ListNode* l2 = q.front(); q.pop();
            ListNode* l3 = mergeTwoLists(l1, l2);
            q.push(l3);
        }
        return q.empty() ? nullptr: q.front();
    }
};
