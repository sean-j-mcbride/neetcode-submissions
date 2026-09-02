class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = defaultdict(list)
        output = []

        for i, word in enumerate(strs):
            sorted_word = "".join(sorted(list(word)))
            h_map[sorted_word].append(i)
        
        for key, value in h_map.items():
            temp = []
            for idx in value:
                temp.append(strs[idx])
            output.append(temp)
        
        return output