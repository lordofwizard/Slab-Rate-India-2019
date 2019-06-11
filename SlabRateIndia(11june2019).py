inc = int(input(''' 
Hello WELCOME TO THE FIRST PROGRAMM TO CALCULATE THE SLAB RATE OF YOUR INCOME FOR FREE
DOC
HOW TO USE THE SOFTWARE 
* YOU JUST NEED TO ADD THE VALUE IN THE "> _" HERE FOR CALCULATING THE SLAB RATE 
IT'S SO SIMPLE AND EASY
SO INPUT YOUR VALUE HERE 
> '''))
if inc < 250000:
    print("Sorry your income is below '250000' and you don't have to pay any taxes")



elif inc >= 250000 and inc <= 500000:
        a =  (inc-250000)* 5/100     
        print(f"Your income tax is {a} RS")

elif 500000 < inc <= 1000000:
        b = 12500 + (inc-500000)*20/100        
        print(f"Your income tax is {b} RS")

elif inc > 1000000:
        z = 12500 + 100000 + (inc-1000000)*30/100
        print(f'Your income tax is {z}')




