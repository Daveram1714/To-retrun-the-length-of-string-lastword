#function word is defined
def string(word):

#using the split() fuction we used to split two strings
    a = word.split()
#we check  the length is greater than zero
    if len(a) > 0:

#if so we calculate it form reverser array
        return a[-1]
    
    else:
        return"no words forund"

#here we have called the defined fuction on top

word=input("Enter the string: ")
b=string(word)
c=print(len(b))
        
   
  