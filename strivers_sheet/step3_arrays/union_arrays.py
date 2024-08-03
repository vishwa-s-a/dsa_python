# we will get a list as output which is the union of two given sorted list

# time complexity is O(m+n), where m is length of array1 and n is length of array2
# space complexity is O(m+n)
def union_array(l1,l2):
    i=0
    j=0
    ans=[]
    while(i<len(l1) and j<len(l2)):
        if(l1[i]<=l2[j]):
            if(len(ans)==0 or ans[-1]!=l1[i]):
                ans.append(l1[i])
            i+=1
        else:
            if(len(ans)==0 or ans[-1]!=l2[j]):
                ans.append(l2[j])
            j+=1
    while(i<len(l1)):
        if(len(ans)==0 or ans[-1]!=l1[i]):
            ans.append(l1[i])
        i+=1
    while(j<len(l2)):
        if(len(ans)==0 or ans[-1]!=l2[j]):
            ans.append(l2[j])
        j+=1

    return ans


l1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2=[2, 3, 4, 4, 5, 11, 12]
ans=union_array(l1,l2)
print(ans)