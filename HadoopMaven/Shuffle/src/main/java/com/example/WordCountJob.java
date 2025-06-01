package com.example;

// 由于 public 类型的 WordCountJob 必须定义在其自己的文件中，
// 此文件应单独创建，文件名应为 WordCountJob.java
public class WordCountJob {
    /**
     * 组装job=map+reduce
     * @param args
     */
    public static void main(String[] args) {
        try {
            if(args.length!=2){
                //  如果传递的参数不够，程序直接退出
                System.exit(100);
            }
            //  job需要的配置参数
            Configuration conf = new Configuration();
            //  创建一个job
            Job job = Job.getInstance(conf);

            //  注意：这一行必须设置，否则在集群中执行的是找不到WordCountJob这个类
            job.setJarByClass(WordCountJob.class);

            //  指定输入路径(可以是文件，也可以是目录)
            FileInputFormat.setInputPaths(job,new Path(args[0]));
            //  指定输出路径(只能指定一个不存在的目录)
            FileOutputFormat.setOutputPath(job,new Path(args[1]));

            //  指定map相关的代码
            job.setMapperClass(MyMapper.class);
            //  指定k2的类型
            job.setMapOutputKeyClass(Text.class);
            //  指定v2的类型
            job.setMapOutputValueClass(LongWritable.class);

            //  指定reduce相关的代码
            job.setReducerClass(MyReducer.class);
            //  指定k3的类型
            job.setOutputKeyClass(Text.class);
            //  指定v3的类型
            job.setOutputValueClass(LongWritable.class);


            //  提交job
            job.waitForCompletion(true);


        }catch (Exception e){
            e.printStackTrace();
        }

    }
}