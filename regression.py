x, y, xy, xy2, x2, y2 = [], [], [], [], [], []

class Number ():

    def __init__ (self, size=0, number=0):
        self.number = number
        self.size = size
    
    def square_root(self):
        emptyList = []
        i = 0.01
        max_number = 0

        while (i*i) <= self.number:
            emptyList.append(i)
            i += 0.01
            emptyList.sort()

            max_number = emptyList[0]

            for i in range(1, len(emptyList)):
                if emptyList[i] > max_number:
                    max_number = emptyList[i]

        return max_number

    def regression_values(self):
        initialValue = 1
        while initialValue <= self.size:
            x1 = int(input('Enter a x value: '))
            y1 = int(input('Enter a y value: '))

            xyValue = (x1*y1)

            x.append(x1)
            y.append(y1)
            xy.append(xyValue)
            xy2.append(xyValue**2)
            x2.append(x1**2)
            y2.append(y1**2)

            initialValue += 1


setSize = input('How many x and y values do you have?\n')
sizeValid = False

while sizeValid == False:
    try:
        setSize = int(setSize)
        sizeValid = True
    except:
        print('Please enter a valid string!\n')
        setSize = input('How many x and y values do you have?\n')


Number(setSize).regression_values()

Ey = sum(y)
Ex = sum(x)
Exy = sum(xy)
Exy2 = sum(xy2)
Ex2 = sum(x2)
Ey2 = sum(y2)

print("\nEx is",Ex, "\n")
print("\nEy is",Ey, "\n")
print("\nExy is",Exy, "\n")
print("\nExy^2 is",Exy2, "\n")

xMean = Ex/setSize
yMean = Ey/setSize

aBar = ((Ex*Ey)-(setSize*Exy))/((Ex**2)-(setSize*Ex2))
bBar = ((Ex*Exy)-Ey*Ex2)/((Ex**2)-(setSize*Ex2))

Sx = Number(setSize, ((Ex2)-((1/setSize)*(Ex**2)))/(setSize-1)).square_root()
Sy = Number(setSize, ((Ey2)-((1/setSize)*(Ey**2)))/(setSize-1)).square_root()

r = (Sx/Sy)*aBar


print("a is : ",aBar)
print("b is : ",bBar)
print(" Co-efficient of Correlation r is : ",r)