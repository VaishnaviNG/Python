# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # +++your code here+++
    start = s.find("not")
    end = s.find("bad")
    str_to_replace = s[start:end+3]
    return s.replace(str_to_replace,"good")


input_str = input("Enter a string with words not and bad(Ex:'This dinner is not that bad!'):\n")
print(not_bad(input_str))
