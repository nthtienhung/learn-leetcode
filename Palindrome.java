public class Palindrome {
    public static void main(String args[]) {
        String s = "A man, a plan, a canal: Panamas";
        boolean check = isPalindrome(s);
        System.out.println(check);
    }
    public static boolean isPalindrome(String s) {
        s = s.toLowerCase();
        s = s.replaceAll("\\s+","");
        s= s.replaceAll("[^a-zA-Z0-9]", "");
        
        String reverse = "";
        for(int i = s.length() - 1; i >= 0; i--) {
            reverse += s.charAt(i);
        }
        if(s.equals(reverse)){
            return true;
        }
        return false;
    }
}