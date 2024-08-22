#
# @lc app=leetcode id=2469 lang=python
#
# [2469] Convert the Temperature
#

# @lc code=start
class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [kelvin, fahrenheit]
        

# Complexidade de Tempo: O(1)
# Complexidade de Espaço: O(1)

# @lc code=end

