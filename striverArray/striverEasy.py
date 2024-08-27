def leftRotateArrayByOnePlace(array):

    i=len(array)-1
    temp=array[i]
    while i>=0:

        if i==0:
            array[len(array)-1]=temp

        else:

            
            array[i-1],temp=temp,array[i-1]

        i-=1
    print(array)



def missingNumber( nums) :
        #converting array to set to retain only unique elements
        temporary_set=set(nums)
        result_with_unique_elements=list(temporary_set)
        distinct_num_length=len(result_with_unique_elements)
        print(distinct_num_length)
        for i in range(distinct_num_length+1):
            if i not in result_with_unique_elements:
                return i
    
def findMaxConsecutiveOnes(nums):

        count=0
        max_count=0
        for i in nums:
            if i == 1: 
                count+=1
                if max_count<count:
                    max_count=count
            else:
                count=0
        return max_count


def unionOfTwoSortedArray(array1,array2):
     
        for element in array1:
             if element in array2:
                  array2.remove(element)
        
        array1.extends(array2)

        return array1



def findUnion(arr1,arr2):

        arr1.extend(arr2)
        temp=set(arr1)
        temp_arr=list(temp)
        temp_arr.sort()
        return temp_arr


# XOR of elements , by using this only single element will be left
def singleNumber( nums) :

        num=0
        for element in nums:
            num^=element
        
    

        return num
                  
