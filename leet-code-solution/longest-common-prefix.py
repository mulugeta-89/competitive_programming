class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for item in strs:
            while not item.startswith(prefix):
                prefix = prefix[:-1]
        return prefix
        