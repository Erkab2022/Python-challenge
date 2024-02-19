# Store the file path associated with the file
import os
import csv 
#budget_data = os.path.join('..','Resources','budget_data.csv')
budget_data = os.path.join('C:/Users/17639/Documents/ARCC/UVM Bootcamp/Courses support/Activity 3/Python challenge/Starter_Code/PyBank/Resources/budget_data.csv')

#Create Lists to store data
Date = []
Profit_Losses = []

#Open the csv file
with open(budget_data) as csvfile:
    csvreader=csv.reader(csvfile,delimiter = ',')
    #Skip the header
    next(csvreader,None)
    for row in csvreader:
        Date.append(row[0])
        Profit_Losses.append(row[1])

#Zip lists together
budget_data = list(zip(Date,Profit_Losses))

print("Financial analysis")
print("----------------------")
print(f'{"Total mounths: " + str(len(budget_data))}')

#Set a new List to store a new line of data
numbers = []
for x in range(0,86):
    y=int(budget_data[x][-1])
    numbers.append(y)
numbers_data = list(numbers)
# calculate the sum of the numbers
sum = sum(numbers_data)
print(f'{"Total: $"+ str(sum)}')

#Set the average variable
global_change = int(budget_data[85][-1]) - int(budget_data[0][-1])
average = global_change/85
print (f'{"average_change: $" + str(average)}')

#Retrieve the greatest increase and decrease 
#Define the values to compare
#Set a new list to store the data
value_data = []
for i in range(0,85):
    for each_row in budget_data:
        value_1 = int(budget_data[i][-1])
        value_2 = int(budget_data[(i)+1][-1])
        value = value_2-value_1
        #Add a new row
        value_data.append(value)
value_data_set = list(value_data)
greatest_increase = max(value_data_set)
greatest_decrease = min(value_data_set)
print(f'{"Greatest Increase in Profits: $" + "(" + str(greatest_increase) + ")"}')
print(f'{"Greatest Decrease in profits: $" + "(" + str(greatest_decrease) + ")"}')
