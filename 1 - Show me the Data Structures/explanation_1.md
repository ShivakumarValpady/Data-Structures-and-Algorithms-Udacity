As the LRU Cache has to designed using O(1) complexity, using the dictionary is a good option. The dictionaries can access values from the given keys in constant time. 
The queue has been created for keeping order of the elements by using dequeue from collections. The least recently usd element can be removed from cache by using the popleft() function of dequeue. 

Get Time complexity: O(1) Set Time complexity: O(1)

Space complexity of the LRU: O(capacity)


