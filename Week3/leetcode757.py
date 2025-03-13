class Solution:
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: (x[1], -x[0]))

        size = 0
        largest = -1
        second_largest = -1
        
        for start, end in intervals:

            if start > largest:

                size += 2
                largest = end
                second_largest = end - 1

            elif start > second_largest:

                size += 1
                second_largest = largest
                largest = end
   
        return size
        