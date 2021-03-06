package problems;

import java.util.ArrayList;
import java.util.Dictionary;
import java.util.HashMap;
import java.util.List;
import java.util.Stack;

/**
 *	https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/
 */

public class No_3_Longest_Substring_Without_Repeating_Characters {

	public static void main(String[] args) {
		No_3_Longest_Substring_Without_Repeating_Characters no3 = new No_3_Longest_Substring_Without_Repeating_Characters();
		System.out.println("result is " + no3.lengthOfLongestSubstring("wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"));;
	}

	
	// HashMap中用一个get代替contain函数
	public int lengthOfLongestSubstring(String s) {
		int result = 0;
		int counter = 0;
		HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
		for (int i=0;i<s.length();i++) {
			char c = s.charAt(i);
			Integer idx = hm.get(c);
			if(idx!=null&&idx>=0){
				counter = 0;
				i = idx+1;
				hm.clear();	// 这里有问题，应该保留
			} else {
				counter++;
				hm.put(c, i);
			}
			if (counter>result){
				result = counter;
			}
		}
		return result;
    }
	
	 // Time Limit Exceeded
	 public int VersionOne(String s) {
			int result = 0;
			int counter = 0;
			ArrayList<Character> list = new ArrayList<Character>();
			char[] ch = s.toCharArray();
			for (int i=0;i<s.length();i++) {
				if(!list.contains(ch[i])){
					list.add(ch[i]);
					counter++;
				}else {
					if (counter>result){
						result = counter;
					}
					counter = 1;
					list.clear();
				}
			}
			return result;
	   }
	 
	 // Time Limit Exceeded 
	 public int VersionTwo(String s) {
			int result = 0;
			int counter = 0;
			char[] ch = s.toCharArray();
			HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
			for (int i=0;i<s.length();i++) {
				
				if(!hm.containsKey(ch[i])){
					counter++;
				}else {
					counter = 1;
					i = hm.get(ch[i])+1;
					hm.clear();
				}
				hm.put(ch[i], i);
				if (counter>result){
					result = counter;
				}
			}
			return result;
	    }
}

/**
 * wlrb
 * bmq
 * bhcdarzowk
 * kyhid
 * dqsc
 * dxrjmowf
 * rxsjybld
 * befsarc
 * bynecd
 * yg
 * gx
 * xpklore
 * l
 * lnmpa
 * pqfwkho
 * pkmco
 */


/*	wlrb
 * 	bmq
 * 	bhcdarzowk
 * 	kyhid
 * 	dqsc
 * 	dxrjmowfr
 * 	xsjybldbef
 * 	sarcbynecdyg
 * 	gx
 * 	xpklore
 * 	l
 * 	lnmpa
 * 	pqfwkho
 * 	pkmco
 * 
 */



