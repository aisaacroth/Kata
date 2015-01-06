import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

/**
 * Test Runner for SequenceSum program.
 *
 * @author Alexander Roth
 * @date   2015-01-06
 **/
public class SequenceSumTestRunner {

    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(SequenceSumTest.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }

        System.out.println(result.wasSuccessful());
    }
    
}
