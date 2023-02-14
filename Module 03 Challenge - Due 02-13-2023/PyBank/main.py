# import os module for operating system and file handling function
import os

# import module for csv files
import csv

# use os.path.join to form a path to the csv file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

print("Financial Analysis")
print('-------------------')

# declare variables
totalMonths = 0 #row count
totalRevenue = 0 
revenue = []
previousRevenue = 0
month_of_change = []
revenueChange = 0
greatestDecrease = ["", 9999999]
greatestIncrease = ["", 0]
revenue_change_list = []
revenueAverage = 0

# use the with open() function to open the budget_data_csv into an object csvFile
with open(budget_data_csv) as csvFile:

      # csv module .reader() function specifies the delimiter and the object name for the reader in the open() function
      csvReader = csv.reader(csvFile, delimiter=",")

      # skip header so not included in count
      header = next(csvReader)

# find total months
 
      for row in csvReader:

        # get count for total months
        totalMonths += 1
        print(totalMonths)

        #get total revenue over the entire time span
        totalRevenue = totalRevenue + int(row[1])

        #get change in revenue 
        revenueChange = float(row[1])- previousRevenue
        previousRevenue = float(row[1])
        revenue_change_list = revenue_change_list + [revenueChange]
        month_of_change = [month_of_change] + [row[0]]
       

        #use if statement to find increase and decrease in revenue over entire time span
        if revenueChange > greatestIncrease[1]:
            greatestIncrease[1]= revenueChange
            greatestIncrease[0] = row[0]

        if revenueChange < greatestDecrease[1]:
            greatestDecrease[1]= revenueChange
            greatestDecrease[0] = row[0]

revenueAverage = sum(revenue_change_list)/len(revenue_change_list)

# create output

with open("financialanalysis.text", "w") as f
f.write("Financial Analysis\n")
f.write("---------------------\n")
f.write("Total Months: %d\n" % totalMonths)
f.write("Total Revenue: $%d\n" % totalRevenue)
f.write("Average Revenue Change $%d\n" % revenueAverage)
f.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatestIncrease[0], greatestIncrease[1]))
f.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatestDecrease[0], greatestDecrease[1]))

  
   
