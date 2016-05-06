class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # pass
        # nums.sort()

        # time exceed
        # size = len(nums)
        # final_pointer = 0
        # move_pointer = size - 1

        # phase = 0
        # while final_pointer < size - 1:
        #     # print final_pointer, move_pointer

        #     if nums[final_pointer] == phase:
        #         final_pointer += 1
        #     if nums[move_pointer] == phase:
        #         tmp = nums[final_pointer]
        #         nums[final_pointer] = nums[move_pointer]
        #         nums[move_pointer] = tmp
        #     else:
        #         move_pointer -= 1

        #     if final_pointer > move_pointer:
        #         phase += 1
        #         move_pointer = size - 1
        #     # print nums


        size = len(nums)
        hp = 0
        tp = size - 1
        p = 0
        while p < size:
            # print nums
            if nums[p] == 0:
                if p > hp:
                    self.swap(nums, p, hp)
                    hp += 1
                else:
                    p += 1
            elif nums[p] == 2:
                if p < tp:
                    self.swap(nums, p, tp)
                    tp -= 1
                else:
                    p += 1
            else:
                p += 1





    def swap(self, nums, pos1, pos2):
        tmp = nums[pos1]
        nums[pos1] = nums[pos2]
        nums[pos2] = tmp
















