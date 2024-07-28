def ab(nums):
    a=sorted(nums)
    b=set()
    for i in a:
        if (i-1)>0 and (i-1) not in b:
            b.add(i-1)
        elif i not in b:
            b.add(i)
        else:
            b.add(i+1)
    return len(b)
nums=[1,1,1,1]
print(ab(nums))
        
            
