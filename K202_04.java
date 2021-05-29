import java.util.Scanner;
public class K202_04 {
    public static void main(String args[]) {
        System.out.println("あなたの名前を入力してください。");
        Scanner scanner = new Scanner(System.in);
        System.out.print("Input > ");

        String input = scanner.nextLine();
        System.out.println(input + "さん、こんにちは。");
        System.out.println("あなたは何歳ですか？");

        String age = scanner.nextLine();
        System.out.println(age + "歳なんですね。よろしくお願いします。");
        scanner.close();
    }
}
