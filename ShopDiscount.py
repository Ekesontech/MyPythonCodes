## Shop discount ##

CostPerUnit = 100
Discount = 10/100
QtyPur = int(input("Enter Quantity purchased here> "))
TotalCost = (CostPerUnit * QtyPur)
if QtyPur > 10:
    print(TotalCost - Discount)
else:
    if QtyPur <=10:
        print(TotalCost)
