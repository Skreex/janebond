# we can programmatically read data from an xlsx file using pandas
# then take the data for each record in the xlsx file
# open up the web browser to the entry form page -- 
# locate the proper input fields, and 'type' the values
# from the stashed record into the form's fields
#
#
# things to consider with this strategy though:
# 1. The excel file changing names or orders of columns
# 2. learning the limitations of pandas / selenium
# 3. The TIME it takes to input data into the form and submit it
# 4. Accounting for the time it takes to input that data into the form before reloading the page
#		and submitting a new record


import pandas as pd
from selenium import webdriver

#open the xlsx file
xlsx = pd.ExcelFile(#PATH/TO/EXCEL/FILE)

#get the first sheet as an object
sheet1 = xlsx.parse(0)

#get the first column as a list you can loop through
column = sheet1.icol(0).real

#get the first row as a list you can loop through
row = sheet1.irow(0).real



driver = webdriver.Chrome()

driver.get(#Insert website URL here)

# ways of locating a form label

#example html
# <html>
# 	<body>
# 		<form id="entryForm">
# 			<input name="username" type="text" />
# 			<input name="password" type="password" />
# 			<input name="continue" type="submit" value="Login" />
# 			...
# 		</form>
# 	</body>
# </html>


entry_form = driver.find_element_by_xpath("//form[@id='loginform']")
#or entry_form = driver.find_element_by_xpath("//form[1]")

#elements under the form id can be identified like so

username = driver.find_element_by_xpath("//input[@name='username']")
#or username = driver.find_element_by_xpath("form[@id='entryForm']/input[1]")
#or username = driver.find_element_by_xpath("//form[input/@name='username']")



