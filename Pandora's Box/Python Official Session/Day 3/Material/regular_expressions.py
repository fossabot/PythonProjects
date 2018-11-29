# Regular Expressions

'''
Pattern Matching
file_123.txt
file_456.txt
file_789.txt

Starting with a word 'file_' and followed by any three numbers and is ending with
.txt
^file_[0-9][0-9][0-9].txt$
'''

import re

print('-' * 75)

# Check the pattern in the string
def chk_pattern(pattern, inp_string):
    if re.search(pattern, inp_string, re.I):   # Case Insensitive
        pass
    
    if re.search(pattern, inp_string):    # Case Sensitive
        print(pattern, inp_string, 'Satisfied', sep=' -> ')
    else:
        print(pattern, inp_string, 'Not Satisfied', sep=' -> ')

# Get the input from the user
while True:
    string = input('Enter Any String -> ')
    if string.upper() == 'END':
        break

    print('-' * 75)

    '''
    # Simple Match
    chk_pattern('python', string)

    print('-' * 75)

    # Anchors
    # ^ - startswith; $ - endswith
    chk_pattern('^python', string)    # string.startswith('python')
    chk_pattern('python$', string)    # string.endswith('python')
    chk_pattern('^$', string)         # string == ''
    chk_pattern('^python$', string)   # string == 'python'

    print('-' * 75)

    # Range of characters
    # [0-9] => Matches any single digit
    # [a-z] => Matches any single lowercase alphabet
    # [A-Z] => Matches any single uppercase alphabet
    # [a-zA-Z] => Matches any single alphabet
    # [0-9a-zA-Z] => Matches any single alphanumeric
    chk_pattern('^[1-5][awv][A-Z]$', string)
    chk_pattern('[1-5][awv][A-Z]', string)

    var = 'python'
    chk_pattern('[1-5]' + var + '[A-Z]', string)

    print('-' * 75)

    # Metacharacters
    # + => Matches one to many occurrences of previous character(s)
    # * => Matches zero to many occurrences of previous character(s)
    # ? => Matches zero to one occurrence of previous character(s)
    chk_pattern('^ab+c$', string)
    chk_pattern('^ab*c$', string)
    chk_pattern('^ab?c$', string)

    print('-' * 75)

    # Groupings
    chk_pattern('^(ab)+c$', string)

    print('-' * 75)

    # Quantifiers
    chk_pattern('^(ab){2}c$', string)   # Exactly 2 Occurrences
    chk_pattern('^(ab){1,3}c$', string) # Min 1 and Max 3
    chk_pattern('^(ab){,3}c$', string)  # Min 0 and Max 3
    chk_pattern('^(ab){3,}c$', string)  # Min 3 and Max Infinite

    print('-' * 75)

    # Choices
    chk_pattern('^p(hp|erl|ython)$', string)

    print('-' * 75)

    # Alternatives
    chk_pattern('^a[^0-9a-zA-Z]{2}c$', string)
    chk_pattern('^a([^b-f][^w-z]){2}$', string)
    chk_pattern('^p(\^hp|erl|ython)$', string)
    chk_pattern('^p[^(hp)]$', string)

    print('-' * 75)

    # DOT Character(.)
    chk_pattern('p.p', string)
    chk_pattern('a..b', string)
    chk_pattern('a.{2}b', string)
    chk_pattern('^python .*scripting$', string)

    print('-' * 75)

    # Character class escape sequences
    # \d => [0-9]         ; \D => [^\d]
    # \w => [0-9a-zA-Z_]  ; \W => [^\w]
    # \s => space or tab  ; \S => [^\s]
    chk_pattern('^\+91-[6-9]\d{9}$', string)    # Mobile Number
    chk_pattern('^[A-Z]{5}\d{4}[A-Z]$', string) # PAN Number
    chk_pattern('^(\d{4}\s){3}\d{4}$', string)  # Debit/Card Number
    chk_pattern('^(\d{4}\s){2}\d{4}$', string)  # Aadhar Card Number

    print('-' * 75)
    '''

    # Greedy Matches
    inp_pattern = 'python (.*) and (.*) scripting'

    # Search
    # Looks for the pattern anywhere in the string
    searched = re.search(inp_pattern, string)
    if searched:
        print('Searched ->', searched)

        print('Start Position ->', searched.start())
        print('End Position ->', searched.end())
        print('Matched String ->', searched.group(0))

        print('-' * 75)

        print('Group 1 ->', searched.group(1))
        print('Group 2 ->', searched.group(2))
        

    # Match
    # Looks for the pattern only at the beginning of the string
    matched = re.match(inp_pattern, string)
    if matched:
        print('Matched ->', matched)

        print('-' * 75)

    # Compile
    pattern = re.compile('\d{3}')

    print('Searched ->', pattern.search(string))  # Search
    print('Findall ->', pattern.findall(string))  # Findall
                                                  # re.findall('\d{3}', string)

    # Split
    # re.split('\d{3}', string)
    print('Split ->', pattern.split(string))

    # Sub -> Finding and replacing the pattern to some other string
    # re.sub('\d{3}', '555', string)
    print('Sub ->', pattern.sub('555', string))

    print('-' * 75)

print('-' * 75)

# Raw string
string = 'This is \n not raw str\bing'
raw_string = r'This is \n raw string'

print('String ->', string)
print('Raw String ->', raw_string)

print('-' * 75)

string = 'python,scripting,is,on,the,top'

print('Searching "on" ->', re.findall('on', string))
print('Searching word "on" ->', re.findall(r'\bon\b', string))

print('-' * 75)


