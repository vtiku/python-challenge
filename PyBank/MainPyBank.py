#Script for PyBank 
# Import the necessary dependencies for os.path.join()
import os
import csv

#read in a .csv file
csv_file = os.path.join("Resources", "budget_data.csv")

#create lists
date = []
profit_loss = []
change = []

#initialize variables
month_count=0
total=0
average_change=0
prior_profit=0
total_change=0
increase={"month": "", "profit_loss": 0}
decrease={"month": "", "profit_loss": 0}

# open csv as Reader
with open(csv_file) as csv_bank:
    csv_reader=csv.reader(csv_bank, delimiter=",")
    csv_header=next(csv_reader)
    print(f"Header:{csv_header}")

    #required tasks create a Python script that analyzes the records to calculate each of the following values:

    #The total number of months included in the dataset
    for row in csv_reader:
        month_count +=1
        total +=int(row[1])
        #The net total amount of "Profit/Losses" over the entire period
        date.append(row[0])
        profit = int(row[1])
        profit_loss.append(profit)
        #The changes in "Profit/Losses" over the entire period, and then the average of those changes
        pl=0
        if prior_profit != 0:
            pl = profit - prior_profit
            change.append(pl)
        prior_profit = profit
        
        #The greatest increase in profits (date and amount) over the entire period
        if pl > increase['profit_loss']:
            increase['profit_loss'] = pl
            increase['month'] = row[0]
        
        #The greatest decrease in profits (date and amount) over the entire period
        if pl < decrease['profit_loss']:
            decrease['profit_loss'] = pl
            decrease['month'] = row[0]

average_change = sum(change) / len(change)




print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase['month']} ${increase['profit_loss']}")
print(f"Greatest Decrease in Profits: {decrease['month']} ${decrease['profit_loss']}")


