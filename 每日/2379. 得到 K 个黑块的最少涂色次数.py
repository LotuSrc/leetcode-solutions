class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # 滑动窗口
        # 可以用一个变量来保存
        n = len(blocks)
        ans = 0
        cur = 0
        for i in range(n):
            if i < k:
                cur = cur + int(blocks[i] == 'W')
                ans = cur
            else:
                ans = min(ans, cur - int(blocks[i - k] == 'W') + int(blocks[i] == 'W'))
                cur = cur - int(blocks[i - k] == 'W') + int(blocks[i] == 'W')
        return ans