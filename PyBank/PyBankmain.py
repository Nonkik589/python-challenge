import os
import csv
from statistics import mean

#Opening the CSV File
path = os.path.abspath(os.path.dirname(__file__))
csvpath = os.path.join(path, "../Data/budget_data.csv")

#Initializing the Variables
row_total = 0

total_profit = 0

minmax_store = []


#Reading the file and Grabbing Important Info
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)
    #print(f"Budget Data Header: {csv_header}")

    
    for row in csvreader:
        #print(row[0])

        row_total += 1
        total_profit += int(row[1])

        minmax_store.append(int(row[1]))


avg =  round(mean(minmax_store))
Minimum = min(minmax_store)    
Maximum = max(minmax_store)


print(f'There are {row_total} months of data')
print(f'The total profit is: ${total_profit}')
print(f'The Average profit is: ${avg}')
print(f'The Max Profit is: ${Maximum}')
print(f'The Min Profit is: ${Minimum}')

csvoutput = [row_total, total_profit, avg, Minimum, Maximum]


output_path = os.path.join(path, "../Analysis/PyBankAnalysis" )

with open (output_path, 'w') as af:
    
    afwriter = csv.writer(af, delimiter=' ')
   
    afwriter.writerow(['Total Months', 'Total Profit', 'Average Profit', 'Max', 'Min'])
    afwriter.writerow('-----------------------------------------------------------------------')
    afwriter.writerow([csvoutput])



        