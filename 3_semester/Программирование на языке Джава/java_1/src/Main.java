import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final double ROUBLES_PER_YUAN = 11.91;
        int yuan, digit;
        double roubles;

        Scanner input = new Scanner(System.in);

        System.out.print("Введите колличество юаней: ");
        yuan = input.nextInt();

        roubles = ROUBLES_PER_YUAN * yuan;
        digit = yuan % 10;

        if (yuan % 100 >= 11 && yuan % 100 <= 14) {
            System.out.print(yuan + " китайских юаней это " + roubles + " рублей");
        }
        else if (digit == 1) {
            System.out.print(yuan + " китайский юань это " + roubles + " рублей");
        }
        else if (digit >= 2 && digit <= 4) {
            System.out.print(yuan + " китайских юаня это " + roubles + " рублей");
        }
        else {
            System.out.print(yuan + " китайских юаней это " + roubles + " рублей");
        }
    }
}