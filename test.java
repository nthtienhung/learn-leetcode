import java.util.Stack;

public class test {
    public static void main(String[] args) {
        String a = "asd";
        String b = "awe";

        Character charA = a.charAt(1);
        System.out.println(charA.equals('b'));
        System.out.println(a.replace('s','\0' ));

        //stack
        Stack<String> stack = new Stack<String>();
        System.out.println("is stack empty: " + stack.empty());
        stack.push("call of duty");
        stack.push("elden ring");
        stack.push("battlefront");
        System.out.println("is stack empty: " + stack.empty());
        System.out.println(stack);
        // stack.pop();
        // stack.pop();
        // stack.pop(); //cause error
        System.out.println("top of stack: " + stack.peek()); 
        System.out.println("search for battlefront: " + stack.search("battlefront"));
        System.out.println(stack);
    }
}
