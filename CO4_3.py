"""Create a class Rectangle with private attributes length and width. Overload ‘<’ operator
to compare the area of 2 rectangles."""


class Reactangle:
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
    
    def area(self):
        return self.length*self.bredth

    def __lt__(self,obj):


    

if __name__=='__main__':
    rectangle1_length=int(input("rectangle1_length  :"))
    rectangle1_bredth=int(input("rectangle1_bredth  :"))

    rectangle2_length=int(input("rectangle2_length   :"))
    rectangle2_bredth=int(input("rectangle2_bredth   :"))

    rectangle_obj1=Reactangle(rectangle1_length,rectangle1_bredth)
    rectangle_obj2=Reactangle(rectangle2_length,rectangle2_bredth)

    if rectangle_obj1.area()==rectangle_obj2.area():
        print("Both having same area")
    else:
        if rectangle_obj1.area()>rectangle_obj2.area():
            print("Rectangle1's area is greater")
        else:
            print("Rectangle2's area is greater")

