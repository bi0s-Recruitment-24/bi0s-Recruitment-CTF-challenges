import java.util.HashMap;
import java.util.Scanner;

public class m{
    public static String c(String i){
        HashMap<Character,Character>m=new HashMap<>();
        for(int c:new int[]{65,97}){
            for(int j=0;j<26;j++){
                char o=(char)(j+c);
                char r=(char)((j+13)%26+c);
                m.put(o,r);
            }
        }
        StringBuilder r=new StringBuilder();
        for(char c:i.toCharArray()){
            r.append(m.getOrDefault(c,c));
        }
        return r.reverse().toString();
    }
    public static void main(String[]a){
        Scanner s=new Scanner(System.in);
        System.out.print("Enter the flag: ");
        String i=s.nextLine();
        if(i.startsWith("bi0s{")&&i.endsWith("}")){
            String m=i.substring(5,i.length()-1);
            if(c(m).equals("rSNF_qaN_Yhse3J0c_rycZVf_Fv_Ni4w")){
                System.out.println("that's right");
            }else{
                System.out.println("Oops, wrong flag!");
            }
        }else{
            System.out.println("Oops, wrong flag format!");
        }
        s.close();
    }
}

