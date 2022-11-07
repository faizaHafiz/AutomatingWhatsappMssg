# AutomatingWhatsappMssg
For a system where we need to send personalised bulk messages to our customer, typing each message and sending them one by one becomes a repetitive and hectic task. For this purpose a simple python script can automate this task.
We all use excel sheets to store customer details. Using this excel sheet one can extract data from it and use it in python.
In this article we are going to extract numbers and respective marks of each candidate and send their marks to their parents on whatsApp.

Before running the above code make sure you have  all the packages installed. 

I have created a marks.csv file in which i have stored these data with Parents_no in the format +910000000000 i.e. adding a plus sign and a country code as whatsApp will use this number to send the message.
rollno	Name	Parents_no	Self_no	Physics	Chemistry	Maths	Biology

The element_presence function searches for the chatbox in our whatsApp web using xpath (You can write it outside of function as well). To copy xpath open whatsapp web, inspect the page and select the chatbox where you type your message to inspect it. 
After getting the code of the chatbox, right click on the code and select copy xpath. After copying, come to the python code and paste it in the code.
send_message function sends the message using the url passed to the function.
chrome_options is given for the purpose of not asking the Qr code again and again.

We are saving the excel sheet as csv file so that we can easily traverse through the file and parse through each row one by one using for loop.
Any suggestions are welcome. Thankyou.
