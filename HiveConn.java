package com.tjoeun.hadoop;

import java.sql.SQLException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.DriverManager;

public class HiveConn {
   private static String driverName = "org.apache.hive.jdbc.HiveDriver";
   
   public static void main(String[] args) throws Exception {
   
      // Register driver and create driver instance
      Class.forName(driverName);
      
      // get connection, 데이터베이스 이름 : userdb
      // VMWare의 Ubuntu에 Hadoop, Hive가 실행되고, 호스트 컴의 Eclipse에서 이 클래스 실행
      Connection con = DriverManager.getConnection("jdbc:hive2://192.168.66.128:10000/userdb", "hduser", "hduser");
      
      // create statement
      Statement stmt = con.createStatement();
      
      // execute statement.   default 데이터베이스에 employee 테이블 생성 후 테스트
      ResultSet res = stmt.executeQuery("SELECT * FROM employee WHERE salary>30000");
      
      System.out.println("Result:");
      System.out.println(" ID \t Name \t Salary \t Designation ");
      
      while (res.next()) {
         System.out.println(res.getInt(1) + " " + res.getString(2) + " " + res.getDouble(3) + " " + res.getString(4));
      }
      con.close();
   }
}