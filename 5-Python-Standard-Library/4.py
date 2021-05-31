import csv

# with open("data.csv", "w") as file:
#     reader = csv.writer(file)
#     reader.writerow(["trasaction_id", "product_id", "price"])
#     reader.writerow([1000, 1, 5])
#     reader.writerow([1001, 2, 15])

with open("data.csv") as file:
    reader = csv.reader(file)
    print(list(reader))
    # when you convert the reader to list, the index will be moved from beginning of file to the end, that's why you can't iterate this reader twice which means you can't iterate like you're doing in next line, so needa comment out this code

    for row in reader:
        print(row)
