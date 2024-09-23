from collections import defaultdict
def majorityElement(nums) :
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        result=[]
        for i in d:
            if d[i]>len(nums)//3:
                result.append(i)

        return result


class PascalTriangle:
    def nCr(self,n,r):
        i=0
        result=1
        while i<r:
            result*=(n-i)
            result//=i+1 
            i+=1
        return result


    def pascalTriangle(self,n):
        final=[]
        for j in range(n+1):
            result=[]
            for i in range(j+1):
                
                temp=self.nCr(j,i)
                result.append(temp)

            final.append(result)

        print(final)


class FourSum():
    def fourSum(self, nums, target):
        
        nums.sort()
        result=[]
        i=0
        while i<len(nums)-3:
            
            j=i+1
            while j<len(nums)-2:
               
                left = j+1
                right=len(nums)-1
                while left<right:
                    s=nums[i]+nums[j]+nums[left]+nums[right]
                    if s==target:
                        if [nums[i],nums[j],nums[left],nums[right]] not in result:
                            result.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1

                    elif s<target:
                        left+=1
                    else:
                        right-=1
                j+=1
            i+=1
        return result
    

class ThreeSum():
    def threeSum(self, nums):
        result=[]
        nums.sort()
        i=0
        while i<len(nums)-2:
            if i != 0 and nums[i] == nums[i - 1]:
                i+=1
                continue
            left=i+1
            right=len(nums)-1
            target=0-nums[i]
            
            while left<right:
                if nums[left]+nums[right]==target:

                    if [nums[i],nums[left],nums[right]] not in result:
                    
                   
                        result.append([nums[i],nums[left],nums[right]])
                    
                    
                    left+=1
                    right-=1

                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while right>left and nums[right]==nums[right+1]:
                        right-=1
                    
                elif nums[left]+nums[right]<target:
                    left+=1
                else:
                    right-=1
            i+=1

        return result



def largestSubarrayWithZeroSum(array):
    mpp={}
    sum=0
    max_count=0
    i=0
    while i<len(array):
        sum+=array[i]
        if sum==0:
            max_count=max(max_count,i+1)
        if sum in mpp:
            count=i-mpp[sum]
            max_count=max(max_count,count)

        else:
            mpp[sum]=i

        i+=1
    return max_count

   


def subarrayWithGivenXOR(A : list,B : int) -> int :
    
    count=0
    xR=0
    d=defaultdict(int)
    d[xR]=1
    for i in A:
        xR=xR^i
        x=xR^B
        count+=d[x]
        d[xR]+=1
            
    return count


def mergeIntervals( intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        j=0
        result=[intervals[0]]
        for i in range(1,len(intervals)):
            if result[j][1]>=intervals[i][0] and result[j][1]<=intervals[i][1] :
                result[j][1]=intervals[i][1]
            elif result[j][1]>=intervals[i][0] and result[j][1]>=intervals[i][1]:
                continue
            else:
                result.append(intervals[i])
                j+=1
            
        return result



def mergeTwoSortedArraysWithoutExtraSpace(nums1,m,nums2,n):
    i=m
    j=0
    while i<m+n:
        nums1[i]=nums2[j]
        j+=1
        i+=1
    nums1.sort()

# find repeating and missing element 
class Solution:
    def findTwoElement( self,arr): 
        # code here
        n=len(arr)
        Sn=(n*(n+1))//2
        S2n=(n*(n+1)*(2*n+1))//6
        S=0
        S2=0
        for i in range(n):
            S+=arr[i]
            S2+=arr[i]**2
        val1=S-Sn
        # print(val1)
        val2=(S2-S2n)//val1
        x=(val1+val2)//2
        y=val2-x
        return x,y






def merge(arr,left,mid,right):
    temp=[]
    low=left
    high=mid+1
    count=0
    while low<=mid and high<=right:
        if arr[low]<=arr[high]:
            temp.append(arr[low])
            low+=1
        else:
            temp.append(arr[high])
            count+= (mid - low + 1)
            high+=1
    while low<=mid:
        temp.append(arr[low])
        low+=1
    while high<=right:
        temp.append(arr[high])
        high+=1
   
    i=left
    while i <=right:
        arr[i]=temp[i-left]
        i+=1
    return count 
        
def countInversions(arr,left,right):
    count=0
    if left>=right:
        return count
    mid=(left+right)//2
    count+=countInversions(arr,left,mid)
    count+=countInversions(arr,mid+1,right)
    count+=merge(arr,left,mid,right)
   
    return count






from typing import List

def merge(arr, low, mid, high):
    temp = []  # temporary array
    left = low  # starting index of left half of arr
    right = mid + 1  # starting index of right half of arr

    # storing elements in the temporary array in a sorted manner
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # if elements on the left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1

    # transferring all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def countPairs(arr, low, mid, high):
    right = mid + 1
    cnt = 0
    for i in range(low, mid + 1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        cnt += (right - (mid + 1))
    return cnt

def mergeSort(arr, low, high):
    cnt = 0
    if low >= high:
        return cnt
    mid = (low + high) // 2
    cnt += mergeSort(arr, low, mid)  # left half
    cnt += mergeSort(arr, mid + 1, high)  # right half
    cnt += countPairs(arr, low, mid, high)  # Modification
    merge(arr, low, mid, high)  # merging sorted halves
    return cnt

def team(skill: [int], n: int) -> int:
    return mergeSort(skill, 0, n - 1)







def maxProduct(nums: List[int]) -> int:
    prefix=1
    suffix=1
    maximum=-float("inf")
    j=len(nums)
    i=0
    while i<len(nums):
        if prefix==0:
            prefix=1
            
        if suffix==0:
            suffix=1    
        prefix*=nums[i]
        suffix*=nums[j-i-1]
        maximum=max(maximum,prefix,suffix)

        i+=1
        
    return maximum

arr=[2,3,-2,4]
print(maxProduct(arr))







        
        

 
          