#include<iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* dummy = new ListNode();
    ListNode* curr = dummy;

    ListNode* recursion(ListNode* head){
        if (!head) return nullptr;

        ListNode *i = head;
        ListNode *j = head->next;

        if (!j) {
            curr->next = new ListNode(i->val);  
            return curr;
        }

        ListNode* i_node = new ListNode(i->val);
        ListNode* j_node = new ListNode(j->val);

        j_node->next = i_node;
        curr->next = j_node;
        curr = i_node;

        recursion(j->next);  

        return curr;
    }

    ListNode* swapPairs(ListNode* head) {
        recursion(head);
        return dummy->next;
    }
};

int main(){
    ListNode* head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
    Solution soln;
    ListNode* result = soln.swapPairs(head);

    cout << "Swapped pairs: ";
    while (result) {
        cout << result->val << " ";
        result = result->next;
    }
    cout << endl;

    return 0;
}
