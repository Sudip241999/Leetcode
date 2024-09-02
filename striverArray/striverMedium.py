def twoSum(array,target):
    array.sort()
    left=0
    right=len(array)-1
    while left<right:
        sumOfTwoNumber=array[left]+array[right]
        if sumOfTwoNumber==target:
            print(array[left],array[right])
            return array[left],array[right]
        elif sumOfTwoNumber<target:
            left+=1
        else:
            right-=1
    return -1,-1


def majorityElement(array):
    hashmap={}
    for i in array:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1
    temp=max(hashmap.values())
    print(temp)
    for i in hashmap:
        if hashmap[i]==temp:
            return i


def largestSubArraySum(array):
    maximum_sum=-float('inf')
    sum=0
    i=0
    while i < len(array):
        sum+=array[i]
        if sum<0:
            sum=0
        else:
            maximum_sum=max(sum,maximum_sum)
        i+=1

    return maximum_sum


def bestTimetoBuyandSellStock(array):
    max_profit=0
    i=0
    left=0
    
    while i < len(array):
        profit=0


        if i==len(array)-1:
            profit=array[i]-array[left]
            max_profit=max(profit,max_profit)



        elif  array[i]>array[i+1]:
            if array[left]>array[i+1]:
                left=i+1
                i=left
                
        else:
            profit=array[i+1]-array[left]
            max_profit=max(profit,max_profit)
        
        i+=1

    print(max_profit)



def rearrangeArray(nums) :
        positive=[]
        negative=[]
        for i in nums :
            if i>=0:
                positive.append(i)
            else:
                negative.append(i)
        result=[]
        i=0
        pos=0
        while i<len(nums):
            if i%2==0:
                result.append(positive[pos])
            else:
                result.append(negative[pos])
                pos+=1
            i+=1
        return result



def nextPermutation(array):
    index=-1
    i=len(array)-2
    while i>=0:
        if array[i]<array[i+1]:
            index=i
            break
        i-=1
    if index==-1:
        array.reverse()
        return array
    j=len(array)-1
    while j>index:
        if array[j]>array[index]:
            array[j],array[index]=array[index],array[j]
            array[index+1:] = list(reversed(array[index+1:]))

            return array
        j-=1



def leadersInAnArray(array):
    n=len(array)-1
    maximum=array[n]
    result=[maximum]
    while n-1>=0:
        if array[n-1]>=maximum:
            result.append(array[n-1])
            maximum=array[n-1]
        n-=1
    return result


def longestConsecutive(nums) :
        
        if len(nums)==1:
            return 1
        if len(nums)==0:
            return 0

        nums.sort()
        maximum_count=1
        last_smallest=-float("inf")
        count=0
        for i in nums:
            if i==last_smallest:
                continue
            elif i-1==last_smallest:
                last_smallest=i
                count+=1
                maximum_count=max(count,maximum_count)
            else:
                last_smallest=i
                count=1

        return maximum_count




            




array=[4, 7, 1, 0]
print(leadersInAnArray(array))