import java.util.Scanner;

class Area
{
	float area = 0;
	Area(float radius)
	{
		area = 3.1415f * radius * radius;
	}
	Area(float length, float breadth)
	{
		area = length * breadth;
	}
}


public class AreaCons
{
	public static void main(String[] args)
	{
		Scanner s = new Scanner(System.in);
		System.out.println("Enter the shape whose area has to be calculated: ('r' for rectangle 'c' for circle");
		char ch = s.nextChar();
		if(ch == 'r')
		{
			System.out.println("Enter the measurements:");
			float size1 = s.nextFloat();
		    float size2 = s.nextFloat();
		    System.out.println("Them " + size1 + "ThemAgain" + size2);
	    }
	    if(ch == 'c')
		{
			System.out.println("Enter the measurement:");
			float size1 = s.nextFloat();
		    System.out.println("Them " + size1);
	    }

	}
}
