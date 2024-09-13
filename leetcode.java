public class leetcode {

    //palindrome number(turn to string)
    public boolean isPalindromeStr(int x) {
        if (x < 0)  return false;

        String str = Integer.toString(x);
        for(int i = 0; i < str.length() / 2; i++) {
            if(str.charAt(i) != str.charAt(str.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }
    //palindrome number(keep int format)
    public boolean isPalindromeInt(int x) {
        if (x < 0 || (x != 0 && x % 10 == 0) ) {
            return false;
        }
        int num = x;
        int y = 0;
        
        //reverse the number
        while (num != 0) {
            int rem = num % 10;
            num = num / 10;
            y = y * 10 + rem;
        }
        return y == x;
    }

    //reverse number
    public static int reverseNumber(int x) {
        String str = Integer.toString(x);
        String reverseStr = "";
        int output;
        for(int i = str.length() - 1; i >= 0; i--) {
            if(Character.compare(str.charAt(i),'-') == 0){
                continue;
            }
            reverseStr += str.charAt(i);
        }
        output = Integer.parseInt(reverseStr);
        if (output > Integer.MAX_VALUE) return 0;
        if(x < 0) output *= -1;
        return output;
    }
    //Minimum Add to Make Parentheses Valid
    public static int minAddToMakeValid(String s) {
        int leftParentheses = 0;
        int rightParentheses = 0;
        for(int i = 0; i < s.length(); i++){
            if (s.charAt(i) == '(') {
                leftParentheses += 1;
            }else if (s.charAt(i) == ')') {
                rightParentheses += 1;
            }
        }
        return Math.abs(leftParentheses - rightParentheses);
    }


    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;

        while(start < end) {
            int mid = start + (end - start) / 2;
            //int mid = (start + end) / 2 //this also works, but can have overflow error??
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        if (nums[start] == target) {
            return start;
        }
        return -1;
    }

    //odd even linked list
    public ListNode OddEvenLinkedList(ListNode head) {
        if (head == null) return null;
        ListNode odd = head;
        ListNode even = head.next;
        ListNode tmp = even;
        
        while (even != null && even.next != null) {
            odd.next = even.next;
            odd = odd.next;
            even.next = odd.next;
            even = even.next;
        }
        odd.next = tmp;
        return head;
    }

    //first bad version
    // public int firstBadVersion(int n) {
    //     int start = 1;
    //     int end = n;

    //     while (start < end) {
    //         int mid = start + (end - start) / 2;
    //         if(isBadVersion(mid)) {
    //             end = mid;
    //         } else {
    //             start = mid + 1;
    //         }
    //     }
    //     if (isBadVersion(start)) return start;
    //     return -1;
    // }
    public boolean backspaceCompare(String s, String t) {

        for(int i = 0; i < s.length(); i++) {
            Character currentCharS = s.charAt(i);
            Character currentCharT = t.charAt(i);
            if(currentCharS.equals('#')) {
                s = s.replace(s.charAt(i - 1), '\0');
            }else if (currentCharT.equals('#')) {
                t = t.replace(t.charAt(i - 1),'\0');
            }else {
                continue;
            }

        }
        if (s.equals(t)) return true;
        return false;

    }
    //number of islands
    public int numberIslands(char[][] grid) {
        if(grid.length == 0 || grid[0].length == 0) return 0;
        int count = 0;
        for (int r = 0; r < grid.length; r++) {
            for(int c = 0; c < grid[0].length; c++) {
                if(grid[r][c] == '1') {
                    count++;
                    helper(grid,r,c);
                }
            }
        }
        return count;
    }
    public void helper(char[][] grid, int r, int c) {
        if(r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] == '0') return;
        grid[r][c] = '0';
        helper(grid, r+1, c);
        helper(grid, r-1, c);
        helper(grid, r, c+1);
        helper(grid, r, c-1);
    }

    public boolean hasCycle(ListNode head) {
        if(head == null) return false;

        ListNode slow = head;
        ListNode fast = head.next;

        while(fast != null && fast.next != null) {
            if(fast == slow) return true;
            slow = slow.next;
            fast = fast.next.next;
        }
        return false;
    }
    //nested list weight sum
    public int depthSum(List<NestedInteger> nestedList) {
        int sum = 0;
        int lv = 1;

        while(nestedList.size() != 0) {
            List<NestedInteger> tmp = new LinkedList<>();
            for (NestedInteger e: nestedList) {
                if(e.isInteger()) {
                    sum += e.getInteger() * lv;
                } else {
                    tmp.addAll(e.getList());
                }
                lv++;
                nestedList = tmp;
            }
            return sum;
        }
    }
    //reverse string
    public void reverseString(char[] s) {
        int start = 0;
        int end = s.length - 1;

        while (start < end) {
            char tmp = s[start];
            s[start] = s[end];
            s[end] = tmp;
            start++;
            end--;
        }
    }
    public static void main(String[] args) {
        System.out.println(minAddToMakeValid("()"));
    }
}
//invert binary tree
public TreeNode invertTree(TreeNode root) {
    if (root == null) {
        return null;
    }

    // Swap the children
    TreeNode tmp = root.left;
    root.left = root.right;
    root.right = tmp;

    invertTree(root.left);
    invertTree(root.right);
    return root;
}
//happy number
class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> visit = new HashSet<Integer>();
        
        while (!visit.contains(n)) {
            visit.add(n);
            n = sumOfSquares(n);
            
            if (n == 1) {
                return true;
            }
        }
        return false;
    }
    public int sumOfSquares(int n) {
        int output = 0;
        while (n != 0) {
            int digit = n % 10;
            digit = (int)Math.pow(digit, 2);
            output += digit;
            n = n / 10;
        }
        return output;
    }
}