import pandas as pd
import matplotlib.pyplot as plt
from datetime import date


today = str(date.today())
while True:
    choice = input("Add expense or quit? (a/q): ").lower()
    if choice == "q":
        break

    date = input("Enter Date (YYYY-MM-DD):")
    if date == "":
        date = today

    category= input("Enter Category:")
    amount= float(input("Enter the amount here:"))
    desc = str(input("Enter description: "))
    with open("expenses.csv",'a') as f:
        f.write(f"{date},{category},{amount},{desc}\n")
        print("✅ Expense added!")
    df = pd.read_csv("expenses.csv")
    totals = df.groupby("category")["amount"].sum()
    print("\n Totals so far: \n",totals)















#print("\n📊 All Expenses:\n", df)


#totals = df.groupby("category")["amount"].sum()

#print("\n💰 Total Spent per Category:\n",totals)

#plt.figure(figsize=(8,5))
#plt.bar(totals.index,totals.values)
#plt.title("Total Spending by category")
#plt.xlabel("Category")
#plt.ylabel("Amount (Omr)")
#plt.grid(axis="y", linestyle="--",alpha=0.7)
##plt.show()