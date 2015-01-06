/**
 * 
 * @author Alexander Roth
 * @date   2015-01-05
 **/
public class AnchorRemover {

    public static String removeUrlAnchor(String url) {
        String cleanUrl = "";

        if (urlHasAnchor(url)) {
            cleanUrl = removeAnchor(url);
        } else {
            cleanUrl = url;
        }

        return cleanUrl;
    }

    public static boolean urlHasAnchor(String url) {
       return url.contains("#"); 
    }

    public static String removeAnchor(String url) {
        int anchorIndex = url.indexOf("#");
        String cleanUrl = url.substring(0, anchorIndex);
        return cleanUrl;
    }
}
