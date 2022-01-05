#1
def calculate(min,max):
    sum=0
    for i in range(min,max+1):
        sum+=i
    print(sum)
calculate(1,3)
calculate(4,8)
#2
def avg(data):
    number = data["count"]
    sum=0
    for i in range(number):
        sum += data["employees"][i]["salary"]
    print('average:%f'%(sum/number))
avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
})
#3
def maxProduct(nums):
    max = nums[0]*nums[1]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            left = nums[i]
            right = nums[j]
            temp = left*right
            if temp>max:
                max=temp
    print(max)
maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])
maxProduct([-1,2])
maxProduct([-1,0,2])
maxProduct([-1,-2,0])
#4
def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            left = nums[i]
            right = nums[j]
            temp = left+right
            if temp==target:
                return[i,j]
result=twoSum([2,11,7,15],9)
print(result)
#5
def maxZeros(nums):
    count=0
    List=[]
    for elem in nums:
        if elem==0:
            count+=1
        elif count!=0:
            List.append(count)
            count=0
    if List and count==0:
        pass
    else:
        List.append(count)
    print(max(List))
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
