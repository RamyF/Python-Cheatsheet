def main():
    # multiple assignments
    a, b = 1, "abc"

    # incrementation
    num = 1
    num += 1

    # null value
    var = None

    # conditional
    if num > 2:
        print("number is greater than 2")
    elif num == 2:
        print("number is 2")
    else:
        print("number is less than 2")
    
    # and or operators
    if var != None or a != 1:
        print("something changed")
    elif var == None and num == 1:
        print("nothing has changed")

    # while loops
    counter = 0
    while counter < 5:
        print("incrementing counter")
        counter += 1

    # for loop where i = 0 to i = 4
    for i in range(5):
        print(i)

    # for loop where i = 2 to i = 5 (first num in range function is inclusive last is not)
    for i in range(2, 6):
        print(i)

    # decrementing for loop. i = 6 to i = 1 (3rd value is decrement/incrment by value)
    for i in range(6, 0, -1):
        print(i)
  
    # division (decimal divison is default)
    a = 5 / 2 # equals 2.5
    a = 5 // 2 # equals 2

    # mod (remainder after division)
    a = 10 % 3 # equals 1

    # helpful math methods
    import math
    a = math.floor(3 / 2) # 1 
    a = math.ceil(3 / 2) # 2
    a = math.sqrt(3, 2) # 9

    ######### ARRAYS / lists. Python lists are mutable ##########
    arr = [1, 2, 3]

    # can be used as a stack since the list is mutable
    arr.append(4) # push to stack
    arr.pop() # pop stack

    # insert into array (note O(N) operation)
    arr.insert(1, 2) # insert 2 at index i = 1

    #initialize array of certain size
    arr2 = [1] * 5 # [1, 1, 1, 1, 1]

    # indexing backwards
    print(arr[-1]) # 3; last val of array

    # sublists / slicing an array
    newArr = [1, 2, 3, 4, 5, 6]
    slicedArr = newArr[0:3] # [1, 2, 3]; last val of slice is not inclusive

    # looping thru arrays
    nums = [1, 2, 3, 4, 5]

    # loop thru index values of array
    for i in range(len(nums)):
        print(nums[i])

    # loop thru values of array
    for num in nums:
        print(nums)

    # index and value
    for index, value in enumerate(nums):
        print(index, value)

    # combine arrays a loop thru both of them
    arr1 = [1, 2, 3, 4]
    arr2 = [5, 6, 7, 8]
    for num1, num2 in zip(arr1, arr2):
        print(num1, num2)
    
    # reverse array
    arr1.reverse()

    # sorting; note sort uses Tim sort which is a combo of merge sort and quick sort. time is O(nlogn)
    arr2.sort()
    arr2.sort(reverse=True)

    # sort strings is by alphabetical order
    a1 = ["b", "a", "c"].sort # ["a", "b", "c"]
    # custom sort (by len of string)
    a2 = ["amy", "charlie", "bobby"].sort(key=lambda x: len(x)) # ["amy", "bobby", "charlie"]

    # list comprehension
    newArr = [i*2 for i in range(5)] # [0, 2, 4, 6, 8]

    # 2D List
    twoDList = [[0] * 4 for i in range(4)] # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    ##### STRINGS #########

    # act very similar to arrays
    str = "abc"
    subStr = str[0:2] # "ab"

    # however strings are not mutable. Can't change char value of string. i.e str[1] = "t"

    # appending creates a new string
    str += "def" # new "abcdef" string

    # can be converted to integers and vice versa
    num = int("123") # 123
    str = str(123) + str(123) # "123123"

    # ascii value of char
    print(ord("a"))

    ######### QUEUES #######

    from collections import deque

    queue = deque()
    queue.append(1)
    queue.append(2) # ([1,2])
    queue.popleft() # ([2])
    queue.appendleft(2) # ([1, 2])
    queue.pop() # ([1])


    ###### HASHSET #######
    # operations are O(1)

    hashset = set()
    hashset.add(1)
    hashset.add(2) # {1, 2}

    # check if val in set
    print(1 in hashset)

    hashset.remove(2) # {1}

    ####### HASHMAP / DICT ########

    defaultMap = defaultdict(list) # *** creates a dictionary with the defualt value of a new key being an empty list i.e { 'new_key': [] }
    map = {}
    map["amy"] = 1 # { "amy": 1 }
    map["bobby"] = 2 # { "amy": 1, "bobby": 2 }
    map.pop("amy")
    print("amy" in map)

    # dictionary comprenhension (useful for creating graphs/adjeceny lists)
    graph = { i: 2*i for i in range(5) }

    # looping through map
    map = {"amy": 1, "bobby": 2}
    # keys
    for key in map:
        print(key, map[key])
    # values
    for value in map.values:
        print(value)
    # key and values
    for key, value in map.items():
        print(key, value)


    # tuples
    a = (1, 2, 3) # immutable 

    # most often used as keys in a map
    myMap = {
        (1, 2): 3
    }
    myMap[(1,2)] # 3


    ##### HEAPS #######
    import heapq

    # useful for finding max or min of a set of values
    # by default they are min heaps
    minHeap = []
    heapq.heappush(minHeap, 3)
    heapq.heappush(minHeap, 2)
    heapq.heappush(minHeap, 4)

    # min is at index 0
    print(minHeap[0]) # 2

    # looping thru non null heap (prints val from smallest to largest)
    while len(minHeap):
        print(heapq.heappop(minHeap)) # 2, 3, 4

    # to use maxheap multiple val by -1 when inserting and processing
    maxHeap = []
    heapq.heappush(maxHeap, -1 * 3)
    heapq.heappush(maxHeap, -1 * 2)
    heapq.heappush(maxHeap, -1 * 4)

    # max is at first index
    print(maxHeap[0] * -1) # 4

    while len(maxHeap):
        print(heapq.heappop(maxHeap) * -1) # 4, 3, 2

    # build heap from exisiting values
    arr = [4, 6, 30, 2, 50, 7]

    # build heap in O(N) time
    heapq.heapify(arr) # note it will be a min heap unless all values are multiplied by -1

### INNER FUNCTIONS ##
# inner functions do not need vals to be passed in (useful for graphs and recursion)
def outer(a, b):
    c = 2

    def inner():
        return a + b + c
    
# print(outer(2, 4)) returns 8

s = "abceedba"
print(s[:2] + s[3:])
    
