 public class capt{

    public static void main(){

int birthYear = 1979;
int birthMonth = 8;
int birthDay = 15;
int currentYear = 2016;
int currentMonth = 4;
int currentDay = 13;
int age = currentYear-birthYear;

if(currentMonth < birthMonth || currentMonth == birthMonth && currentDay < birthDay)
    age -= 1;

System.out.println("The captain is " + age +  " years old.");

    }

}
