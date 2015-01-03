public class God {

    public static Human[] create() {
        Man adam = new Man("Adam");
        Woman eve = new Woman("Eve");
        Human[] humans = new Human[2];
        humans[0] = adam;
        humans[1] = eve;
        return humans;
    }

    public static void main(String[] args) {
        create();
    }

}
