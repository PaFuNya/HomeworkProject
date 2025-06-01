package Shotime;
import java.io.FileInputStream;

public class App {
                public static void main(String[] args) throws Exception {
                    FileInputStream fis=null;
                    try {
                        fis=new FileInputStream("D:\\A.txt");
                        StringBuffer strb=new StringBuffer();
                        int tmp=0;
                        while ((tmp=fis.read())!=-1) {
                            strb.append((char)tmp);    
                        }
                        System.out.println(strb);
                    } catch (Exception e) {
                        System.out.println("报错咯");
                    }finally{
                        try {
                            if(fis!=null)
                            fis.close();
                        } catch (Exception e) {
                            System.out.println("WOW");
                        }
                        
        }
    }
}
