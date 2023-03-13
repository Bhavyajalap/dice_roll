# firstly we import the liberary random module

import random

#defining the function to create the design of the faces of dice

def DICE_ART(i):
    if i == 1:
        print("┌─────────┐"),
        print("│         │"),
        print("│    *    │"),
        print("│         │"),
        print("└─────────┘"),
    
    elif i == 2:
        print("┌─────────┐"),
        print("│  *      │"),
        print("│         │"),
        print("│      *  │"),
        print("└─────────┘"),
        
    
    elif i == 3:
        print("┌─────────┐"),
        print("│ *       │"),
        print("│    *    │"),
        print("│       * │"),
        print("└─────────┘"),
    elif i == 4: 
        print("┌─────────┐"),
        print("│ *     * │"),
        print("│         │"),
        print("│ *     * │"),
        print("└─────────┘"),  
    elif i == 5:   
        print("┌─────────┐"),
        print("│ *     * │"),
        print("│    *    │"),
        print("│ *     * │"),
        print("└─────────┘"),   
    elif i == 6:
        print("┌─────────┐"),
        print("│ *     * │"),
        print("│ *     * │"),
        print("│ *     * │"),
        print("└─────────┘"),   
    else:
        print("none")
        

# creating function which will check that input given by the user is valid(i.e between 1-6) or not.

def pass_input(m):
    
    if m.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(m)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)
        
        
# creating a function which will declare random values chosen        
    
def roll(check):
    result=[]
    for _ in range(check):
        r=random.randint(1,6)
        result.append(r)
    return result


# main code


num= input("how many time you want to roll the dice [1-6]")
check=pass_input(num)
result=roll(check)   
print(result) 
for i in result:
    DICE_ART(i)
