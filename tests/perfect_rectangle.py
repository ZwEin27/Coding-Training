import sys

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        min_axis_x = min_axis_y = sys.maxint
        max_axis_x = max_axis_y = -sys.maxint
        areas = []
        i = 0
        for i in range(len(rectangles)):
            rectangle = rectangles[i]
            if rectangle[0] < min_axis_x:
                min_axis_x = rectangle[0]
            if rectangle[1] < min_axis_y:
                min_axis_y = rectangle[1]

            if rectangle[2] > max_axis_x:
                max_axis_x = rectangle[2]
            if rectangle[3] > max_axis_y:
                max_axis_y = rectangle[3]

            areas.append((rectangle[3] - rectangle[1]) * (rectangle[2] - rectangle[0]))


        target_area = (max_axis_y - min_axis_y) * (max_axis_x - min_axis_x)

        return target_area == sum(areas)

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]
print Solution().isRectangleCover(rectangles)
