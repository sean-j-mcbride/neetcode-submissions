class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False



class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children:
                        if child and dfs(i + 1, child):
                            return True
                    return False
                else:
                    idx = ord(c) - ord("a")
                    if curr.children[idx] == None:
                        return False
                    curr = curr.children[idx]
            return curr.endOfWord
        
        return dfs(0, self.root)
        
