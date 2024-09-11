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

   





        
        

 
          