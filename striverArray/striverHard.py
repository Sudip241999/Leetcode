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

     
ob=PascalTriangle()
print(ob.nCr(2,2))
ob.pascalTriangle(4)
          