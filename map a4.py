num_list=[1,2,3,4,5,6,7]
print("original list:", num_list)
result=map(lambda x: x+x+x,num_list)
print("triple list:", list(result))
