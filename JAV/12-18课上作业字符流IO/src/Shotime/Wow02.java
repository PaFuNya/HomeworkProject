package Shotime;
import java.io.FileOutputStream;
import java.io.IOException;
public class Wow02 {
    public static void main(String[] args){
        FileOutputStream fos=null;
            try {
                fos=new FileOutputStream("D:\\A.txt");
                String str="Good job!";
                fos.write(str.getBytes());
            } catch (Exception e) {
                // TODO: handle exception
            }finally{
                try {
                    if(fos!=null)
                    fos.close();
                } catch (Exception e) {
                    // TODO: handle exception
                }
            }
            System.out.println("写入成功!");
    }
}
