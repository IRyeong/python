#! /usr/bin/env python3
"""문제 출처 : https://leetcode.com/problems/valid-palindrome/"""

import re

# ------------------------------------------------------
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s에 있는 모든 문자를 소문자로 바꾼다.
        s = s.lower()
        # 정규 표현식을 사용하여, s에 있는 문자들 중 a-z나 0-9 사이의 알파벳이나 숫자가 아닌 경우 모두 제거한다.
        s = re.sub("[^a-z0-9]", "", s)
        # 정제된 s와 s를 거꾸로 한 것이 서로 같으면 True, 다르면 False를 리턴한다.
        return s == s[::-1]


# ------------------------------------------------------
def main():
    text = input("Input : ")
    answer = Solution()
    print(answer.isPalindrome(text))


# ------------------------------------------------------
if __name__ == "__main__":
    main()
