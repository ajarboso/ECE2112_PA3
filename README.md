# ECE2112_PA3
# II. Instructions:

### For this programming assignment, download the following file and save to your default user folder: http://bit.ly/Cars_file

![image](https://github.com/user-attachments/assets/c8b74db9-dc8c-49b4-a02b-c74b223215ba)

- Put the file the same folder as the Pa3

## PROBLEM 1: Save your file as Surname_Pandas-P1.py

a. Load the corresponding .csv file into a data frame named cars using pandas

b. Display the first five and last five rows of the resulting cars.

### Code:

```#Put the codes into the string variable
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
```


For Question A: The code uses pd.read_csv() to load the contents of cars.csv into a DataFrame named cars.
```cars = pd.read_csv('cars.csv')```

- Displaying First 5 Rows: The method **cars.head()** is used to display the first 5 rows of the DataFrame.

```print("First Five\n",cars.head())```

  Output:
  
Frist Five:

![image](https://github.com/user-attachments/assets/2c511943-b153-4c73-82f9-c1ea5ef2576d)


- Displaying Last 5 Rows: Similarly, **cars.tail()** is used to show the last 5 rows of the DataFrame.

```print("Last Five\n",cars.tail())```

  Last Five:

  ![image](https://github.com/user-attachments/assets/6431e9a6-8690-4503-89cd-4427abc28005)


  


## PROBLEM 2: Save your file as Surname_Pandas-P2.py
Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
indexing operations.

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

Code:

```
#Put the codes into string variable
code_problem_2 = """

#import pandas library
import pandas as np

#load the .csv file into dataframe named cars
cars = pd.read_csv('cars.csv')

#print selected rows and column
print("A.\n",cars.iloc[0:5:1,1::2])

#prints all the rows the the Model is "Mazda RX4"
print("B.\n",cars.loc[cars['Model']=='Mazda RX4'])

#prints the cyl coloumn where the model is CamaroZ28
print("C.\n",cars.loc[(cars['Model']=='Camaro Z28'),['cyl']])

#prints the cyl and gear coloumn for the 3 specific models
print("D.\n",cars.loc[cars['Model']=='Mazda RX4 Wag',['cyl','gear']])
print(cars.loc[cars['Model']=='Ford Pantera L',['cyl','gear']])
print(cars.loc[cars['Model']=='Honda Civic',['cyl','gear']])

"""
# Writes those code into python file
file_2 = open('PA.3_Arboso.py','w')
file_2.write(code_problem_2)
# Closed the file
file_2.close()
```

For Question A: 

```print("A.\n",cars.iloc[0:5:1,1::2])```

Select and print specific rows and columns using .iloc. Here, it extracts a slice of the DataFrame, selecting rows 0 through 5, and columns starting from the second column while skipping every other column so you can get the odd numbers.

Output:

![image](https://github.com/user-attachments/assets/efdcf5b0-9df1-434a-8d26-e8c1c450c0ed)


For Questions B-D: These sections use the .loc method to filter the data based on specific conditions in the Model column.


B. Retrieves all rows where the car model is Mazda RX4.

![image](https://github.com/user-attachments/assets/6959d8f2-fdb4-46d9-b1e3-0e4dc7e8a2b9)


C. Displays only the cyl (number of cylinders) column for the Camaro Z28 model.

![image](https://github.com/user-attachments/assets/a8c3d7f2-9a3e-491f-81cf-c112ef75928f)


D. Displays both the cyl and gear columns for car models such as Mazda RX4 Wag, Ford Pantera L, and Honda Civic

```print("D.\n",cars.loc[cars['Model']=='Mazda RX4 Wag',['cyl','gear']])```

![image](https://github.com/user-attachments/assets/2030a971-3073-4619-8860-ce6301e73d9e)

```print(cars.loc[cars['Model']=='Ford Pantera L',['cyl','gear']])```

![image](https://github.com/user-attachments/assets/fa260115-6efe-4501-8cdf-003e96ee88ac)

```print(cars.loc[cars['Model']=='Honda Civic',['cyl','gear']])```

![image](https://github.com/user-attachments/assets/0fcb7b0f-42b2-49c8-bac4-482e9e518c19)


#### For Saving as a python file For problem 1 and 2

- Let's have problem 2 for example
  
- ```code_problem_2 = """``` The whole code will be save to the string variable code_problem_2
  
- ```file_2 = open('Arboso_Pandas-P2.py','w') file_2.write(code_problem_2)``` it will open a python file then writes it to the given strings
  
- ```file_2.close()``` Then closed the file to be saved.






