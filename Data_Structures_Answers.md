Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
- O(1) because we're only going to be appending a single item at a time and once that item enters the if/else statement and performs an operation that isn't impacted by the size of the input it will always only have 1 input.

2. What is the space complexity of your ring buffer's `append` function?
- Again this is going to be O(1) because we are only appending one item to our storage dictionary every time we call the function. 

3. What is the runtime complexity of your ring buffer's `get` method?
- Our Get method runs in O(n), n being the length of our storage array. Instead of passing back our variables we need to loop our data to make sure no "None" objects exist. This manipulation increases our runtime to O(n) instead of O(1)

4. What is the space complexity of your ring buffer's `get` method?
- The space complexity is a little heavier here as we're using a secondary variable to store our filtered values. As I write this I wonder if I can't convert it to a list comprehension to save on storage? You know what, it worked! Optimized it so now we are just relying on our class's storage, giving us a O(1) space complexity.

5. What is the runtime complexity of the provided code in `names.py`?
- The nested for loop immediately jumps out here, and we've seen so far a nested for loop usually returns a complexity of O(n^2)

6. What is the space complexity of the provided code in `names.py`?
- The space complexity is going to be dependent on the amount of names we receive. We could be storing 1 name or thousands! So I think this comes out to be O(n) as we are storage size is dependent on the amount we input in.

7. What is the runtime complexity of your optimized code in `names.py`?
- Though I have not implemented with a data structure we had this week, I did use a list comprehension to help speed up our code. Now we are just dependent on the amount of names in the first input creating an O(n) relationship. 

8. What is the space complexity of your optimized code in `names.py`?
- Space complexity again will be dependent on the amount of names in our initial input so that creates O(n) again.
