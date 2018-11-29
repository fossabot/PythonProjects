# Lambda Expressions
# Anonymous Function
# Can take any number of parameters of any type
# It will evaluate only one expression
# The output of the expression will be return to the caller function
# without the usage of the return statement

print('-' * 75)

# Simple Function
def calc_func(num, value=2):
    return num ** value

print(calc_func, '->', type(calc_func))
print('Calc Func 1 ->', calc_func(5))
print('Calc Func 2 ->', calc_func(5, 3))

print('-' * 75)

# Lambda Expression
calc_lambda = lambda num, value=2: num ** value
print(calc_lambda, '->', type(calc_lambda))
print('Calc Lambda 1 ->', calc_lambda(5))
print('Calc Lambda 2 ->', calc_lambda(5, 3))

print('-' * 75)

get_palin = lambda lst: [e for e in lst if e == e[::-1]]
print('Get Palin ->', get_palin(['php', '123', '121']))

print('-' * 75)

val_mail_id = lambda mail_id: 'Valid' if mail_id.endswith('@cypress.com', 5) else 'Invalid'
print('Valid Mail Id ->', val_mail_id('justin@cypress.com'))

print('-' * 75)

get_count_char = lambda lst: [{ch: elem.count(ch) for ch in elem}
                              for elem in lst]

lst_of_dicts = get_count_char(('php', 'aba', 'bcc'))
print('List of Dictionaries ->', lst_of_dicts)

for elem in lst_of_dicts:
    print('Element ->', elem)

print('-' * 75)


