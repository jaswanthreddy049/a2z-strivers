"""
Problem statement
You are given a number ?n?.
Find the number of digits of ?n? that evenly divide ?n?.
Note:
A digit evenly divides ?n? if it leaves no remainder when dividing ?n?.
Example:
Input: ?n? = 336
Output: 3
Explanation:
336 is divisible by both ?3? and ?6?. Since ?3? occurs twice it is counted two times.
Note:
You don?t need to print anything. Just implement the given function.
"""
def countDigits(n: int) -> int:
    dup=n
    count=0
    while(n>0):
        rem=0
        rem=n%10
        n=n//10
        if rem!=0:
            if dup%rem==0:
                count+=1
    return count
    pass