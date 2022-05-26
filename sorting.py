import csv
file = open("real-estate.csv")
csvreader = csv.reader(file)
filename = next(csvreader)
print(filename)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()



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

def printRows(rows):
    new_list=[]
    for row in range(len(rows)):
        new_list.append({rows[row].row: rows[row][1]})
    print(new_list)
mergeSort(rows)
printRows(rows)