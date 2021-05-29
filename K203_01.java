public class K203_01 {
    public static void main(String args[]) {
        int i = 0;
        int mod;
        while (i < 101){
            mod = i % 7;
            if (mod == 0){
                System.out.println(i);
            }
            i += 1;
        }
    }
}
