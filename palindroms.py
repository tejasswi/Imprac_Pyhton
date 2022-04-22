import sys
import load_dictionary


word_list = load_dictionary.load('2of12.txt')
pali_list = []
for word in word_list:
    if len(word)> 1 and word == word[::-1]:
        pali_list.append(word)
print("\nNumber of Palinndormes found = {}\n".format(len(pali_list)))
print(*pali_list,sep ='\n')

filename = "palingrams.txt"
x=0
#initiation
"""with open('palingrams.txt','r') as text:
    for line in text: #for loop
        line = line.split() #to split the line into words
        for i in range(0,2):
            if line[i] == line[i][::-1]: 
                x +=1 #increment

print(x)"""



            




