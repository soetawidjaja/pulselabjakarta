/**
 * Program Name : dynamoDB_Fullscan.java
 * Description  : small app to do full table scan on Amazon DynamoDB and download it into csv format
 * @author      : soetawidjaja
 * Create Date  : 5th November 2013 
 * Last Update  : 7th November 2013
 * History      : (7-11-2013) Add config file (lastkey.properties), to save last hash key history                
 */
 
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Properties;

import com.amazonaws.AmazonClientException;
import com.amazonaws.AmazonServiceException;
import com.amazonaws.auth.ClasspathPropertiesFileCredentialsProvider;
import com.amazonaws.regions.Region;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClient;
import com.amazonaws.services.dynamodbv2.model.AttributeDefinition;
import com.amazonaws.services.dynamodbv2.model.AttributeValue;
import com.amazonaws.services.dynamodbv2.model.ComparisonOperator;
import com.amazonaws.services.dynamodbv2.model.Condition;
import com.amazonaws.services.dynamodbv2.model.CreateTableRequest;
import com.amazonaws.services.dynamodbv2.model.DescribeTableRequest;
import com.amazonaws.services.dynamodbv2.model.KeySchemaElement;
import com.amazonaws.services.dynamodbv2.model.KeyType;
import com.amazonaws.services.dynamodbv2.model.ProvisionedThroughput;
import com.amazonaws.services.dynamodbv2.model.PutItemRequest;
import com.amazonaws.services.dynamodbv2.model.PutItemResult;
import com.amazonaws.services.dynamodbv2.model.ScalarAttributeType;
import com.amazonaws.services.dynamodbv2.model.ScanRequest;
import com.amazonaws.services.dynamodbv2.model.ScanResult;
import com.amazonaws.services.dynamodbv2.model.TableDescription;
import com.amazonaws.services.dynamodbv2.model.TableStatus;

 
public class dynamoDB_FullScan {

   

    static AmazonDynamoDBClient dynamoDB;

    private static void init() throws Exception {
    	 
    	dynamoDB = new AmazonDynamoDBClient(new ClasspathPropertiesFileCredentialsProvider());
        //Region usEast1 = Region.getRegion(Regions.US_EAST_1);
          
        //dynamoDB.setRegion(usEast1);
        
        dynamoDB.setEndpoint("dynamodb.us-east-1.amazonaws.com"); 
         
    }


    public static void main(String[] args) throws Exception {
        init();

        try {
            String tableName = "ImmunizationSideEffect";
 
           
            Date date = new Date();            
            SimpleDateFormat sdf = new SimpleDateFormat("MM/dd/yyyy h:mm:ss ");
            String start = sdf.format(date);
            
            HashMap<String, Condition> scanFilter = new HashMap<String, Condition>();
            ScanRequest scanRequest = new ScanRequest(tableName);
             
             Properties prop = new Properties();
    		 String lastkey = "";
         	 try {
              
         		prop.load(new FileInputStream("/Users/soetawidjaja/Documents/workspace/AWS_DynamoDB_Scan/src/lastkey.properties"));
      
                lastkey = prop.getProperty("lastkey");
         	 
         	  } catch (IOException ex) {
         		ex.printStackTrace();
              }		// TODO Auto-generated method stub
         	
         	 /*
             if (lastkey != "null" || lastkey != "") {
            	 
            	 scanRequest.setExclusiveStartKey(lastkey);
            	 --> need to save hash-map to file config
            	 
             }
             */
             
             
             ScanResult scanResult = dynamoDB.scan(scanRequest);
             List<Map<String, AttributeValue>> rows = scanResult.getItems();
             
              
            File file =new File(tableName + ".json");
            if(!file.exists()){ file.createNewFile(); }
             
            FileWriter fileWritter = new FileWriter(file.getName(),true);
 	        BufferedWriter bufferWritter = new BufferedWriter(fileWritter);
                     
            int i = 1;
            int num = rows.size();
            int trecs = 0;
            
            while  (scanResult != null && num <= 4519){//num <= 13418 
            	 
            	
            	bufferWritter.write(scanResult.toString());
            	
            	System.out.println("Result: " + scanResult);
            	System.out.println("NumIter: " + i + "-numRows= " + num);
            	 
            	trecs = trecs + rows.size();
            	
            	scanRequest.setExclusiveStartKey(scanResult.getLastEvaluatedKey());
            	scanResult = dynamoDB.scan(scanRequest);
            	i++;
            	rows = scanResult.getItems();
            	num = num + rows.size();
            	 
            	if (i%3 == 0){
            		System.out.println("inside sleep:"  + i );
            		Thread.sleep(240000);
            	}
            	 
            	
            }
            
	        bufferWritter.close();
             
	       //String finish = sdf.format(date);
	        
           System.out.println("Finished Download from Amazon DynamoDB: " + tableName);
           //System.out.println("Started at: " + start + ", Finished at: " + finish);
           //System.out.println("Total Records: "  + trecs);
           
           

        } catch (AmazonServiceException ase) {
            System.out.println("Caught an AmazonServiceException, which means your request made it "
                    + "to AWS, but was rejected with an error response for some reason.");
            System.out.println("Error Message:    " + ase.getMessage());
            System.out.println("HTTP Status Code: " + ase.getStatusCode());
            System.out.println("AWS Error Code:   " + ase.getErrorCode());
            System.out.println("Error Type:       " + ase.getErrorType());
            System.out.println("Request ID:       " + ase.getRequestId());
        } catch (AmazonClientException ace) {
            System.out.println("Caught an AmazonClientException, which means the client encountered "
                    + "a serious internal problem while trying to communicate with AWS, "
                    + "such as not being able to access the network.");
            System.out.println("Error Message: " + ace.getMessage());
        }
    }

    private static Map<String, AttributeValue> newItem(String name, int year, String rating, String... fans) {
        Map<String, AttributeValue> item = new HashMap<String, AttributeValue>();
        item.put("name", new AttributeValue(name));
        item.put("year", new AttributeValue().withN(Integer.toString(year)));
        item.put("rating", new AttributeValue(rating));
        item.put("fans", new AttributeValue().withSS(fans));

        return item;
    }

    private static void waitForTableToBecomeAvailable(String tableName) {
        System.out.println("Waiting for " + tableName + " to become ACTIVE...");

        long startTime = System.currentTimeMillis();
        long endTime = startTime + (10 * 60 * 1000);
        while (System.currentTimeMillis() < endTime) {
            try {Thread.sleep(1000 * 20);} catch (Exception e) {}
            try {
                DescribeTableRequest request = new DescribeTableRequest().withTableName(tableName);
                TableDescription tableDescription = dynamoDB.describeTable(request).getTable();
                String tableStatus = tableDescription.getTableStatus();
                System.out.println("  - current state: " + tableStatus);
                if (tableStatus.equals(TableStatus.ACTIVE.toString())) return;
            } catch (AmazonServiceException ase) {
                if (ase.getErrorCode().equalsIgnoreCase("ResourceNotFoundException") == false) throw ase;
            }
        }

        throw new RuntimeException("Table " + tableName + " never went active");
    }

}
