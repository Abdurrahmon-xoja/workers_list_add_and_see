from functions import add_workers
from functions import see


user_order = input('what you want to do: ')

if user_order == 'add':
    user_order_name = input('enter name: ')
    user_order_age = input('enter age: ')
    user_order_position = input('enter position: ')
    add_workers(user_order_name, user_order_age, user_order_position)

elif user_order == 'see':
    see()
