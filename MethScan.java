import java.util.Scanner;

public class MethScan {

	public static void main(String[] args) {
		
		String result = InputDataFromSCanner();
		System.out.println(result);
	}
	
	public static String InputDataFromSCanner()
	{
		Scanner scan = new Scanner(System.in);
		try{
		System.out.println("Enter String 1");
		String str1 = scan.nextLine();
		System.out.println("Enter String 2");
		String str2 = scan.nextLine();
		System.out.println("Enter String 3");
		String str3 = scan.nextLine();
		
		System.out.println(str1);
		System.out.println(str2);
		System.out.println(str3);
		}catch(Exception e)
		{
			return "Failure";
		}
		return "Success";
	}

}