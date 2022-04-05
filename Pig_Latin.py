

String_name = input("enter the word\n")

def pig_latin(str):
    for ch in str:
        if ch in "aeiouAeiou":
            #platin = str[1:len(str)]{0}.format("way", "ay")
            mid = str[1:len(str) - 1]
            platin = f"{str[len(str)-1] +mid + str[0]}way" 
            
        else:
            #platin = str[1:len(str)]{1}.format("way", "ay")
           
            mid = str[1:len(str) - 1]
            platin = f"{str[len(str)-1] +mid + str[0]}ay"
        return platin
   
print(pig_latin(String_name))

        
    
    
    