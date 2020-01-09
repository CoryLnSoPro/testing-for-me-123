import java.util.Scanner;
public class MPG {
public static void main(String[] args) {
        
        Scanner Scn = new Scanner(System.in);
        
        // Get brand of the car.
        String carBrand;
        System.out.println("Please enter the brand of your car: ");
        carBrand = Scn.nextLine();
        
        // Get starting odometer mileage.
        Double startingMileage = 0.0;
        Scanner SCAN = new Scanner(System.in);
        System.out.println("Please enter the starting odometer mileage: ");
        startingMileage = SCAN.nextDouble();
        
        // Get ending odometer mileage.
        Double endingMileage = 0.0;
        System.out.println("Please enter the ending odometer mileage: ");
        endingMileage = SCAN.nextDouble();
                                                                      
        // Get total gallons used on trip.
        Double gallonsUsed = 0.0;
        System.out.println("Please enter the gallons used in the total trip: ");
        gallonsUsed = SCAN.nextDouble();
        
        // Formula to calculate Miles Per Gallon.
        Double MPG = (endingMileage - startingMileage)/(gallonsUsed);
        
        // Print everything entered on separate lines
        System.out.println("Make: " + carBrand);
        System.out.println("Starting mileage: " + startingMileage);
        System.out.println("Ending mileage: " + endingMileage);
        // Print out the Miles Per Gallon that the car used in the trip.
        System.out.println("MPG: " + MPG);
        // And MPG again in a sentence just to reiterate
        System.out.println("Your " + carBrand + " got "+ MPG + " miles per gallon on your trip.");
    }
}
