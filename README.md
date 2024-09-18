# ECE2112_PA3
# II. Instructions:

### For this programming assignment, download the following file and save to your default user folder:
http://bit.ly/Cars_file
![image](https://github.com/user-attachments/assets/c8b74db9-dc8c-49b4-a02b-c74b223215ba)

- Put the file the same folder as the Pa3

## PROBLEM 1: Save your file as Surname_Pandas-P1.py

a. Load the corresponding .csv file into a data frame named cars using pandas

b. Display the first five and last five rows of the resulting cars.

### Code:

#Put the codes into the string variable
code_problem_1 = """

#import pandas library
import pandas as pd
#load the .csv file into a data frame named cars
cars = pd.read_csv('cars.csv')
#print the first five rows of the resulting cars
print("First Five\n",cars.head())
#print the last five rows of the resulting cars
print("Last Five\n",cars.tail())
"""
#writing the code block to a python file 
file_1 = open('PA.3_Arboso.py','w')
file_1.write(code_problem_1)
#close the file
file_1.close()





## PROBLEM 2: Save your file as Surname_Pandas-P2.py
Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
indexing operations.

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4

Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.




