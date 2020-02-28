#!/usr/bin/env python
# coding: utf-8

# In[1]:


import timeit,os

def factorial():
    try:
        os.remove('output_1.txt')
    except OSError:
        pass
    
    output_file = open('output_1.txt', 'w')
    request_count = 0
    for num in num_list[:-1]:
        request_count+=1
        start_time = timeit.default_timer()
        fact = calculate_factorial(int(num))
        end_time = timeit.default_timer()
        output_file.write(str(request_count)+' '+str(end_time-start_time)+' '+str(num)+' '+str(fact) + '\n')
    output_file.close()

def calculate_factorial(num):
    result = 1
    if num == 1:
        return 1
    else:
        result = num * calculate_factorial(num-1)
        return result
    
if __name__ == '__main__':
    input_file = open('input.txt', 'r')
    num_list = (input_file.read().split('\n'))
    factorial()
    input_file.close()


# In[ ]:




