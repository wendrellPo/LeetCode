#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(0)  # Nó fictício
        current = dummy
        
        while l1 or l2 or carry:
            # Pega o valor dos nós atuais de l1 e l2 (ou 0 se a lista já terminou)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calcula a soma dos valores mais o carry
            total = val1 + val2 + carry
            carry = total // 10  # Atualiza o carry
            new_val = total % 10  # Valor do dígito atual
            
            # Adiciona o novo valor na lista resultante
            current.next = ListNode(new_val)
            current = current.next
            
            # Avança os nós de l1 e l2 (se houver)
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next  # Retorna a lista ligada resultante (ignora o nó fictício)
        
# @lc code=end

