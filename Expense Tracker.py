print("\n$$ Welcome to Expense Tracker $$\n")
print("======= Menu =======")
print("1. Add Expense")
print("2. View All Expense")
print("3. View Total Spending")
print("4. Exit")
print("\n======================\n")
expense_list=[]
while True:
    choice=int(input("Enter your choice (1-4) : "))
    if(choice==1):
        date=input("Enter date (DD-MM-YYYY) : ")
        category=input("Enter Category (Food, Travel, Shopping, etc) : ")
        description=input("Enter short description : ")
        amount=input("Enter amount : ")
        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }
        expense_list.append(expense)
        print("\n✅ Expense added successfully!\n")
    elif(choice==2):
        if(len(expense_list)==0):
            print("\n⚠ No expense recorded yet")
        else:
            print("\n--- All Expenses ---")
            i=1
            for e in expense_list:
                print(f"{i}. {e['date']} | {e['category']} | {e['description']} | {e['amount']}")
                i += 1
            print("\n--------------------------\n")
    elif(choice==3):
        total=0
        for e in expense_list:
            total = total+int(e['amount'])
        print(f"\n Total Spending = {total}\n")
    elif(choice==4):
        print("\n🖐Thanks for using Expense Tracker! Bye!")
        break
    else:
        print("\n❎Invalid Choice. Please try again.")