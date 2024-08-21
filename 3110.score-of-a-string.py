#
# @lc app=leetcode id=3110 lang=python
#
# [3110] Score of a String
#

# @lc code=start
class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        
        for i in range(len(s) - 1):
            
            # Obter o valor ASCII dos caracteres adjacentes
            current_value = ord(s[i])
            next_value = ord(s[i + 1])
            
            # Calcular a diferença absoluta e adicionar ao total
            total += abs(current_value - next_value)
        
        return total

# Complexidade de Tempo: O(n)
# Complexidade de Espaço: O(1)

# @lc code=end

