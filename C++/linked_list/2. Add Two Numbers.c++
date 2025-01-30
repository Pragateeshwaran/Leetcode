#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(NULL) {}
    ListNode(int x) : val(x), next(NULL) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    // Function to reverse a linked list (if needed)
    ListNode* reverse(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* curr = head;
        while (curr) {
            ListNode* nextNode = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextNode;
        }
        return prev;
    }

    // Function to add two numbers represented as linked lists
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int remainder = 0;
        ListNode* res = new ListNode(); // Dummy node to simplify handling
        ListNode* tempi = res;

        // Traverse both lists
        while (l1 || l2 || remainder) {
            int val1 = (l1) ? l1->val : 0;
            int val2 = (l2) ? l2->val : 0;
            int temp = val1 + val2 + remainder;

            // Create new node for the current digit
            tempi->next = new ListNode(temp % 10);
            tempi = tempi->next;

            // Update remainder
            remainder = temp / 10;

            // Move to the next nodes
            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }

        return reverse(res->next); // Return the head of the resulting list
    }
};

int main() {
    // Example usage
    ListNode* l1 = new ListNode(2, new ListNode(4, new ListNode(3))); // 342
    ListNode* l2 = new ListNode(5, new ListNode(6, new ListNode(4))); // 465

    Solution sol;
    ListNode* result = sol.addTwoNumbers(l1, l2);

    // Print the result
    while (result) {
        cout << result->val;
        if (result->next) cout << " -> ";
        result = result->next;
    }
    cout << endl;

    return 0;
}

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
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* Res = new ListNode();
        ListNode* curr = Res;
        int carry = 0;
        while(l1||l2||carry){
            cout<<curr->val<<endl;
            int val1 = l1 !=nullptr ? l1->val: 0 ;
            int val2 = l2 !=nullptr ? l2->val: 0 ;
            int total = val1 + val2 + carry;
            int lastDigit = total%10;
            carry = total/10;
            curr->next = new ListNode(lastDigit);
            curr = curr->next;
            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }
        return Res->next;
    }
};