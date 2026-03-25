public class DataTypes {
	
	public static void main(String[] args) {
		
		int myInt = 19;
		System.out.println(myInt);
		
		double myDouble = 1.60;
		System.out.println(myDouble);
		
		char myChar = 'H';
		System.out.println(myChar);
		
		boolean myBoolean = true;
		myBoolean = false;
		System.out.println(myBoolean);

		String myString = "Hola, Java";
		System.out.println(myString);

		// Tipo de dato en tiempo de compilación

		System.out.println(myString.getClass().getSimpleName());
		}
	}
