public class Main
{
    public static void main(String args[]) 
    {
     String s="Helloworld";
     for (int i=0;i<s.length();i++)
     {
         int a=(s.charAt(i)^127);
         String str = new Character((char)a).toString();
         System.out.print(s.charAt(i)+" & 127:"+((char)(s.charAt(i)&127)));
         System.out.print("\t"+s.charAt(i)+" | 127:"+((char)(s.charAt(i)|127)));
         System.out.print("\t"+s.charAt(i)+" ^ 127:"+str);
         System.out.println("");
     }
      
     
    }
}
    
}