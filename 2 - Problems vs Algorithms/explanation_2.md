Here are the detailed breakdowns of the algorithm:

* Initiate the pointer start to 0, and the pointer end to n - 1.
* Perform standard binary search. While start <= end:
  *Take an index in the middle mid as a pivot.

  * If nums[mid] == target, the job is done, return mid.

  * Now there could be two situations:
      * Pivot element is larger than the first element in the array, i.e. the subarray from the first element to the pivot is non-rotated.
          - If the target is located in the non-rotated subarray: 
              go left: `end = mid - 1`.
  
          - Otherwise: go right: `start = mid + 1`.
          
      * Pivot element is smaller than the first element of the array, i.e. the rotation index is somewhere between 0 and mid. 
        It implies that the sub-array from the pivot element to the last one is non-rotated.
        
            - If the target is located in the non-rotated subarray: 
                go right: `start = mid + 1`.
                
            - Otherwise: go left: `end = mid - 1`
