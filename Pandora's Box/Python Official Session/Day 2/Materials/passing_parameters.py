# Forms of Parameters

def display_emp(name, loc='bangalore', salary=5000):
    return '{0} from {1} earns Rs.{2}'.format(name,
                                              loc,
                                              salary)
    # return name + ' from ' + loc + ' earns Rs.' + str(salary)

print('-' * 75)

print('Positional Parameters')

# All the parameters should be passed
# Order of parameters mandatory
print(display_emp('ravi', 'pune', 8000))
print(display_emp('pune', 8000, 'ravi'))

print('-' * 75)

print('Keyword Parameters')

# All the parameters should be passed
# Order of parameters optional
print(display_emp(name='raj',
                  loc='pune',
                  salary=7000))
print(display_emp(loc='pune',
                  salary=7000,
                  name='raj'))

print('-' * 75)

print('Mix of Positional and Keyword Parameters')

# Positional Parameters followed by Keyword Parameters
print(display_emp('justin', salary=8000, loc='pune'))

print('-' * 75)

print('Default Parameters')

# Default values to the parameters should be given in function definition
# Non default Parameters followed by Default Parameters
# Parameters which has default values are optional to pass

print(display_emp('pradeep'))
print(display_emp('pradeep', salary=8000))
print(display_emp('pradeep', 'kochin'))

print('-' * 75)

print('Variable Length Parameters')

# *args => 'n' number of positional parameters retrieved in the form of tuple
# **kwargs => 'n' number of keyword parameters retrieved in the form of dictionary

def display_details(lang, *scr, platform, **det):
    print(lang, '->', type(lang))
    print(scr, '->', type(scr))
    print(det, '->', type(det))
    print(platform, '->', type(platform))

display_details('php',
                'perl',
                'python',
                list(range(1,6)),
                typ='interpreted',
                name='scripting',
                platform='multi',
                lst=[x for x in 'python'])

print('-' * 75)

display_details('python', platform='multi')

print('-' * 75)
