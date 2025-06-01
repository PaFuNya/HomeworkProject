package Shotime;
import java.io.*;

public class OOOO {
    private static void copyFile(String wow,String sss){
        FileReader fis=null;
        FileWriter fos=null;
        try {
            fis=new FileReader(wow);
            fos=new FileWriter(sss);
            char []buffer=new char[1024];
            fis.read(buffer);
            fos.write(buffer);
            int tmp=0;
                while((tmp=fis.read(buffer))!=-1){
                    fos.write(buffer,0,tmp);
                }
        } catch (IOException e) {
            System.out.println("抱错啦！");
        }finally{
            try {
                if(fis!=null)
                fis.close();
                if(fos!=null)
                fos.close();
            } catch (Exception e) {
                // TODO: handle exception
            }
        }
        System.out.println("OVER！");
    }
    public static void main(String[] args){
        copyFile("d:\\A.txt","d:\\B.txt");

    }
}
