class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []
        
        while i < len(nums1) and j < len(nums2):
            id1, v1 = nums1[i]
            id2, v2 = nums2[j]
            if id1 == id2:
                result.append([id1, v1 + v2])
                i += 1
                j += 1
            elif id1 < id2:
                result.append([id1, v1])
                i += 1
            else:
                result.append([id2, v2])
                j += 1
        
        result.extend(nums1[i:])
        result.extend(nums2[j:])
        return result