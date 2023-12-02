class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        le = 0
        for word in words:
            flag = 1
            for c in word:
                if c not in chars or word.count(c) > chars.count(c):
                    flag = 0
                    break
            if flag == 1:
                le += len(word)
        return le