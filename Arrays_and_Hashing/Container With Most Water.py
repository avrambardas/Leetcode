class Solution(object):
    def maxArea(self, height):
        pointer1 = 0
        pointer2 = len(height)-1
        
        most_water = 0
        while pointer1 < pointer2:
            min_pointer = min(height[pointer1], height[pointer2])
            
            contained_water = min_pointer*(pointer2-pointer1)
            if contained_water > most_water:
                most_water = contained_water
            if min_pointer==height[pointer1]:
                pointer1 += 1
            else:
                pointer2 -= 1
        return most_water
