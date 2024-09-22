#1 selection sort
        # - one outer loop to iterate through all elements of an array
        # - inner loop is to find the minimum
        # - then replace the minimum value with the strting value

def selectionSort(array):
    i=0
    while i<len(array):
        j=i
        minimum=i
        while j<len(array):
            if array[j]<array[minimum]:
                minimum=j
            j+=1

        array[i],array[minimum]=array[minimum],array[i]
        i+=1

    return array

#2 Bubble sort

        # - one outer loop to iterate n-1 number of time to sort the array
        # - in the inner loop we will swap two adjacent elements if the largest element in the left side , by this after one iteration largest element will be in the last position


def bubbleSort(array):
    i=0 
    while i<len(array)-1:
        j=0
        while j < len(array)-1-i:
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]

            j+=1
        i+=1

    return array



#3 Insertion sort

        # - one outer loop to iterate through all elements
        # - innerloop tries to compare the current element with previous element and swap if needed until it placed in its correct position



def insertionSort(array):
    i=1
    while i<len(array):
        j=i
        while j>0 and array[j]<array[j-1]:
           
            array[j-1],array[j]=array[j],array[j-1]

            j-=1

        i+=1
    return array


#4 quick sort
class QuickSort():        
    def partition(self,array,low,high):

        pivot=array[low]
        i=low
        j=high
        while i<j:
            while array[i]<=pivot and i<high:
                i+=1

            while array[j]>pivot and j>low:
                j-=1
            
            if i<j:
                array[i],array[j]=array[j],array[i]

        array[j],array[low]=array[low],array[j]
        return j


    def quickSort(self,array,low,high):
        if low>=high:
            return 
        partitionIndex=self.partition(array,low,high)
        self.quickSort(array,low,partitionIndex-1)
        self.quickSort(array,partitionIndex+1,high)



#5 Merge Sort


def merge(array,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while left<=mid and right<=high:
        if array[left]<=array[right]:
            temp.append(array[left])
            left+=1
        else:
            temp.append(array[right])
            right+=1

    while left<=mid:
        temp.append(array[left])
        left+=1
    
    while right<=high:
        temp.append(array[right])
        right+=1

    i=low
    while i <=high:
        array[i]=temp[i-low]
        i+=1
    
def mergeSort(array,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    mergeSort(array,low,mid)
    mergeSort(array,mid+1,high)
    merge(array,low,mid,high)

arr=[5,4,3,2,1]
mergeSort(arr,0,4)
print(arr)
    









