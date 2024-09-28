import java.util.HashMap;
import java.util.Map;

public class saltos {

    // funcao com recursao simples
    public static int rec(String path, int pos, boolean lastJumpWasThree) {
        if (pos == path.length() - 1) {
            return 1;
        }

        if (pos >= path.length() || path.charAt(pos) == '0') {
            return 0;
        }

        int ways = 0;

        // pulo de 1m
        ways += rec(path, pos + 1, false);

        // pulo de 2m
        ways += rec(path, pos + 2, false);

        //pulo de 3m
        if (!lastJumpWasThree) {
            ways += rec(path, pos + 3, true);
        }

        return ways;
    }

    // funcao com recursao memorizada
    public static int recMemo(String path, int pos, boolean lastJumpWasThree, Map<String, Integer> memo) {
        if (memo == null) {
            memo = new HashMap<>();
        }

        String key = pos + "," + lastJumpWasThree;

        if (memo.containsKey(key)) {
            return memo.get(key);
        }

        if (pos == path.length() - 1) {
            return 1;
        }

        if (pos >= path.length() || path.charAt(pos) == '0') {
            return 0;
        }

        int ways = 0;

        // pulo de 1m
        ways += recMemo(path, pos + 1, false, memo);

        // pulo de 2m
        ways += recMemo(path, pos + 2, false, memo);

        // pulo de 3m
        if (!lastJumpWasThree) {
            ways += recMemo(path, pos + 3, true, memo);
        }

        memo.put(key, ways);

        return ways;
    }

    public static int nonRecursive(String path) {
        int n = path.length();
        if (n == 0 || path.charAt(0) != 'm' || path.charAt(n - 1) != 'm') {
            return 0;
        }

        int[][] matriz = new int[n][2];
        matriz[0][0] = 1;

        for (int i = 1; i < n; i++) {
            if (path.charAt(i) == '0') {
                continue;
            }
            // olha 1 metro atrás
            if (i - 1 >= 0) {
                matriz[i][0] += matriz[i-1][0] + matriz[i-1][1];
            }
            // olha 2 metro atrás
            if (i - 2 >= 0) {
                matriz[i][0] += matriz[i-2][0] + matriz[i-2][1];
            }
            // olha 3 metro atrás
            if (i - 3 >= 0) {
                matriz[i][1] += matriz[i-3][0];
            }
        }
        return matriz[n-1][0] + matriz[n-1][1];
    }

    public static void main(String[] args) {
        String path = args[0];

        System.out.println("Recursão simples:\t" + "Existem " + rec(path, 0, false) + " maneiras");
        System.out.println("Recursão memorizada:\t" + "Existem " + recMemo(path, 0, false, null) + " maneiras");
        System.out.println("Sem recursão:\t\t" + "Existem " + nonRecursive(path) + " maneiras");
        
    }
}