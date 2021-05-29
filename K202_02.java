public class K202_02 {
    public static void main(String args[]) {
        int banana = 100;
        int peach = 300;
        int  total_price = (banana*25)+(peach * 25);
        System.out.println(banana + "円のバナナを25個、" + peach + "円の桃を25個買ったら、合計:" + String.format("%,d", total_price) + "円になりました。");
    }
}
