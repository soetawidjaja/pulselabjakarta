<?php
/*
Institution   : Global Pulse Lab Jakarta
Program name  : tweetFollower.php  
Decription    : list follower user X
Author        : Sutawijaya
Date          : 13/12/2013
*/


require 'app_tokensC1.php';
require 'tmhOAuth.php';

$connection = new tmhOAuth(array(
  'consumer_key'    => $consumer_key,
  'consumer_secret' => $consumer_secret,
  'user_token'      => $user_token,
  'user_secret'     => $user_secret
));

$tweetAccountName = 'anisanissa';

 
$http_code = $connection->request('GET',$connection->url('1.1/users/show'), 
	                               array('screen_name' => $tweetAccountName,
	                               'count' => 100));

 
    if ($http_code == 200) { 
		        		
				// Extract the tweets from the API response
				$response = json_decode($connection->response['response'],true);		 
				$tweet_data = $response['location'];
				
				print "user profile: " . $tweetAccountName . " <br>";
				print_r($response);
				
		        print  "<br><br>User Location     ==> " . $tweet_data ."<br>";
		        print          "User Followers    ==> " . $tweet_data = $response['followers_count'] ."<br>";
		        print          "User Following    ==> " . $tweet_data = $response['friends_count'] ."<br>";
		        
 		// Handle errors from API request
		} 
		 
		else {
		    
				if ($http_code == 429) {
 					print 'Error: Twitter API rate limit reached <BR>' + $http_code;
				} else {
 					print $http_code.'Error: Twitter was not able to process that search <BR>'+ $http_code;
				}
	    } 

    $http_code = $connection->request('GET',$connection->url('1.1/followers/list'), 
	                               array('screen_name' => $tweetAccountName,
	                               'cursor' => -1));

    if ($http_code == 200) { 
    	$response = json_decode($connection->response['response'],true);
    	//print_r($response);
    	
    	
 


    	foreach($response['users']as $item) {
    	    print "follower name/ID: ".$item['screen_name']. "/".$item['id']."<br>";
    	}
    	
    			 
    	$cursor = $response['next_cursor'];
    	print "<br> Next Cursor:  " . $cursor . "<br>";
 
        while ($cursor != '0' &&  $http_code == 200){
                $http_code = $connection->request('GET',$connection->url('1.1/followers/list'), 
	                               array('screen_name' => $tweetAccountName,
	                               'cursor' => $cursor));


	            if ($http_code == 200) { 
	                 $response = json_decode($connection->response['response'],true);
                    //print_r($response);
                        	foreach($response['users']as $item) {
    	                          print "follower name/ID: ".$item['screen_name']. "/".$item['id']."<br>";
                        	}
                    $cursor = $response['next_cursor'];	
                    print "<br> Next Cursor:  " . $cursor . "<br>";
                    	 	            
	            }else{ print "null --> " . $http_code;}                     	                                    
        } 
            	
    	
    }else{ print "fails outside loop --> " .$http_code ;}

?>