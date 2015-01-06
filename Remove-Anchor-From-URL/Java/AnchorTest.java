import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 *
 *
 * @author Alexander Roth
 * @date   2015-01-05
 **/

public class AnchorTest {

    @Test
    public void testWithAnchor() {
        String testString = "www.codewars.com#about";
        String cleanString = AnchorRemover.removeUrlAnchor(testString);
        assertEquals(cleanString, "www.codewars.com");
    }

    @Test
    public void testWithoutAnchor() {
        String testString = "www.codewars.com?test=1";
        String cleanString = AnchorRemover.removeUrlAnchor(testString);
        assertEquals(cleanString, "www.codewars.com?test=1");
    }
}
