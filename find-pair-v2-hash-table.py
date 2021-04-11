"""
Description

Given an array of integers arr and an integer k, create a boolean
function that checks if there exists two elements in arr such that
we get k when we add them together.

using hashtable

"""

def main():

    input_array = [7,5,9,15,1]
    key = 10

    isPairExist = findPair(input_array,key)

    print(isPairExist)

#time complexity of function is O(n)
def findPair(arr,key):

    visited = {}

    #traversing through each element in array is O(n)
    for element in arr:
        #lookup in hashtable is constant O(1)
        if visited.get(key - element):
            return True
        else:
            #insertion in hashtable is constant O(1)
            visited[element] = True

    return False
            

main()
