from math import sqrt

x = []
y = []
xy = []
xy2 = []
x2 = []
y2 = []
setSize = int(input('how many x and y values do you have? :'))


def RegressionValues():
    initialValue = 1
    while initialValue <= setSize:
        x1 = float(input('Enter a x value: '))
        y1 = float(input('Enter a y value: '))

        xyValue = (x1*y1)

        x.append(x1)
        y.append(y1)
        xy.append(xyValue)
        xy2.append(xyValue**2)
        x2.append(x1**2)
        y2.append(y1**2)

        initialValue += 1


RegressionValues()

Ey = sum(y)
Ex = sum(x)
Exy = sum(xy)
Exy2 = sum(xy2)
Ex2 = sum(x2)
Ey2 = sum(y2)

print("Ex is", Ex)
print("Ey is", Ey)
print("Exy is", Exy)
print("Exy^2 is", Exy2)

xMean = Ex/setSize
yMean = Ey/setSize

aBar = ((Ex*Ey)-(setSize*Exy))/((Ex**2)-(setSize*Ex2))


bBar = ((Ex*Exy)-Ey*Ex2)/((Ex**2)-(setSize*Ex2))

Sx = sqrt((Ex2-((1/setSize)*(Ex**2)))/(setSize-1))
Sy = sqrt((Ey2-((1/setSize)*(Ey**2)))/(setSize-1))

r = (Sx/Sy)*aBar

print("a is : ", aBar)
print("b is : ", bBar)
print(" Co-efficient of Correlation r is : ", r)

print('y = ', aBar, 'x + ', bBar)

Equate = input('Do you want to find an value using the line? (y/n) : ')

if Equate == 'y':
    xOry = input('do you want to find the value of x or y? : ')
    if xOry == 'x':
        yValue = float(input('please enter the value of y : '))
        xValue = (yValue-bBar)/aBar
        print('Your x is : ', xValue)

    elif xOry == 'y':
        xValue = float(input('please enter your x value : '))
        yValue = (aBar*xValue) + bBar
        print('Your y value is : ', yValue)

    else:
        print('Please make sure you enter y or n specifically!')

print('Thank you!!')

#Copyright Tinashe Dzemwa
#Copyright Tinashe Dzemwa
#Copyright Tinashe Dzemwa