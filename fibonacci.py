#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, timeit

def fibonacci():
    try:
        os.remove('output_2.txt')
    except OSError:
        pass
    output_file = open('output_2.txt', 'w')
    request_count = 0
    for num in num_list[:-1]:
        request_count+=1
        start_time = timeit.default_timer()
        fibo = calculate_fibonacci(int(num))
        end_time = timeit.default_timer()
        output_file.write(str(request_count)+' '+str(end_time-start_time)+' '+str(num)+' '+str(fibo) + '\n')
    output_file.close()

def calculate_fibonacci(num):
    result_list = []
    for i in range(num):
        if i == 0:
            result_list = result_list+[0]
        elif i == 1:
            result_list = result_list+[1]
        else:
            result_list = result_list + [sum(result_list[-2:])]
    return result_list

if __name__ == '__main__':
    input_file = open('input.txt', 'r')
    num_list = (input_file.read().split('\n'))
    fibonacci()
    input_file.close()


# In[ ]:




