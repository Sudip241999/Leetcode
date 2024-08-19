#1 count the frequency of each element of an array

def countFrequencyOfElements(array):

    if len(array)==0:
        return None
    
    else:
        hashMap={}
        for element in array:
            if element in hashMap:
                hashMap[element]+=1
            else:
                hashMap[element]=1
        
        return hashMap
    

#2 find the highest and the lowest frequency elements in ana array

def highestAndLowestFrequencyElements(hashmap):

    temp=hashmap.values()

    high=max(temp)
    low=min(temp)

    maxElement=[]
    minElement=[]

    for i in hashmap:
        if hashmap[i]==high:
            maxElement.append(i)
        elif hashmap[i]==low:
            minElement.append(i)

    return maxElement,minElement
    

# temp=[1,13,5,1,6,8,5,1]

# hashmap=countFrequencyOfElements(temp)

# print(highestAndLowestFrequencyElements(hashmap))

