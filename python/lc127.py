#https://leetcode.com/discuss/78093/python-bfs-solution

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """

        queue = [(beginWord, 1)]
        visited = set()

        while queue:
            word, level = queue.pop(0)
            if word == endWord:
                return level

            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = word[:i] + j + word[i+1:]
                    if tmp not in visited and tmp in wordList:
                        queue.append((tmp, level+1))
                        visited.add(tmp)
        return 0

