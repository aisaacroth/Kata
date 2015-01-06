import java.math.BigInteger;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 * Test cases for the Power Set Counter class.
 *
 * @author Alexander Roth
 * @date   2015-01-06
 **/
public class PowerSetCounterTest {

    @Test
    public void testEmptySet() {
        int[] emptyArray = new int[] {};
        BigInteger powerNumber = PowerSetCounter.powers(emptyArray);
        assertEquals(powerNumber, BigInteger.ONE);
    }

    @Test
    public void testSmallSet() {
        int[] numberArray = new int[] {1, 2, 3};
        BigInteger powerNumber = PowerSetCounter.powers(numberArray);
        assertEquals(powerNumber, new BigInteger("8"));
    }
}
