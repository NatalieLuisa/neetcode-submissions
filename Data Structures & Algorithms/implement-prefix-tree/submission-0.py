class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            """if the character is not in children dictionary 
            then we add that character c and create a TrieNode"""
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # if that character already exist then we just update that node
            cur= cur.children[c]
        # cur is at last c of word so now we mark it to true
        cur.endOfWord  = True         
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        #very effient compared to other data structures
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True