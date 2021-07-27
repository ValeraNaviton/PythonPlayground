#https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/submissions/

class Solution:
        def numberOfSteps(self, num: int) -> int:

            steps = 0

            while num != 0:
            #print("Num = %d"% (num))
                steps = steps + 1
                if num % 2 == 0:
                    num = num / 2
                elif num % 2 != 0:
                    num = num - 1

            return steps
