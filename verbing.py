# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

##def verbing(s):
##    str_len = len(s)
##    verb=''   
##    if str_len<3:
##        verb=s
##    else:
##       if s[str_len-3:str_len]=="ing":
##            verb = s+'ly'
##       else:
##            verb=s+'ing'
##    return verb


def verbing(s):
     verb=''
     verb=(s if len(s)<3 else
                    (s+'ly' if s[len(s)-3:len(s)]=="ing"
                     else s+'ing'))

     return verb


print(verbing("Hi"))
print(verbing("Coming"))
print(verbing("Add"))
