#! /usr/bin/env python3
"""문제 출처 : https://leetcode.com/problems/reverse-string/"""

from typing import List

# ------------------------------------------------------
class Solution:
    def __init__(self, s):
        self.s = s

    def reverseString(self, s: List[str]) -> None:
        # 투 포인터 방식으로 접근한다.
        right = len(s) - 1
        left = 0
        # 오른쪽 포인터가 왼쪽 포인터보다 계속 오른쪽에 있는 동안 스왑한다.
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def returnList(self):
        self.reverseString(self.s)
        print(self.s)


# ------------------------------------------------------
def main():
    input_list = [x for x in input("Input : ").split('"')]
    input_list[:] = input_list[1:-1]
    input_list[:] = input_list[::2]
    answer = Solution(input_list)
    answer.returnList()


# ------------------------------------------------------
if __name__ == "__main__":
    main()
