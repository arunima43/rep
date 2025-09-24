numb=int(input("Enter your first number:"))#User input
'''
Main funtion
'''
def main():
       def evenodd():
            if numb%2==0:
                print("It is an even number")
            else:
                print("It is an odd number")
            #This is to check even and odd
       evenodd()
       def positivenegetive():
            if numb>0:
                print("It is positive")
            else:
                print("It is a negetive number")
            #This is to check if its posotive or negetive
       positivenegetive()
       def square():
            print("Square of",numb,"is:",numb*numb)
            #This prints the square
       square()
       def cube():
            print("Cube of",numb,"is",numb*numb*numb)
            #This prints the cube
       cube()
main()
#End program