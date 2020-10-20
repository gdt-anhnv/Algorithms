"""
Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.
 

Example 1:

Input:
N = 4
arr[] = {1, 5, 3, 2}
Output: 2
Explanation: There are 2 triplets: 
1 + 2 = 3 and 3 +2 = 5 

Example 2:

Input: 
N = 3
arr[] = {2, 3, 4}
Output: 0
Explanation: No such triplet exits

Your Task:  
You don't need to read input or print anything. Your task is to complete the function countTriplet() which takes the array arr[] and N as inputs and returns the triplet count

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 103
1 ≤ arr[i] ≤ 105
"""

def CountTriplets(arr = []) :
    count = 0
    arr.sort()
    for i in range(len(arr) - 1, 1, -1) :
        sum = arr[i]
        min = 0
        max = i - 1
        while max > min :
            if arr[min] + arr[max] == sum :
                count += 1
                min += 1
            elif arr[min] + arr[max] > sum :
                max -= 1
            else :
                min += 1

    return count

def main() :
    count = CountTriplets([1, 2, 3, 4, 5, 6, 7, 10, 15])
    print(count)
    return

main()