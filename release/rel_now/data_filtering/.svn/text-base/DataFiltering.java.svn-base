/**
 * Program Name : DataFiltering.java
 * Description  : small app to filter outliers from commodity price data, using 4 type of scenario
 * @author 		: soetawidjaja
 * Create Date  : 7th October 2013 
 * Last Update  : 10th October 2013
 * History      :  
 * Scenario		: (1) Use fix yearly acceptable value (min and max) per year to filter daily prices 
 *           	  (2) Use dynamic daily filter (introducing bootstrap price and sensitivity value to calculate next day acceptable value)
 *           	  (3) Use dynamic filtering using daily quartile to define next day min and max, fence using statistics method approach
 *           	  (4) Use dynamic filtering using daily quartile to define next day min and max, fence using sensitivity value 
 */

package datafiltering;

import com.sun.corba.se.impl.util.Version;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Collections;
import java.util.Date;
import java.util.List;
import org.joda.time.DateTime;
import org.joda.time.Days;

public class DataFiltering {

    /**
     * @param args the command line arguments
     */
    @SuppressWarnings("empty-statement")
    
    
    public static void main(String[] args) {
        // TODO code application logic here
        
        String dbURL = "";
        String username ="";
        String password = "";
       
        Connection dbCon = null;
        Statement stmt = null;
        ResultSet rs = null;
        
        //using scenario 1
        int    filterScenario =  4;
        String commodityType = "daging sapi";
        double stdDev           = 0.9;
        int    fenceDist        = 25;
        int    bootstrapPrice2010 = 60000;  
        int    bootstrapPrice2012 = 60000;
        int    bootstrapPrice2013 = 60000;
        int    o2010 = 0,o2012 = 0,o2013 = 0,v2010 = 0,v2012 = 0,v2013 = 0;
        int    mp2010 = 0,mp2012 = 0,mp2013 = 0,MP2010 = 0,MP2012 = 0,MP2013 = 0;
        int[]  arrayBootStrap = {bootstrapPrice2010,bootstrapPrice2012,bootstrapPrice2013};
         
        
        
        Date date = new Date();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyyMMdd.hhmmss");
        String formattedDate = sdf.format(date);
        System.out.println(formattedDate);

        String filename = "fMeat"+ "_T" + filterScenario +"_"+ stdDev + "_" + "P" + bootstrapPrice2010 + "_" +formattedDate +".csv";
                
          
        System.out.println("Commodity Extracted: " + commodityType );
        try {
            int[]  arrYear = {2010,2012,2013};
            int i;
            
            
             
            
            ArrayList<ArrayList<String>> StrListData = new ArrayList<ArrayList<String>>();
            
            int minTH2010 =  (int) (bootstrapPrice2010 - bootstrapPrice2010 * stdDev);
            int maxTH2010 =  (int) (bootstrapPrice2010 + bootstrapPrice2010 * stdDev);
            int minTH2012 =  (int) (bootstrapPrice2012 - bootstrapPrice2012 * stdDev);
            int maxTH2012 =  (int) (bootstrapPrice2012 + bootstrapPrice2012 * stdDev);
            int minTH2013 =  (int) (bootstrapPrice2013 - bootstrapPrice2013 * stdDev);
            int maxTH2013 =  (int) (bootstrapPrice2013 + bootstrapPrice2013 * stdDev);
            Date cDate = null;
            int cPrice = 0,cMin = 0,cMax = 0,minTH = 0,maxTH = 0;
            int curYear, Outlier;

            dbCon = DriverManager.getConnection(dbURL, username, password);
            
            for (i = 0;i < arrYear.length;i++){
                 
                String tahun =   Integer.toString(arrYear[i]);
                String query = "select TweetDate,price from T_HistoricalPrice where Commodity = '" + commodityType +"' and Year(TweetDate) = "+ tahun +"  order by TweetDate";
                
                stmt  = dbCon.prepareStatement(query);
                rs = stmt.executeQuery(query);
                
                switch(arrYear[i]){
                   case 2010: minTH = minTH2010; maxTH =  maxTH2010;
                              break;
                   case 2012: minTH = minTH2012; maxTH =  maxTH2012;
                              break;
                   case 2013: minTH = minTH2013; maxTH =  maxTH2013;
                              break;                   
                }
                
                 
                List<Integer> sortArray =  new ArrayList<Integer>();
                
                
                while (rs.next()){
                    if (cDate == null) {
                        cDate  = rs.getDate(1); 
                        cPrice = rs.getInt(2);
                        //cMin   = minTH;
                        //cMax   = maxTH;                        
                    }else{
                        
                        if (cDate.toString().equals(rs.getDate(1).toString()) ){ //price explored is the same with "current working date"
                            cPrice = rs.getInt(2);
                   
                        }else if (!cDate.toString().equals(rs.getDate(1).toString()) ){
                             
                            if (cDate.getYear() != rs.getDate(1).getYear()){//very rare change of year                                
                                minTH = minTH;
                                maxTH = maxTH;
                                cDate  = rs.getDate(1);
                                cPrice = rs.getInt(2);
                                
                            }else{//price explored is not the same with current working date (cwd), cwd change to explored date
                            
                                cDate  = rs.getDate(1);
                                cPrice = rs.getInt(2);
                                
                                int IQR;
                             
                                //if date is changed, need to check max and min price on the previous day price table 
                                if (sortArray.isEmpty()){
                                    //previus day price is not available, using previous Threshold for calculate new acceptable value
                                    
                                     switch(filterScenario){
                                        case 1 :  
                                                 // scenario 1
                                                 minTH = minTH;
                                                 maxTH = maxTH;
                                     
                                                 break;
                                        case 2 :   
                                                //scenario 2
                                                 minTH = (int) Math.round(minTH - minTH * stdDev);
                                                 maxTH = (int) Math.round(maxTH + maxTH * stdDev);
                                                  
                                                  break;
                                        case 3 : 
                                               //Scenario 3
                                                 IQR = maxTH - minTH;
                                                 minTH = (int) Math.round(minTH - 1.5 * IQR);
                                                 maxTH = (int) Math.round(maxTH + 1.5 * IQR);
                                                 
                                                 break;                   
                                        case 4 : 
                                               //Scenario 4
                                                 minTH = (int) Math.round(minTH - minTH * stdDev);
                                                 maxTH = (int) Math.round(maxTH + maxTH * stdDev);
                                                 
                                                 break;                       
                                      }//end of switch
                                            
                                    
                                }else{//previous day price table is available, get min and max price from prev day
                                 
                                 /* sort using array
                                    int length =  sortArray.size();
                                    Integer[] arrTemp = sortArray.toArray(new Integer[length]);
                                    Arrays.sort(arrTemp);
                                    cMin = arrTemp[0];
                                    cMax = arrTemp[length-1];
                                */  
                                    Collections.sort(sortArray);
                                     
                                    switch(filterScenario){
                                        case 1 :  
                                               //scenario 1
                                      
                                               if (rs.getDate(1).getYear() == 2010){
                                                    minTH = minTH2010;
                                                    maxTH = maxTH2010;
                                               }else if (rs.getDate(1).getYear() == 2012){
                                                    minTH = minTH2012;
                                                    maxTH = maxTH2012;
                                                }else if (rs.getDate(1).getYear() == 2013){
                                                    minTH = minTH2013;
                                                    maxTH = maxTH2013;
                                                }
                                                break;
                                        case 2 :   
                                                //scenario 2
                                                
                                                 cMin = sortArray.get(0);
                                                 cMax = sortArray.get(sortArray.size()-1);
                                
                                                 minTH =   (int) Math.round(cMin - cMin * stdDev);
                                                 maxTH =   (int) Math.round(cMax + cMax * stdDev);
                                                  
                                                  break;
                                        case 3 : 
                                               //Scenario 3
                                                  cMin = quartile(sortArray,25);
                                                  cMax = quartile(sortArray,75);
                                          
                                                  IQR = cMax - cMin;
                                                  
                                                  if (sortArray.size() == 1){
                                                        System.out.println("IQR 0 --> " + IQR);
                                                  }else{
                                                        System.out.println("Component# " + sortArray.size() + " : IQR -->  " + IQR );
                                                  }
                                          
                                                 minTH =   (int) Math.round(cMin - 1.5 * IQR);
                                                 maxTH =   (int) Math.round(cMax + 1.5 * IQR);
                                                 
                                                 break;                   
                                        case 4 : 
                                               //Scenario 4
                                                  cMin = quartile(sortArray,25);
                                                  cMax = quartile(sortArray,75);
                                          
                                                  IQR = cMax - cMin;
                                                  
                                                  if (sortArray.size() == 1){
                                                        System.out.println(" Scenario 4 - IQR 0 --> " + IQR);
                                                  }else{
                                                        System.out.println(" Scenario 4 - Component# " + sortArray.size() + " : IQR -->  " + IQR );
                                                  }
                                          
                                                 minTH =   (int) Math.round(cMin - cMin * stdDev);
                                                 maxTH =   (int) Math.round(cMax + cMax * stdDev);
                                                 
                                                 break;     
                                      }//end of switch
                                    
                                    
                                    for (int j=0;j<sortArray.size();j++){
                                       System.out.println(">> array component >> " + sortArray.get(j) );
                                    }
                                    System.out.println("sort array result >> cMin: " + cMin + ", cMax:" + cMax + ", minTH: " + minTH + ",maxTH:" + maxTH);
                                    
                                    sortArray.clear();
                                }//end else not the same date
                            
                            }//else taun sama
                        }
                    }
                    
                    Calendar cal = Calendar.getInstance();
                    cal.setTime(cDate);
                    int year = cal.get(Calendar.YEAR);
                       
                    if (minTH <= cPrice && cPrice <= maxTH){//checking current price is outlier based on minTH and maxTH                         
                       Outlier = 0;
                       sortArray.add(cPrice);
                        
                  
                       
     
                       //soetawidjaja TBD hahaha...
                       switch(year){
                           case 2010:
                                   v2010 = v2010 + 1;
                                   if (cPrice < mp2010 ){ mp2010 = cPrice;}
                                   if (cPrice > MP2010 ){ MP2010 = cPrice;}
                                   break;
                           case 2012:
                                   v2012 = v2012 + 1;
                                   if (cPrice < mp2012 ){ mp2012 = cPrice;}
                                   if (cPrice > MP2012 ){ MP2012 = cPrice;}
                                   break;
                           case 2013:
                                   v2013 = v2013 + 1;
                                   if (cPrice < mp2013 ){ mp2013 = cPrice;}
                                   if (cPrice > MP2013 ){ MP2013 = cPrice;}
                                   break;
                       } 
                       
                    }else {
                       Outlier = 1;
                        
                       switch(year){
                           case 2010:
                                   o2010 = o2010 + 1;
                                    
                                   break;
                           case 2012:
                                   o2012 = o2012 + 1;
                                    
                                   break;
                           case 2013:
                                   o2013 = o2013 + 1;
                                    
                                   break;
                       } 
                    }
                    
                    System.out.println("Date:" + rs.getDate(1).toString() + " - minTH:" + minTH + " - maxTH:" + maxTH + " - cPrice:" + cPrice +  " - CMin:" + cMin + " - cMax:" + cMax + "  - Outlier:" + Outlier);
                    
                    ArrayList<String> StrData = new ArrayList<String>(); 
  
                    StrData.add(rs.getDate(1).toString());
                    StrData.add(Integer.toString(cPrice));
                    StrData.add(Integer.toString(Outlier));
                    
                    StrListData.add(StrData);
                
                }//end while
                
                
            }//end for
            
        //Writing to File    
            
        try
	{
             
	    FileWriter writer = new FileWriter(filename);
             
            int j;
             
	    for (i=0;i<StrListData.size();i++){
               ArrayList<String> temp = new ArrayList<String>();
               temp = StrListData.get(i);
                
               for(j=0;j<temp.size();j++){
                   writer.append(temp.get(j));
                   if (j<temp.size()-1){
                       writer.append(',');
                   }
                   
               }
               writer.append('\n');
            }
         
            int t2010 = o2010 + v2010; 
            int t2012 = o2012 + v2012;
            int t2013 = o2013 + v2013;
            int total = t2010 + t2012 + t2013;
            int tO = o2010 + o2012 + o2013;
            int tV = v2010 + v2012 + v2013;
            
            //float pctV = tV/total * 100 ;
             
                    
             
            System.out.println("####################################################");         
            System.out.println("Sucsessfull filtering Commodity : " + commodityType);            
            System.out.println("Bootstrap Price 2010            :"  + bootstrapPrice2010);
            System.out.println("Bootstrap Price 2012            :"  + bootstrapPrice2012);
            System.out.println("Bootstrap Price 2013            :"  + bootstrapPrice2013);
            System.out.println("Sensitivity                     :"  + stdDev);
            System.out.println("Scenario used                   :"  + filterScenario);
            System.out.println("====================================================");
            System.out.println("Total Data Points 2010:" + t2010);
            System.out.println("Outliers              :" + o2010);
            System.out.println("Valid                 :" + v2010);
            //System.out.println("Min Price             :" + mp2010);
            //System.out.println("Max Price             :" + MP2010);
            System.out.println("====================================================");
            System.out.println("Total Data Points 2012:" + t2012);
            System.out.println("Outliers              :" + o2012);
            System.out.println("Valid                 :" + v2012);
            //System.out.println("Min Price             :" + mp2012);
            //System.out.println("Max Price             :" + MP2012);
            System.out.println("====================================================");
            System.out.println("Total Data Points 2013:" + t2013);
            System.out.println("Outliers              :" + o2013);
            System.out.println("Valid                 :" + v2013);
            //System.out.println("Min Price             :" + mp2013);
            //System.out.println("Max Price             :" + MP2013);
            System.out.println("====================================================");
            System.out.println("Total Data Points Filtered :" + total);
            System.out.println("Total Outliers             :" + tO);
            System.out.println("Total Valid                :" + tV);
            //System.out.println("Percentage of Valid Data   :" + pctV + "%");
            
                         
            
            
	    writer.flush();
	    writer.close();
            System.out.println("Sucsessfull writing file: " + filename);
	}
	catch(IOException e)
	{
	     e.printStackTrace();
	} 
           
        } catch (SQLException ex) {
            //Logger.getLogger(CollectionTest.class.getName()).log(Level.SEVERE, null, ex);
            System.out.println("count of stock : " + ex.getMessage() );
        } finally{
           try {
                if (rs != null) {
                    rs.close();
                }
                if (stmt != null) {
                    stmt.close();
                }
                if (dbCon != null) {
                    dbCon.close();
                }

            } catch (SQLException ex) {
                Logger lgr = Logger.getLogger(Version.class.getName());
                lgr.log(Level.WARNING, ex.getMessage(), ex);
            }
        }
    }
    
    public static Integer quartile(List<Integer> values, Integer lowerPercent) {

        /*
        if (values == null || values.length == 0) {
            throw new IllegalArgumentException("The data array either is null or does not contain any data.");
        }*/

        // Rank order the values
        List<Integer> v =  new ArrayList<Integer>(values);
       
        //Collections.copy(v,values);
        Collections.sort(v); 
       

        int n = (int) Math.round(v.size() * lowerPercent / 100);
        
        return v.get(n);

    }
}
