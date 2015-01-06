/**
 * Sequence Sum java version
 *
 * @author Alexander Roth
 * @date   2015-01-06
 **/
public class SequenceSum {
    
    public static int[] sumOfN(int n) {
        int[] result = new int[Math.abs(n) + 1];

        int sum = 0;
        int sign = (int) Math.signum(n);

        for (int i = 0; i < result.length; i++) {
            result[i] = sum + sign * i;
            sum += sign * i;
        }

        return result;
    }

}
