print("Reading the data in the csv")

import csv
file = open("real-estate.csv")
csvreader = csv.reader(file)
header = next(csvreader)
# print(header)
rows = []
for row in csvreader:
    rows.append(row)
# print(rows)
file.close()

print("Sorting the data in the csv:")

def mergeSort(rows):
    if len(rows) > 1:
        middle = len(rows)//2
        left = rows[:middle]
        right =  rows[middle:]

        mergeSort(left)
        mergeSort(right)

        i =j =k =0
        while i < len(left) and j <len(right):
            if left[i][1] < right[j][1]:
                rows[k]= left[i]
                i+=1
            else:
                rows[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            rows[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            rows[k] = right[j]
            j+=1
            k+=1

print(rows)
mergeSort(rows)
print("Writing back to the CSV")
filename = 'real-estate.csv'
with open(filename, 'w', newline="") as csvfile:
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(header) 
    csvwriter.writerows(rows) 
    print(header)