/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode p = head;
        int n = 0;
        while(p!= null){
            n += 1;
            p = p.next;
        }
        n = n / 2;
        while(n - 1 >= 0){
            head = head.next;
            n -= 1;
        }
        return head;
    }
}