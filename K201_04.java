import java.math.BigDecimal;

public class K201_04 {
    public static void main(String args[]) {
        BigDecimal a = new BigDecimal("1.1");
        BigDecimal b = a.multiply(a).multiply(a) ;

        BigDecimal c = a.add(a).add(a) ;
        System.out.println(c);
        System.out.println(b);
    }
}
