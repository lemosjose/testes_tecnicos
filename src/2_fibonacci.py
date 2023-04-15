import typing 
import math 

def fibonnaci_detector(input: float) -> None:
    A1 = 5*((input)**2) + 4
    A2 = 5*((input)**2) -4
    B1 = math.sqrt(A1)
    B2 = math.sqrt(A2)
    if ( (B1*B1) == A1) or ( (B2*B2) == A2):
        print("esse número está na sequência de fibonnaci")
        SystemExit()
    else:
        print("esse número não está na sequência de fibonnaci")




userInput = float(input("Digite um número a ser consultado na sequência de fibonnaci "))
fibonnaci_detector(userInput)
