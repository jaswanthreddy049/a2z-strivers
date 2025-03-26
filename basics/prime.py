"""Problem statement
A prime number is a positive integer that is divisible by exactly 2 integers, 1 and the number itself.



You are given a number 'n'.



Find out whether 'n' is prime or not.



Example :
Input: 'n' = 5

Output: YES

Explanation: 5 is only divisible by 1 and 5. 2, 3 and 4 do not divide 5.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
5


Sample Output 1:
YES


Explanation of sample input 1 :
5 is only divisible by 1 and 5. 2, 3 and 4 do not divide 5.


Sample Input 2:
6


Sample Output 2:
NO"""
n=int(input())
count=0
for i in range(1,n):
    if n%i==0:
        count+=1
        if count>1:
            break
if count==1:
    print("YES")
else:
    print("NO")
