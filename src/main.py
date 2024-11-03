#Main file for neural networking.
import sys
sys.path.append("../lib/")
import lib_math as math_lib

def main():
   print("This is the main function. \n")
   math_lib.fib(35)
   test = math_lib.fib2(35)
   print(test)

if __name__ == "__main__":
   main()