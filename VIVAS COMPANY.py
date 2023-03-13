

# VIVAS COMPANY OFFERING 5% TO ALL WORKERS WHO HAVE WORKED FOR OVER 5 YEARS #

Name = input("Enter your name> ")
print("Hello", Name)
Salary = int(input("Enter your salary?> "))
YearsOfService = int(input("Enter years of service?> "))
Bonus = 0.005
QualifyForBonus = (YearsOfService > 5)
NetBonusAmt = (QualifyForBonus, Salary * Bonus)
if YearsOfService > 5:
    print(NetBonusAmt)
else:
    print("We are sorry, you don not qualify for the bonus")


