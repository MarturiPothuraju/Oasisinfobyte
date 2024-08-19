class node:
    height=None
    weight=None
    category=None
    next_node=None
    def __init__(self,h,w,c):
        self.height=h
        self.weight=w
        self.category=c
class bmi_class:
    start_node=None
    def insert_node(self,h,w,c):
        a1=node(h,w,c)
        if(self.start_node==None):
            self.start_node=a1
        else:
            b=self.start_node
            a1.next_node=b
            self.start_node=a1
    def disp(self):
        temp=self.start_node
        print("_"*50)
        print("height(m)\tweight(kg)\tcategory")
        print("---------\t----------\t--------")
        while True:
            print(temp.height,end="\t\t")
            print(temp.weight,end="\t\t")
            print(temp.category,end="\n")
            if(temp.next_node==None):
                break
            temp=temp.next_node
        print("_"*50)
    def bmi_calc(self):
        hei=float(input('enter the height in meters: '))
        wei=float(input('enter the weight in kilograms: '))
        bmi=wei/(hei*hei)
        c=None
        print("-"*50)
        if(bmi<18.5):
            print('your in underweight')
            c="underweight"
        elif(18.5<=bmi and bmi<=24.9):
            print('your in normal weight')
            c="normal"
        elif(25<=bmi and bmi<=29.9):
            print('your in overweight')
            c="overweight"
        elif(30<=bmi and bmi<=34.9):
            print('your in class-1 obesity')
            c="class-1 obesity"
        elif(35<=bmi and bmi<=39.9):
            print('your in class-2 obesity')
            c="class-2 obesity"
        elif(bmi>=40):
            print('your in class-3 obesity')
            c="class-3 obesity"
        print("-"*50)
        self.insert_node(hei,wei,c)
        
sll=bmi_class()
print(":"*50)
print("1:calculate BMI \n2:show history \n3:exit from program")
print(":"*50)
while True:
    x=int(input("enter the option :"))
    match x:
        case(1):
            sll.bmi_calc()
        case(2):
            sll.disp()3
        case(3):
            break
