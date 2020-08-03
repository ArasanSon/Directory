def birthday(s, d, m):
    count=0
    for j in range(0,len(s)):
        sum=0
        for i in range(0,m):
            if (i+j)<=(len(s)-1):
                
                sum+=s[i+j]
                print(s[i+j],i+j,sum)
        if sum==d:
            count+=1
    return count
print(birthday([1,2,1,3,2],3,2))
