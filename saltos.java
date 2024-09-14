public class saltos{

    public static int R(int n){
        if(n == 0) return 1;
        if(n == 1) return 1;
        if(n == 2) return 2;
        
        if(n >= 6) return R(n-1) + R(n-2) + R(n-3) - R(n-6);

        return R(n-1) + R(n-2) + R(n-3);

    }

    public static void printR(int n){
        System.out.println(R(n));
    }

    public static void main(String[] args) {
        
        String in = args[0];

        int n = Integer.valueOf(in);

        R(n);
        printR(n);
        
    }
}