# Store the file path associated with the file
import os
import csv 
#budget_data = os.path.join('..', 'Resources', 'budget_data.csv')
budget_data = os.path.join('C:/Users/17639/Desktop/Python-challenge/PyBank/Resources/budget_data.csv')

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

output = os.path.join('C:/Users/17639/Documents/ARCC/UVM Bootcamp/Courses support/Activity 3/Python-challenge/PyBank/Resources/Financial_analysis.txt')
with open(output, "w") as txt_file:
    Financial_analysis = (
        f"\n\nFinancial analysis\n"
        f"----------------------\n"
        f"Total mounths: {str(len(budget_data))}\n"
        )
    
    print(Financial_analysis)

    txt_file.write(Financial_analysis)

#Set a new List to store a new line of data
    numbers = []
    for x in range(0,86):
        y=int(budget_data[x][-1])
        numbers.append(y)
    numbers_data = list(numbers)
# calculate the sum of the numbers
    sum = sum(numbers_data)
    sum_output = f"Total: ${str(sum)}\n"
    print(sum_output)
    txt_file.write(sum_output)

#Set the average variable
    global_change = int(budget_data[85][-1]) - int(budget_data[0][-1])
    average = global_change/85
    average_output = f"average_change: ${str(average)}\n"
    print (average_output)
    txt_file.write(average_output)
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
    greatest_increase_output = f"Greatest Increase in Profits: $({str(greatest_increase)})\n"
    greatest_decrease_output = f"Greatest Decrease in profits: $({str(greatest_decrease)})\n"
    print(greatest_increase_output)
    print(greatest_decrease_output)

    txt_file.write(greatest_increase_output)
    txt_file.write(greatest_decrease_output)
