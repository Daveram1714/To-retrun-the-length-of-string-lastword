def string(last):
   
    a = last.split()
    
   
    if len(a) > 0:
        
        return a[-1]
    else:
        
        return "No words found in the input string"


last = input(f"Enter the sting value: ")
b = string(last)
print("Last word:", str(len(b)))

