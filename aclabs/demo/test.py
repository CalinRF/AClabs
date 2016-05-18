#another comment
#My first python app
''' 
    some comment here
'''

a = 10

my_string = 'test'
my_string = 'test2'
# 'test' now destroyed by garbage collector


# c = int(raw_input('Number: '))
# print('Your number  %s' % c)
# print(c + a)

my_dict = {'test' : 10,
            'abc' : [1, 2, 'abbb', 'test3'],
            'c' : dict(a=10),
            'cd' : {'a': 10}}

# print my_dict
# print my_dict['abc']
# my_dict['c'] = 'a'
#prints all functions of my_dict
#print dir(my_dict)

# a = range(10)
# print a[2:-1: 2]


# def my_function(a, b, c, d=10):
#     #prints variables in scope
#     print locals()
# my_function(1, 2, c='Test')

# def my_function2(a, *args, ** kwargs):
#         print locals()

# my_function2(1,2,3, kw='test')

def tuple_example():
    #tuples - lists that cannot be modified
    my_list  = [1,2,3]
    my_tuple = (1,2,3)

    my_list += [1] #or my_list.append(1)
    #can't do that with tuples
    my_tuple2 = 1,
    print my_tuple + my_tuple2
    print locals()

tuple_example()