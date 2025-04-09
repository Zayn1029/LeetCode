class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}
        
        def backtrack(start):
            if start == len(s):
                return [""]
            
            if start in memo:
                return memo[start]
            
            result = []
            
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:

                    sub_sentences = backtrack(end)
                    
                    for sub in sub_sentences:

                        if sub:
                            result.append(word + " " + sub)
                        else:
                            result.append(word)
            
            memo[start] = result
            return result
        
        return backtrack(0)