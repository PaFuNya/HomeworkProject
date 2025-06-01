package Shotime;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.nio.Buffer;
public class OVER {
    public static void main(String[] args){
        //BufferedReader wo=new BufferedReader(new FileReader("D:\\A.txt"));
        BufferedReader wo=null;
        BufferedWriter as=null;
        FileReader fis=null;
        FileWriter fos=null;
            try {
                fis=new FileReader("D:\\A.txt");
                fos=new FileWriter("D:\\l.txt");
                wo=new BufferedReader(fis);
                as=new BufferedWriter(fos);
                    char[]buffer=new char[1024];
                    wo.readLine();
                    String tmp="";
                        while((tmp=wo.readLine())!=null){
                            as.write(tmp);
                            as.newLine();
                        }
            } catch (Exception e) {
                System.out.println("呦呦呦抱错啦！");
            }finally{
                try {
                    if (wo!=null) 
                        fis.close();
                    if(as!=null)
                        fos.close();
                } catch (Exception e) {
                    System.out.println("报错轼！");
                }
            }
            System.out.println("OVER!!");
    }
}
