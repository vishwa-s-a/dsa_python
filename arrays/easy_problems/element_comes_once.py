# time complexity is O(n) and space complexity is O(1)
def find_once(arr,n):
    result=arr[0]
    for i in range(1,n):
        result=result^arr[i]#here we are trying to do xor operations as 7^7=0 and 7^0=7 like this we solve it
    return result

def main():
    #here the array contains only one element which will come only once and other elements come twice
    arr=[2, 2,1,3, 5, 4, 5, 3, 4]
    n=len(arr)
    print('The element which occurs only once is : ',find_once(arr,n))
main()