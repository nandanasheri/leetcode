'''
preserve order - index positions
hashmap string -> index position
Shogun -> 0
Tapioca Express -> 1

list2 -> ["KFC","Shogun","Burger King"]

element = Shogun 1+0 => 1

minimum = len(list1) + len(list2) // 1
for i in range(list2):
    # check for common
    if list2[i] in hashmap:
        check for the minimum
        min = min(min, i+hashmap[[i]])

result = []
iterate through the list2:


'''
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_map = {}

        for i in range(len(list1)):
            list1_map[list1[i]] = i
    
        minimum = len(list1) + len(list2)

        # iterate through to find minimum index sum 
        for i in range(len(list2)):
            if list2[i] in list1_map:
                ind_list1 = list1_map[list2[i]]
                minimum = min(minimum, i+ind_list1)
       
        result = []
        for i in range(len(list2)):
            if list2[i] in list1_map and i + list1_map[list2[i]] == minimum:
                result.append(list2[i])
        
        return result

        