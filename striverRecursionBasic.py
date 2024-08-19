#1 printing number upto n

def repeat_name(start,end):
    if start>end :
        return

    print(start,end=" ")

    return repeat_name(start+1,end)

#2 sum of firt n numbers
 
def sumOfFirstN_numbers(sum,start,end):
    if start>end :
        return sum

    sum+=start
    
    return sumOfFirstN_numbers(sum,start+1,end)



#3 checking a string is palindrome or not
def palindromOrNot(start,end,word):

    if start>end:
        return True
    
    else:
        if word[start]==word[end]:

            start+=1
            end-=1
            return palindromOrNot(start,end,word)
        
        else:

            return False
        

#4 printing fibonacci series 
def fibonacciSeries(n):

    if n<=1:
        return n
   
    
    else : 
        last=fibonacciSeries(n-1)
        secondLast=fibonacciSeries(n-2)

        return last+secondLast
    
#5 printing the factorial value
def factorial(n):
    if n==0:
        return 1
    


    
    return n*factorial(n-1)
        


#6 reversing an array
def reverseAnArray(start , end , array):

    if start>=end:
        return array
    

    array[start],array[end] = array[end],array[start]

    start+=1
    end-=1

    return reverseAnArray(start,end ,array)




