class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
        w = valueDiff + 1 

        def bucket_id(num):
            return num // w  

        for i, num in enumerate(nums):
            bid = bucket_id(num)

            if bid in buckets:
                return True
            if bid - 1 in buckets and abs(num - buckets[bid - 1]) <= valueDiff:
                return True
            if bid + 1 in buckets and abs(num - buckets[bid + 1]) <= valueDiff:
                return True

            buckets[bid] = num

            if i >= indexDiff:
                del buckets[bucket_id(nums[i - indexDiff])]

        return False