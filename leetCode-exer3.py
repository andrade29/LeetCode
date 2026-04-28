'''3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        lista_A = [] #lista para adicionar as substrings
        maior_visto = 0 #controle de substring

        for elem in s: #percorre a string recebida 
            while elem in lista_A: 
                lista_A.pop(0)

            lista_A.append(elem)
            if len(lista_A) > maior_visto: #verificar o tamanho da maior substring
                maior_visto = len(lista_A)
        return maior_visto
