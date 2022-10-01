from audioop import avg
from calendar import month
import os
import csv

#write to txt file
with open('Analysis/PyBank_Financial_Analysis.txt', 'w') as f:

    #open and read csv
    pybank_csv = os.path.join("Resources", "budget_data.csv")

    #initiate global variables
    total_months = 0
    net_total = 0
    count = 0 
    month_list = []
    profit_list = []
    pl_list=[]
    combined_month_pl_list = []

    # Open and read csv
    with open(pybank_csv) as csv_file:
        csv_reader = csv.DictReader(csv_file)
    
        #creating columns into python lists  
        for row in csv_reader:
            if count == 0:
                profit_list.append(int(row['Profit/Losses']))
                month_list.append(row['Date'])
            else:
                profit_list.append(int(row['Profit/Losses']))
                month_list.append(row['Date'])
                #this is the difference between the current row and previous row
                diff = int(row['Profit/Losses']) - profit_list[count-1] 
                pl_list.append(diff)
            count = count+1

    # print(profit_list)
    # print(month_list)
    # print(pl_list)
                  
    #trying to find the average of a list, I made a function
    def Average(list):
        total_of_items = sum(list)
        list_length = len(list)
        average_pl = (total_of_items / list_length)
        return average_pl

    #to find the average change of the list, I perform the function I created.    
    average_change = Average(pl_list)
    #round average change and add formatting
    rounded_average = str("${:,.2f}". format(average_change, 2))
    # print(f"Average Change: {(rounded_average)}")
    #to find the greatest decrease:
    min_value=min(pl_list)
    #add formatting
    money_min = ("${:.0f}". format(min_value))
    # print(f"Greatest Decrease In Profits: {money_min}.")
    #to find the greatest increase:
    max_value=max(pl_list)
    #add formatting
    money_max = ("${:.0f}". format(max_value))
    # print(f"Greatest Increase In Profits: {money_max}.")
   
    #count total months
    total_months = len(month_list)
    #sum net total from "Profit/Losses"
    net_total = sum(profit_list) 
    #add formatting
    money_net=("${:.0f}". format(net_total))
    #add months associated with the greatest increase/decrease values
    #turns it into the index of the value accessed
    max_index = pl_list.index(max_value)
    max_month = (month_list[max_index + 1])
    min_index = pl_list.index(min_value)
    min_month = (month_list[min_index + 1])

                
    #formatting for final print
    print("Financial Analysis")
    print("----------------------------")      
    print(f"Total Months: {total_months}")
    print(f"Total: {money_net}")
    print(f"Average Change: {(rounded_average)}")
    print(f"Greatest Increase In Profits: {max_month} ({money_max}).")
    print(f"Greatest Decrease In Profits: {min_month} ({money_min}).")
    print("----------------------------")
    
    #write to txt file:
    f.write("\n")  
    f.write("Financial Analysis")
    f.write("\n")  
    f.write("----------------------------") 
    f.write("\n")       
    f.write(f"Total Months: {total_months}")
    f.write("\n")  
    f.write(f"Total: {money_net}")
    f.write("\n")  
    f.write(f"Average Change: {(rounded_average)}")
    f.write("\n")  
    f.write(f"Greatest Increase In Profits: {max_month} ({money_max}).")
    f.write("\n")  
    f.write(f"Greatest Decrease In Profits: {min_month} ({money_min}).")
    f.write("\n")  
    f.write("----------------------------")

        