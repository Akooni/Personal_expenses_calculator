import pandas as pd
import matplotlib.pyplot as plt
from datetime import date


today = str(date.today())
while True:
    choice = input("Add expense or quit? (add/quit/today): ").lower()
    if choice == "add":
        date = input("Enter Date (YYYY-MM-DD):")
        if date == "":
            date = today

        category= input("Enter Category:")

        #To make the app solid and don't break when faced with a str
        while True:
            try:
                amount= float(input("Enter the amount here:"))
                break
            except ValueError:
              print("Please enter a number, not text 🙂")

        desc = str(input("Enter description: "))
        with open("expenses.csv",'a') as f:
            f.write(f"{date},{category},{amount},{desc}\n")
            print("✅ Expense added!")
        df = pd.read_csv("expenses.csv")
        # to show to amount in ascending order
        totals = (
             df.groupby("category")["amount"]
             .sum()
             .sort_values(ascending=False)
        )


        print("\n 💰 Totals so far: \n")
        #loop to show OMR in each amount
        for category,amount in totals.items():
            print(f"{category:<15} OMR {amount:,.2f}")


    elif choice =="today":
        df = pd.read_csv("expenses.csv")
        today_rows = df[df["date"] == today]
        today_total = today_rows["amount"].sum()
        print(f"🕒 Today’s spending: OMR {today_total:,.2f}")
        


    elif choice == "quit":
        break

    else:
        print("Please Enter a number here not a Text :) ")

   














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