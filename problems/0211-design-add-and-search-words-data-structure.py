# LeetCode 211 - Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/
#
# ✅ Problem:
# Design a data structure that supports:
#   - addWord(word): store a word
#   - search(word): search a pattern where '.' can match any single character
#
# 📚 Pattern:
# Trie (Prefix Tree) + DFS backtracking for wildcard search
#
# 🔍 Core Idea:
# - Use a Trie to store words character by character.
# - Each node:
#     - children: map char -> next TrieNode
#     - is_end: marks end of a valid word
# - For search:
#     - Normal char: follow that child if it exists.
#     - '.' wildcard: branch out and try ALL children (DFS).
#
# 🧠 Memory Hook:
# - addWord → walk trie, create nodes, mark is_end at final char
# - search:
#     - if i == len(word) → return node.is_end
#     - if char != '.' → must exist in children → dfs(next, i+1)
#     - if char == '.' → try ALL children → any(dfs(child, i+1)) == True
#
# ✅ Time Complexity:
#   - addWord:  O(L)          (L = length of word)
#   - search:
#       - Best/avg: O(L)
#       - Worst (many '.' and branching): O(α^L), α = alphabet size (e.g., 26)
#
# ✅ Space Complexity:
#   - O(N * L) for total characters stored across all words
#   N = number of words stored, L = length of each word
#
# 📌 Common Gotchas:
# - Forgetting to check node.is_end only when i == len(word) in DFS.
# - For '.', you MUST explore all children and return True on the first match.
# - Don’t accidentally reuse a single index variable globally; pass `i` into dfs.
# - Remember to mark node.is_end = True only at the end of addWord.


class TrieNode:
    def __init__(self):
        # children: char -> TrieNode
        self.children = {}
        # is_end: does a word end at this node?
        self.is_end = False


class WordDictionary:

    def __init__(self):
        # 🌱 Initialize root of Trie
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Add a word into the data structure.

        Steps:
        1) Start from root.
        2) For each char:
            - If child doesn't exist, create it.
            - Move node to that child.
        3) After last char, mark node.is_end = True.
        """
        node = self.root

        # 1️⃣ Walk through characters of the word
        for char in word:
            # 2️⃣ Create child node if missing
            if char not in node.children:
                node.children[char] = TrieNode()
            # 3️⃣ Move to next node
            node = node.children[char]

        # 4️⃣ Mark the end of a valid word
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Search for a pattern where '.' can match any character.

        DFS(node, i) meaning:
          - We are currently at Trie node `node`
          - We are trying to match word[i:]

        Steps:
        1) Base case: if i == len(word):
            - return node.is_end (only True if we ended on a word)
        2) If word[i] == '.':
            - Try ALL children:
                if any dfs(child, i+1) is True → return True
            - If none match → return False
        3) Else (normal char):
            - If char not a child → False
            - Else → dfs(child[char], i+1)
        """

        def dfs(node: TrieNode, s: str, i: int) -> bool:
            # 1️⃣ If we've consumed all characters, check if it's a valid word end
            if i == len(s):
                return node.is_end

            ch = s[i]

            # 2️⃣ Wildcard: try all children
            if ch == '.':
                for child in node.children.values():
                    if dfs(child, s, i + 1):
                        return True
                # No child path worked
                return False

            # 3️⃣ Normal character: must exist in children
            if ch not in node.children:
                return False

            # 4️⃣ Continue DFS with the matched child
            return dfs(node.children[ch], s, i + 1)

        # 🚀 Start DFS from root at index 0
        return dfs(self.root, word, 0)


# ---------------------------------------------------------------------------
# 🔄 Example Usage & Dry Run (for mental model)
# ---------------------------------------------------------------------------
# wd = WordDictionary()
# wd.addWord("bad")
# wd.addWord("dad")
# wd.addWord("mad")
#
# Search examples:
# - wd.search("pad") → False
# - wd.search("bad") → True
# - wd.search(".ad") → True
# - wd.search("b..") → True
#
# Dry run: wd.search(".ad")
#   dfs(root, ".ad", 0), ch='.'
#     - ch == '.' → try all root children: 'b', 'd', 'm'
#     1) child 'b':
#          dfs(node('b'), ".ad", 1), ch='a'
#          'a' in children → dfs(node('a'), ".ad", 2)
#          dfs(node('a'), ".ad", 2), ch='d'
#          'd' in children → dfs(node('d'), ".ad", 3)
#          dfs(node('d'), ".ad", 3), i == len(s) → return node.is_end (True)
#        → bubble up True → overall search(".ad") == True ✅
#
# This branching on '.' and strict is_end check at the end
# are the two key behaviors to remember.