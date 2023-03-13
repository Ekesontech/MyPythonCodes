## Checking if it's square or not ##


RecLength = int(input("Enter length of the rectangle> "))
RecBreadth = int(input("Enter breadth of the rectangle> "))
SquaLength = 8
SquaBreadth = 8
Square = (SquaLength * SquaBreadth)
if (RecLength * RecBreadth == Square):
    print("It is square")
else:
    print("it is not sqaure")