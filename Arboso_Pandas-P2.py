

#import pandas library
import pandas as np

#load the .csv file into dataframe named cars
cars = pd.read_csv('cars.csv')

#print selected rows and column
print("A.
",cars.iloc[0:5:1,1::2])

#prints all the rows the the Model is "Mazda RX4"
print("B.
",cars.loc[cars['Model']=='Mazda RX4'])

#prints the cyl coloumn where the model is CamaroZ28
print("C.
",cars.loc[(cars['Model']=='Camaro Z28'),['cyl']])

#prints the cyl and gear coloumn for the 3 specific models
print("D.
",cars.loc[cars['Model']=='Mazda RX4 Wag',['cyl','gear']])
print(cars.loc[cars['Model']=='Ford Pantera L',['cyl','gear']])
print(cars.loc[cars['Model']=='Honda Civic',['cyl','gear']])

