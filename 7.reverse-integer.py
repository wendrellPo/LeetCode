#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        reversed_num = 0
        sign = -1 if x < 0 else 1  # Determina o sinal do número
        x = abs(x)  # Trabalha com o valor absoluto

        while x != 0:
            digit = x % 10  # Extrai o último dígito
            x //= 10  # Remove o último dígito do número original
            
            # Verifica se a adição do próximo dígito causaria overflow
            if reversed_num > (2**31 - 1) // 10:
                return 0
            
            reversed_num = reversed_num * 10 + digit  # Constrói o número invertido
        
        return sign * reversed_num
        
        
# Complexidade de Tempo: O(log₁₀(x))
# Complexidade de Espaço: O(1)

# @lc code=end

