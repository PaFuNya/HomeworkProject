package Shotime;
import java.io.*;

public class LST03 {
    private static void copyFile(String file1,String file2){
        FileInputStream fis=null;
        FileOutputStream fos=null;
        try {
            fis=new FileInputStream(file1);
            fos=new FileOutputStream(file2);
            byte[]buffer=new byte[1024];
            fis.read(buffer);
            int tmp=0;
                while ((tmp=fis.read(buffer))!=-1) {
                    fos.write(buffer);
                }
        } catch (IOException e) {
            System.out.println("输入出错啦！");
        }finally{
            try {
                if(fis!=null)
                    fis.close();
                if(fos!=null)
                    fos.close();
            }catch (Exception e) {
                // TODO: handle exception
            }
            }
            System.out.println("复制成功！");
        }
public static void main(String[] args){
        copyFile("D:\\A.txt","D:\\c.txt");{

    }
}
}