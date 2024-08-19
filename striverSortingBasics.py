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




