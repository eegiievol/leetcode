class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        # words = set(wordDict)

        slen = len(s)
        for i in range(slen):
            for word in wordDict:
                wordLen = len(word)
                if i < wordLen - 1:
                    continue
                if dp[i-wordLen+1]==1 and s[i-wordLen+1:i+1]==word:
                    dp[i+1] = 1
        
        return dp[-1]
        
