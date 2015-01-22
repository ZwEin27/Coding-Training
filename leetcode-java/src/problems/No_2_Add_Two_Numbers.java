package problems;

/**
 * https://oj.leetcode.com/problems/add-two-numbers/
 */

//Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}


public class No_2_Add_Two_Numbers {

	public static void main(String[] args) {
		No_2_Add_Two_Numbers no2 = new No_2_Add_Two_Numbers();
		ListNode l1 = new ListNode(5);
		
		ListNode l2 = new ListNode(5);
		
		ListNode rln = no2.addTwoNumbers(l1, l2);
		while (rln!=null){
			System.out.println(rln.val);
			rln = rln.next;
		}
		
		
	}

	 public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		 ListNode returnLN = null;
		 ListNode curRLN = null;
		 int ao = 0;
		 while(l1!=null||l2!=null||ao==1){
			 int v1 = l1!=null?l1.val:0;
			 int v2 = l2!=null?l2.val:0;
			 int sum = v1 + v2 + ao;
			 		 
			 if (returnLN==null) {
				 returnLN = new ListNode(sum%10);
				 curRLN = returnLN;
			 } else {
				 curRLN.next = new ListNode(sum%10);
				 curRLN = curRLN.next;
			 }
			 
			 l1 = l1!=null?l1.next:null;
			 l2 = l2!=null?l2.next:null;
			 
			 if (sum>=10){
				 ao = 1;
			 } else {
				 ao = 0;
			 }
		 }
		return returnLN;
	 }
	
}
