/**
 * Program Name : DataIndexing.java
 * Description  : small app to create index number from timeseries data
 * @author 		: soetawidjaja
 * Create Date  : 7th October 2013 
 * Last Update  : 10th October 2013
 * History      :  
 * Scenario		: {'1-1-2013', '2-1-2013', '28-1-2013', '1-2-2013', '28-2-2013'} --> {1,2,28,32,59}
 *           	   
 */

package dataindexing;



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
import java.util.Date;
import org.joda.time.DateTime;
import org.joda.time.Days;
  
 

public class dataindexing {

    /**
     * @param args the command line arguments
     */
    
    
    public class dataStructure{
        
    
    }
    
    public static void main(String[] args) {
        String dbURL = "jdbc:mysql://localhost:3306/PriceQuotes";
        String username ="developer";
        String password = "developer";
       
        Connection dbCon = null;
        Statement stmt = null;
        ResultSet rs = null;
        
        String commodityType = "daging sapi"; 
         
        String query = "select distinct TweetDate from T_HistoricalPrice where Commodity = '" + commodityType +"' order by TweetDate";
         
        System.out.println("Commodity Extracted: " + commodityType );
        try {
            
            int i;
            ArrayList<String> StrArray = new ArrayList<String>(); 
            
            ArrayList<ArrayList<String>> StrList = new ArrayList<ArrayList<String>>();
            
             
            dbCon = DriverManager.getConnection(dbURL, username, password);
            stmt  = dbCon.prepareStatement(query);
            rs = stmt.executeQuery(query);
            
            
            while(rs.next()){
               StrArray.add(rs.getDate(1).toString());             
            }
            
            
            long seqIdx,timeDiff,dateDiff; 
            SimpleDateFormat dtFormat = new SimpleDateFormat("yyyy-MM-dd");
            Date currDate,prevDate = null;
            
            seqIdx = 1;
            
            for (i=0;i<StrArray.size();i++){
                //query = "select distinct(price) from T_HistoricalPrice where Tweetdate='" + StrArray.get(i).replace('-', '/') + "' and Commodity='" + commodityType + "'";
                query = "select  price  from T_HistoricalPrice where Tweetdate='" + StrArray.get(i).replace('-', '/') + "' and Commodity='" + commodityType + "'";
                
                stmt = dbCon.prepareStatement(query);
                rs = stmt.executeQuery(query);
                 
                ArrayList<String> StrRec = new ArrayList<String>(); 
                
                 //this is the sequence creation
                  
                 if (i != 0){
                     try{
                          currDate = dtFormat.parse(StrArray.get(i));
                          prevDate = dtFormat.parse(StrArray.get(i-1));
                 
                          DateTime dt1 = new DateTime(currDate);
		          DateTime dt2 = new DateTime(prevDate);
                
                          /*
                          timeDiff = currDate.getTime() - prevDate.getTime() ;
                          dateDiff = timeDiff / (24 * 3600 * 1000);
                          */
                          
                          dateDiff = Days.daysBetween(dt2, dt1).getDays();
                          
                          seqIdx   = dateDiff + seqIdx;
                 
                     }catch(Exception e){
                          e.printStackTrace();
                     }
                  }
                
                System.out.println("Sequence Index: " + seqIdx);
                
                //StrRec.add(StrArray.get(i));
                StrRec.add(Long.toString(seqIdx));              
                 
                System.out.println("Date : " + StrArray.get(i) );
                
                while(rs.next()){
                   StrRec.add(rs.getString(1));
                   System.out.println("Value : " + rs.getString(1));
                }
               StrList.add(StrRec);
            } 
            
             
            
             
            
        try
	{
             
	    FileWriter writer = new FileWriter(commodityType+"DupX.csv");
             
            int j;
             
	    for (i=0;i<StrList.size();i++){
               ArrayList<String> temp = new ArrayList<String>();
               temp = StrList.get(i);
                
               for(j=0;j<temp.size();j++){
                   writer.append(temp.get(j));
                   if (j<temp.size()-1){
                       writer.append(',');
                   }
                   
               }
               writer.append('\n');
            }
                         
 
	    writer.flush();
	    writer.close();
            System.out.println("Sucsessfull writing file: " + commodityType + ".csv");
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
    
    
}
