<?php
echo '<html><meta http-equiv="refresh" content="10" >';
echo '<head/><body> GeoLocating Twitter API Channel 1 <br>';
$numeric = rand();
echo 'Thread ID: '.$numeric. '<br>';


/*
Institution   : Global Pulse Lab Jakarta
Program name  : channel1.php  
Decription    : add geo location to tweet data, this programm will automatically trigered every 10 seconds 
Author        : Sutawijaya
Date          : 25/03/2013
*/


    //Twitter API 
    require 'app_tokensC1.php';
	require 'tmhOAuth.php';
	$tweetLookup      = 'time_zone';
	$numberOfRequest  = 50; //optimum throughput (server/network timeout consideration, API 1.1 limited only 180 request allowed for 15 minutes) 
	
    //ODBC Connection Properties
	$conn = odbc_connect($mysql_db, $mysql_user, $mysql_password);
    
	/* Used for multi channel processing
	
	$strQuery = "select * from  ChannelProcessing   where channel = '1'";
	$result   = odbc_exec($conn, $strQuery); 
    while(odbc_fetch_row($result)){
		$channel    = odbc_result($result, 1);
		$iteration  = odbc_result($result, 2);
		$thread     = odbc_result($result, 3);        		  		 
	}
	
	echo 'Number of Iteration: '.$iteration;
	$iteration = $iteration +1 ; 
	$strQuery = "update  ChannelProcessing   set iteration=".$iteration.", thread='".$thread."' where channel='"$channel."'";
	$result   = odbc_exec($conn, $strQuery);
	*/
	
	$strQuery = "select * from   " .$tableName. " where LocationProfile = '".$defaultLocation."'";
	$result   = odbc_exec($conn, $strQuery); 
    
 
    //Create Tweets Data Structure	
	$idxArray = 0;	
    while(odbc_fetch_row($result)){
		$date    = odbc_result($result, 1);
		$content = odbc_result($result, 6);
		$name    = odbc_result($result, 3);
        $statId  = odbc_result($result, 4);		
	   
	    $tweetData =  array($statId,$name,$defaultLocation); 
	    $tweetStructure[$idxArray] = $tweetData ;  
		   
		$idxArray ++;
		 
	}
	
	echo "Number of Records ".$idxArray."<br>";
    
	//Conecting to Twitter API 
	$connection = new tmhOAuth(array(
	  'consumer_key'    => $consumer_key,
	  'consumer_secret' => $consumer_secret,
	  'user_token'      => $user_token,
	  'user_secret'     => $user_secret
	));
	
	 
  
     echo "Start: ".date("H:i:s:u")."<br>";
	//GeoLocating based on Tweet Screen Name
	
	 
	for ($i=0;$i<$numberOfRequest;$i++){
	     //print  $tweetStructure[$i][0] . $tweetStructure[$i][1]  . $tweetStructure[$i][2]. "<br>";
		 $tweetAccountName = $tweetStructure[$i][1];
	     
		 $http_code = $connection->request('GET',$connection->url('1.1/users/show'), 
	                                  array('screen_name' => $tweetAccountName,'count' => 100));
									  
		//Search was successful
		 if ($http_code == 200) {
		
				// Extract the tweets from the API response
				$response = json_decode($connection->response['response'],true);
 
				$tweet_data = $response['location'];
  				$tweetStructure[$i][2] = $tweet_data;
				
				//print_r ($tweet_data);
				print "[".$i."]".$tweetStructure[$i][0].'--'.$tweetStructure[$i][1].'--'.$tweetStructure[$i][2];
				print "<br>";
 		
		// Handle errors from API request
		} 
		 
		else {
				if ($http_code == 429) {
				    //$tweetStructure[$i][2] = '429';
					$tweetStructure[$i][2] = $defaultLocation;
					print 'Error: Twitter API rate limit reached <BR>';
				} else {
				    //$tweetStructure[$i][2] =  '999';
					$tweetStructure[$i][2] = $defaultLocation;
					print $http_code.'Error: Twitter was not able to process that search <BR>';
				}
	    } 
									  
	}
	
	//Updating Geolocation on Table
	$numberofupdatedlocation = 0;
	$numberofdefaultedlocation = 0;
	for ($i=0;$i<$numberOfRequest;$i++){	
	     
	    $tweetLocation = $tweetStructure[$i][2];
		if ($tweetLocation == '' || $tweetLocation == $defaultLocation){$tweetLocation =$notfoundLocation;}
			
		$tweetLocation  = str_replace("'","",$tweetLocation );
		
		 if ($tweetStructure[$i][0] <> '') { 
		      $strQuery = "update ".$tableName." set LocationProfile = '".$tweetLocation."' where Status_Id='".$tweetStructure[$i][0]."'"; 
		 } 	
		 if ($tweetStructure[$i][1] <> '') {
		 		$strQuery = "update ".$tableName." set LocationProfile = '".$tweetLocation."' where Screen_Name='".$tweetStructure[$i][1]."'";
		 }
		 
		print "strquery==>:  ".$strQuery ."<br>";
		$result   = odbc_exec($conn, $strQuery);
		if ($tweetLocation != $notfoundLocation){
		  echo "[".$i."] Location Updated >>".$result."<br>";
		  $numberofupdatedlocation = $numberofupdatedlocation + 1;
		}else{
		  echo "[".$i."] Location Set to Default >>".$result."<br>";
		  $numberofdefaultedlocation = $numberofdefaultedlocation + 1;
		}
		
	}
 
	odbc_close($conn);	
	
	echo "End: ".date("r")."<br>";
	echo "Number of Tweets that has Location = ".$numberofupdatedlocation."<br>";
	echo "Number of Tweets that has No Location = ".$numberofdefaultedlocation."<br>";
    echo '</body></html>';
?>