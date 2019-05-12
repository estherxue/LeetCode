class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    is_odd = (len(nums1) + len(nums2)) % 2 == 1
    return self.findMedianSortedArrayHelper(nums1, nums2, (len(nums1) + len(nums2)) // 2 + int(is_odd), is_odd)

  def findMedianSortedArrayHelper(self, nums1, nums2, k, is_odd):
    if not nums1 or not nums2:
      if is_odd:
        return float((nums1 + nums2)[k - 1])
      else:
        return float(sum((nums1 + nums2)[k - 1:k + 1]) / 2)
    if k == 1:
      if is_odd:
        return float(min(nums1[0], nums2[0]))
      else:
        if isinstance(nums1, int):
          nums1 = [nums1]
        if isinstance(nums2, int):
          nums2 = [nums2]
        return float(sum(sorted(nums1[:2] + nums2[:2])[:2]) / 2)
    half_k = int(k / 2)
    pos_1 = min(len(nums1), half_k) - 1
    pos_2 = min(len(nums2), half_k) - 1
    if nums1[pos_1] <= nums2[pos_2]:
      return self.findMedianSortedArrayHelper(nums1[pos_1 + 1:], nums2, k - pos_1 - 1, is_odd)
    else:
      return self.findMedianSortedArrayHelper(nums1, nums2[pos_2 + 1:], k - pos_2 - 1, is_odd)



