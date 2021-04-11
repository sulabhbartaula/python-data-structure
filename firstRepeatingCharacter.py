"""
Description

Given a string str,
create a function that returns the first repeating character.
If such character doesn't exist, return the null character '\0'.

• Input: str = "programming"
• Output: 'r'

"""

def main():

    input_string = 'programming'

    firstRepeatingChar = findFirstRepeatingCharacter(input_string)

    print(firstRepeatingChar)

#time complexity of function is 0(N)
def findFirstRepeatingCharacter(input_string):

    visited = {}

    for ch in input_string:
        if visited.get(ch):
            return ch
        else:
            visited[ch] = True

    return '/0';
        
main()
