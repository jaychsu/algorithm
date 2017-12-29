class Solution:
    """
    @param: words: an array of string
    @param: k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        if not words or not k:
            return []

        F = {}
        for word in words:
            F[word] = F.get(word, 0) + 1

        W = [(freq, word) for word, freq in F.items()]
        W.sort(key=lambda item: (-item[0], item[1]))

        return [W[i][1] for i in range(k)]
