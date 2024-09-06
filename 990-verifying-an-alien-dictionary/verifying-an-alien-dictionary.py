class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderIdx = {ch : idx for idx, ch in enumerate(order)}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            if len(word2) < len(word1) and word1[: len(word2)] == word2:
                return False

            for ch1, ch2 in zip(word1, word2):
                if ch1 != ch2:
                    if orderIdx[ch2] < orderIdx[ch1]:
                        return False
                    break

        return True