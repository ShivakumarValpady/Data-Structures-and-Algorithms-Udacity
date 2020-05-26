For this dutch national flag problem, I just copied the solution from the "lesson 2: sorting algorithms". And I add some extra checking. For example, if the length of the input list 
is empty, then it returns -1. If there is any number other than 0s, 1s, or 2s, then it prints "Error, please only included 0s, 1s, or 2s" and returns -1. There are four different
conditions in the IF statement. This is a single traversal by putting all possible 0 at the start of the array, all 2s in the end, and the 1s in the middle of array.
Time complexity: O(n). Because we need to check all the elements in the input list.
Space complexity: O(1). Because we sort the list in place.
