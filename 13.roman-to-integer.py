#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dicionário dos símbolos romanos
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        total = 0
        prev_value = 0
        
        for char in s:
            current_value = roman_to_int[char]
            
            # Se o valor atual for maior que o anterior, subtrai o valor anterior duas vezes e soma o atual
            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value
                
            # Atualiza o valor anterior para a próxima iteração
            prev_value = current_value
        
        return total
    
#Complexidade de Tempo: O(n)
#Complexidade de Espaço: O(1)

# @lc code=end

