nums=[19,9,10,0]
target = 19
m=1
count=-1
while count<=1:
   # two_sum= nums[] + nums[]
    count+=1
    if nums[count] + nums[1] == target :
        print(f"two_sum{(nums[count],nums[1],target)}")
       
    if nums[count] + nums[2] == target :
            print(f"two_sum{(nums[count],nums[2],target)}")
            
    if nums[count] + nums[3] == target :
           print(f"two_sum{(nums[count],nums[3],target)}")


