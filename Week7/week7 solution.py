 #Create CSV file for product selling for 6 Months ( Prod_No | Prod_Name | Jan | Feb | Mar | Apr | May | Jun) for 5 products.

import csv
import pandas as pd
header=['Prod_No','Prod_Name','Jan','Feb','Mar','Apr','May','Jun']
with open("C:\\sqlite3\\csv\\selling.csv","w",newline='') as csvfile:
    data=csv.writer(csvfile)
    data.writerow(header)

#1)Add 12 Records. by taking input from user.

l=[]
with open("c:\\sqlite3\\csv\\selling.csv",'a',newline="") as file:
    insert =csv. writer(file)
    for i in range(12):
        prod_no = input("Enter Product Number: ")
        prod_name = input("Enter Product Name: ")
        jan = int(input("Enter January Sales: "))
        feb = int(input("Enter February Sales: "))
        mar = int(input("Enter March Sales: "))
        apr = int(input("Enter April Sales: "))
        may = int(input("Enter May Sales: "))
        jun = int(input("Enter June Sales: "))
        data=[prod_no,prod_name,jan,feb,mar,apr,may,jun]
        l.append(data)
    insert.writerows(l)

#2)Change Column Name Product No, Product Name, January, February, March, April, May, June.

df=pd.header=['Product_NO','Product_Name','January','February','March','April','May',' June']
print(df)

#3)Add column "Total Sell" to count total of all month and "Average Sell"

header=['Product_NO','Product_Name','January','February','March','April','May',' June']
df=pd.read_csv("c:\\sqlite3\\csv\\product_selling.csv")
row=df.values.tolist()
total=[sum(i[2::]) for i in row]
average=[int(sum(i[2::])/6) for i in row]

df = pd.DataFrame(row,columns=header)
df['Total']=total
df['Average']=average

print(df)

#4)Add 2 row at the end.

new_rows = {'Product No': '', 'Product Name': '', 'January': '', 'February': '', 'March': '', 'April': '', 'May': '', 'June': ''}
for i in range(2):
    for column in new_rows:
        new_rows[column] = input(f"Enter value for {column}: ")
df = df.append(new_rows, ignore_index=True)
df.reset_index(drop=True, inplace=True)

#5)add 2 row after 3rd row

header=['Product No', 'Product Name', 'January', 'February', 'March', 'April', 'May', 'June','Total','Average']
df.loc[2.5] = [15, 'cable',1290,7128,7456,4325,3874,2002,26075,4345.8333333]
df = df.sort_index().reset_index(drop=True)
df.loc[3.5] = [16, 'projecter',1140,1148,2260,2245,2256,2221,11270,1878.333333]
df = df.sort_index().reset_index(drop=True)

#6)Print first 5 row.

print("FIRST FIVE ROWS")
print(df.head())

#7)Print Last 5 row.
print("LAST 5 ROWS")
print(df.tail())

#8)Print row 6 to 10.
print("ROW BETWEEN 6 TO 10")
print(df.loc[6:10])

#9)Print only product name.
print(df["Product Name"])

#10)Print sell of January month with product id and product name.
print(df[["Product No", "Product Name", "January"]])

#11)Print only those product id , product name where january sell is > 5000 and February sell is >8000
print(" record based on condition")
df["January"] = pd.to_numeric(df["January"])
df["February"] = pd.to_numeric(df["February"])

df2 = df[(df["January"] > 5000) & (df["February"] > 8000)]

print(df2[["Product No", "Product Name"]])

#12)Print record in sorting order of Product name.
print(df.sort_values(by="Product Name"))

#13) Display only odd index number column record.
print("odd rows")
print(df.iloc[1::2])
print("even row")

#14)Display alternate row.
print(df.iloc[::2])
