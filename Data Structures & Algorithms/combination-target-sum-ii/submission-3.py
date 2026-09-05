class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(index, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target or index >= len(candidates):
                return
            
            path.append(candidates[index])
            backtrack(index + 1, path, total + candidates[index])
            path.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, path, total)
                
        backtrack(0, [], 0)
        return res