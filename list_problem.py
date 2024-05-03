
#! A function that drops a given number of elemetns from the start of a list : 


""" 

"""

def drop(n , my_list)->[]: 
    if ((n==0) or (my_list is None)):
        return my_list 
    elif(n==1):
        return my_list[1:]
    else: 
        return drop(n-1 , my_list)[1:]
          
my_list = [ 0, 1,2,3,4,5,6,7]
res = drop(7 , my_list)

print(res)