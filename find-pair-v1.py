def main():

    input_array = [7,5,9,15,1]
    key = 10

    isPairExist = findPair(input_array,key)

    print(isPairExist)

#time complexity of function is O(n.logn)
def findPair(arr,key):

    #sorting array nlogn
    arr.sort()
    left = 0
    right = len(arr) - 1

    #traversing array is O(n)
    while left < right:
        if arr[left] + arr[right] == key:
            return True
        elif arr[left] + arr[right] < key:
            left += 1
        else:
            right -= 1
    return False
            

main()
