import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class GodTest {
    @Test
    public void makingAdam() {
        Human[] paradise = God.create();
        assertEquals("Adam is a man", true, paradise[0] instanceof Man);
    }

    @Test
    public void makingEve() {
        Human[] paradise = God.create();
        assertEquals("Eve is a woman", true, paradise[1] instanceof Woman);
    }
}
