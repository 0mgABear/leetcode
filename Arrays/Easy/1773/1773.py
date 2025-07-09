class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        output: int = 0
        for item in items:
            if item[0] == ruleValue and ruleKey == "type": 
                output +=1
            elif item[1] == ruleValue and ruleKey == "color": 
                output +=1
            elif item[2] == ruleValue and ruleKey == "name": 
                output +=1
        return output
