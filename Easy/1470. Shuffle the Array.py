class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        c = []
        a = nums[0:n]
        b = nums[n:len(nums)]
        for i in range(0,n):
            c.append(a[i])
            c.append(b[i])
        return c
        