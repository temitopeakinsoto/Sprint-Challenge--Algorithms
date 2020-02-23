#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime of the snippet of code in a is O(n) - this is because the number of operations increases linearly with the input size (n) due to the While loop.


b) The runtime of the snippet of code in b is O(n log(n)) - the outer loop is O(n) and the nested loop is O(log n) since j *= 2 is processing more than one element at a time, making the runtime complexity of the entire algorithm O(n log(n))


c) The runtime for the snippet of code in c is O(n) - This is because, each time a recursive call is made, the runtime complexity of that recursive all is O(n). The base case is O(1) and the recursive case is O(n) since it makes one recursive call, which can all be simplified to O(n)

## Exercise II
In this case, we are trying to search for floor 'f' in such a way that the number of broken eggs is minimized. Hence we search using Binary Search Approach which has a runtime complexity of O(log n)

Start at the floor that is in the middle of the building (n // 2) Drop an egg If egg break, move to the floor that is the halfway point between where you currently are and the max floor If egg breaks, move to the floor that is the halfway point between the min floor and where you currently are Repeat the process of cutting floors in half until you are at the highest floor where an egg can be dropped and will not break. That floor is the floor that represents the  value of 'f'.



