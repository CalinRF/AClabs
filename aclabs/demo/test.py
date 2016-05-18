# #another comment
# #My first python app
# ''' 
#     some comment here
# '''

# a = 10

# my_string = 'test'
# my_string = 'test2'
# # 'test' now destroyed by garbage collector


# # c = int(raw_input('Number: '))
# # print('Your number  %s' % c)
# # print(c + a)

# my_dict = {'test' : 10,
#             'abc' : [1, 2, 'abbb', 'test3'],
#             'c' : dict(a=10),
#             'cd' : {'a': 10}}

# # print my_dict
# # print my_dict['abc']
# # my_dict['c'] = 'a'
# #prints all functions of my_dict
# #print dir(my_dict)

# # a = range(10)
# # print a[2:-1: 2]

# #from aclabs.demo2 import utils
# # def my_function(a, b, c, d=10):
# #     #prints variables in scope
# #     print locals()
# # my_function(1, 2, c='Test')

# # def my_function2(a, *args, ** kwargs):
# #         print locals()

# # my_function2(1,2,3, kw='test')

# # def tuple_example():
# #     #tuples - lists that cannot be modified
# #     my_list  = [1,2,3]
# #     my_tuple = (1,2,3)

# #     my_list += [1] #or my_list.append(1)
# #     #can't do that with tuples
# #     my_tuple2 = 1,
# #     print my_tuple + my_tuple2
# #     print locals()

# # tuple_example()


# #print utils.read_from_stdin()

# def func_raising_exception():
#     raise Exception('expected exception')

# def test_exc():
#     try:
#         func_raising_exception()
#     except (Exception, IOError) as ex:
#         print(ex)
#     finally:
#         print('test_exc finished')

# test_exc()




# import contextlib

# @contextlib.contextmanager
# def my_open(*args, **kwargs):
#     f = None
#     try:
#         f = open(*args, **kwargs)
#         yield f
#     finally:
#         if f:
#             f.close()

# def io_demo():
#     import os 

#     tmp_file = '/home/calin/Desktop/random_file'
#     with open(tmp_file, 'w') as f:
#         f.write('test')
#     with my_open(tmp_file, 'r') as f:
#         f.read()

#     os.unlink(tmp_file)

# io_demo()

# def test_xrange():
#     import pdb
#    # pdb.set_trace()
#    #sets brakpoint in here

#     my_list = xrange(10000)
#     for i in my_list:
        
#         if not (i % 2 == 0):
#             continue
#         if(None or '' or 0 or False or {} or []):
#             print 'found smt'
#         print i
#         if i in range(3):
#             print '%s < 3 ' % i
#         if i >= 5:
#             break

# test_xrange()
#(x for x in xrange(100000) if (x % 2 == 2)

# def even_generator():
#    i = 0
#    while True:  
#        i +=2 
#        yield i

# for i in even_generator():
#     print i
#     if i == 10:
#         break   

# f = lambda x ,y, *args, **kwargs: x * y
# print f(1, 2, 'stuff')

# def random_function(a,b,c):
#     return a, b, c

# cbk = lambda: random_function(1, 2, 3)
# print cbk()    
# #same thing
# import functools
# cbk = functools.parials(random_function, 1, 2, 3)
# cbk()

# def get_callback(*args, **kwargs):
#     def callback():
#         return f(*args, **kwargs)
#     return callback
# #still the same - could be used to test inputs
# cbk = get_callback(random_function, 1,2,3)
# print cbk()

# #Serializing 
# import json
# #help(json.load)
# my_dict = dict(key=10)
# serialized = json.dumps(my_dict)
# print serialized

# received = json.loads(serialized)
# print received

# my_string = "%(id)s-%(nume)s" % dict(id=0, nume="annon")
# #same
# my_string = "%s-%s" % (0, "annon")
# print my_string

import logging
logger = logging.getLogger('mylogger')

fmt = logging.Formatter(fmt = '%(asctime)s: %(levelName)s - %(message)s')
handler = logging.StreamHandler()
logger.addHandler(handler)

def test():
    logger.info("My method was called")

test()