#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset = 86  DONE
#The net total amount of "Profit/Losses" over the entire period - $38382578  DONE
#Calculate the changes in "Profit/Losses" over the entire period, 
# then find the average of those changes - £-2315,12 DONE
#The greatest increase in profits (date and amount) over the entire period
#Feb-2012 ($1926159) DONE
#The greatest decrease in profits (date and amount) over the entire period
#Sep-2013 ($-2196167) DONE
#In addition, your final script should both print the analysis to the terminal 
# and export a text file with the results. - DONE 

import os
import csv

#set path for file
pyBank_csv = './Resources/budget_data.csv'

#create the lists
months_count=[]
profit_losses=[]
changes=[]

#open and read csv, split with commas 
with open(pyBank_csv, encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
    #print(csv_header)
    
    # 1 number of months are equal to number of lines, less one for the header
    for row in csv_reader:
        months_count.append(row[0])
        total_months = len(months_count)
    
    # 2 The net total amount of "Profit/Losses" over the entire period $38382578
        profit_losses.append(int(row[1]))
        total_amount=sum(profit_losses)

# print(f"£{total_amount}")
# print(total_months)

    # 3 Calculate the changes in "Profit/Losses" over the entire period, 
# then find the average of those changes - £-2315,12  DONE

#changes over the entire period
    
    for profits in range(len(profit_losses)-1):
        changes.append(profit_losses[profits+1]-profit_losses[profits])
        
        
    #average of changes - rounded to two decimals
    average_change = round(sum(changes)/len(changes),2)

    # 4 The greatest increase in profits (date and amount) over the entire period
#Feb-2012 ($1926159) DONE

greatest_increase = max(changes)
#print(greatest_increase)

max_month = changes.index(max(changes)) + 1

    # 5 The greatest decrease in profits (date and amount) over the entire period
#Sep-2013 ($-2196167)

greatest_decrease = min(changes)
#print(greatest_decrease)
min_month = changes.index(min(changes)) + 1

#In addition, your final script should both print the analysis to the terminal 


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: $ {average_change}")
print(f"Greatest Increase in Profits: {months_count[max_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {months_count[min_month]} (${(str(greatest_decrease))})")


# ----and export a text file with the results.
financial_analysis= './Analysis/Financial_Analysis.txt'
with open(financial_analysis, "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {total_months}")
    file.write("\n")
    file.write(f"Total: ${total_amount}")
    file.write("\n")
    file.write(f"Average Change: {average_change}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {months_count[max_month]} (${(str(greatest_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {months_count[min_month]} (${(str(greatest_decrease))})")