(1) As the Clerk, I should be able to insert a single record of working class hero into database via an API	 	 	 	 	 	 	 
							
Background: The application is running
When: The user run the test code
Then: It will ask User role 
And: The user enters the role
							 
Scenario: Insert a single record of working class hero							 
When: The user enters the role "1"							 
And: The user enters 1 for single insertion from the insert option							 
And: The user enters birthday "01012000"							 
And: The user enters gender "m"							 
And: The user enters name "XYZ"							 
And: The user enters natid "0011$"							 
And: The user enters salary "8000"							 
And: The user enters tax paid "500"							 
Then: The user sends a POST Request with "/calculator/insert" endpoint							 
And: The user will get a response code "202"							 
And: The user checks inserted data							 
 	 	 	 	 	 	 	 
							
(2) As the Clerk, I should be able to insert more than one working class hero into database via an API	 	 	 	 	 	 	 
							
Scenario: Insert more than one record of working class hero		
When: The user enters the role "1"		
And: The user enters 2 for single insertion from the insert option		
And: The user enters birthday "01012000"		
And: The user enters gender "m"		
And: The user enters name "XYZ"							
And: The user enters natid "0011$"							
And: The user enters salary "8000"							
And: The user enters tax paid "500"							
And: The user enters birthday "01012000"							
And: The user enters gender "m"							
And: The user enters name "ABC"							
And: The user enters natid "0111$"							
And: The user enters salary "8000"							
And: The user enters tax paid "500"							
Then: The user sends a POST Request with "/calculator/insertMultiple" endpoint							
And: The user will get a response code "202"							
And: The user checks inserted data							
					
							
(3) As the Clerk, I should be able to upload a csv file to a portal so that I can populate the database from a UI	 	 	 	 	 	 	 
							
Scenario: Upload a csv file							
When: The user enters the role "1"							
And: The user enters 3 to upload csv file with post request "/calculator/uploadLargeFileForInsertionToDatabase" 
endpoint							
Then: The user will get a response code "200"							
And: The user checks inserted data							
							
							
							
(4) As the Bookkeeper, I should be able to query the amount of tax relief for each person in the database so that I can
 report the figures to my Bookkeeping Manager							
							
Scenario: Checks the amount of tax relief for each person							
When: The user enters the role "2" with get request "/calculator/taxRelief" endpoint							
Then: The user checks natid, tax relief amount and name							
And The user verifies tax calculation							
And The user verifies tax calculation							
							
							
							
							
(5) As the Governor, I should be able to see a button on the screen so
that I can dispense tax relief for my working class heroes							
							
Scenario: Dispense relief							
When: The user opens the application							
Then: The user verifies the dispense button is red							
And: The text of the button is "“Dispense Now”"							
When: The user clicks on the dispense button							
Then: The user is redirected to another page							
And: The page contains "Cash dispensed"							
							




Functional Test:
   1.Need to which functionality of the product needs to be tested. This can be testing     main functions, messages, error conditions and product usability.
2.	Need to create input data for functionalities to be tested according to specified requirements.
3.	Determine acceptable output parameters according to specified requirements.
4.	Execute test cases and need to test repeatedly with different data
5.	Compare actual output from the test with the predetermined output values.
 
Non-Functional Test:
1.	Security
2.	Reliability
3.	Efficiency
4.	Usability
5.	Availability


Run Test:
Browse the .py file from command prompt and execute the test.
Please keep csv file in the same location of .py file
