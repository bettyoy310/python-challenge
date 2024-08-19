import os
import csv

csvpath = os.path.join(r"C:\Users\weiwei\python-challenge\Pybank\Resourses\budget_data.csv")

total_months = 0
net_total = 0
pre_profit = 0
changes = []
greatest_increase = {"date":"","amount": float('-inf')}
greatest_decrease = {"date":"","amount": float('inf')}

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    header = next(csvreader)

    first_row = next(csvreader)
    total_months = total_months +1
    net_total = net_total + int(first_row[1])
    pre_profit = int(first_row[1])


    for row in csvreader:
        total_months = total_months + 1
        net_total = net_total + int(row[1])

        change = int(row[1]) - pre_profit
        changes.append(change)
        pre_profit=int(row[1])


        if change > greatest_increase['amount']:
            greatest_increase['amount'] = change
            greatest_increase['date'] = row[0]
        

        if change < greatest_decrease['amount']:
            greatest_decrease['amount'] = change
            greatest_decrease['date'] = row[0]

    if len(changes) > 0:
        average_change = sum(changes) / len(changes)
    else:
        average_change = 0
        

print(f"The total months are {total_months} .")
print(f"The net total amount of Profit/Losses is ${net_total}.")
print(f"The average changes is ${average_change:.2f}")
print(f"The greatest increase in profits was on {greatest_increase['date']} (${greatest_increase['amount']}).")
print(f"The greatest decrease in profits was on {greatest_decrease['date']} (${greatest_decrease['amount']}).")

