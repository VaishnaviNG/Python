#list=[expression for x in sequence]

#Find all of the numbers from 1-1000 that are divisible by 7
print([number for number in range(1,1001) if number%7 == 0])


#Find all of the numbers from 1-1000 that are divisible by 7
print([number for number in range(104) if str(number).find('3') != -1])

#Count the number of spaces in a string
print( "The big bad fox ".count(" "))
print("The big bad fox ".split())

#Remove all of the vowels in a string
input_txt = "The quick brown fox jumps over the lazy dog"
##vowels = ['a','e','i','o','u']
##for char in input_txt:    
##    if char not in vowels:
##       print(char,end='')
        

print( ''.join([char for char in input_txt if char not in ['a','e','i','o','u']]))

#Find all of the words in a string that are less than 4 letters


##for words in input_txt.split(' '):
##    if len(words)<4:
##        print(words)

print([words for words in input_txt.split() if len(words)<4])

#Use a dictionary comprehension to count the length of each word in a sentence

print({words:len(words) for words in input_txt.split()})


#Use a nested list comprehension to find all of the numbers
#from 1-1000 that are divisible by any single digit besides 1 (2-9)

##for number in range(11):
##    for div in range(2,10):
##        if number%div==0:
##                 print(number)

print( { number for number in range(101)
                 for div in range(2,9)
                  if number%div == 0 })


            


