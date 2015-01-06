import java.math.BigInteger;

/**
 * Counts power sets based on length of given array.
 *
 * @author Alexander Roth
 * @date   2015-01-06
 **/
public class PowerSetCounter {

    public static BigInteger powers(int[] list) {
        return new BigInteger("2").pow(list.length);
    }
}
