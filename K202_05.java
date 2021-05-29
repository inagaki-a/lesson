public class K202_05 {
    public static void main(String args[]) {
        String a = "1234567890\n1234567890";
        System.out.println(a);
        a = a.replace("\n", ""); 
        System.out.println(a.length());
    }
}
