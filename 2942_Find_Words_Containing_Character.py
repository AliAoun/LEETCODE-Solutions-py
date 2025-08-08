class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        lst = []
        for i in range(len(words)):
            if x in words[i]:
                lst.append(i)
        return lst
    
    # time complexity: O(n * m) due to iterating through each word and checking for the character,
    #                           where n is the number of words and m is the average length of the words.
    # space complexity: O(n) due to storing the indices of words that contain the character.