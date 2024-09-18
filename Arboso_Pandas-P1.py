

#import pandas library
import pandas as pd
#load the .csv file into a data frame named cars
cars = pd.read_csv('cars.csv')
#print the first five rows of the resulting cars
print("First Five
",cars.head())
#print the last five rows of the resulting cars
print("Last Five
",cars.tail())
