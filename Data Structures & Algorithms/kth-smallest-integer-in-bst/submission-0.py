class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        cnt = 0

        while curr or stack:

            # go all the way left
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            cnt += 1

            if cnt == k:
                return curr.val

            curr = curr.right