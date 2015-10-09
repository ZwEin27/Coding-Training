class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        elem = 0;
        count = 0;
        for i in range(0, len(nums)):
            if count == 0:
                elem = nums[i];
                count = 1;
            else:
                if elem == nums[i]:
                    count += 1;
                else:
                    count -= 1;     # deleted with current elem, so it's not existed yet, and begin from next
        return elem;








        # if len(nums) == 0:
        #     return 0;
        # if len(nums) <= 2:
        #     return nums[0];

        # numslen = len(nums);
        # idx1 = 0;
        # idx2 = numslen - 1;
        
        # while 1:
        #     if idx1 >= numslen or idx2 < 0:
        #         break;

        #     num_one = nums[idx1];
        #     num_two = nums[idx2];
        #     # print num_one
        #     # print num_two
        #     if num_one == num_two:
        #         idx2 -= 1;
        #     else:
        #         nums.pop(idx1);
        #         nums.pop(idx2-1);
        #         print nums
        #         idx2 -=2;

        # return nums[0];


        # idx = 0;
        # while 1:
        #     if idx + 1 >= len(nums):
        #         break;
        #     num_one = nums[idx];
        #     num_two = nums[idx+1];
        #     print num_one
        #     print num_two
        #     if num_one != num_two:
        #         del nums[idx];
        #         del nums[idx];
        #     else:
        #         idx += 1;

        # return nums[0];

            