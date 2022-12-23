class Solution:
    def average(self, salary: List[int]) -> float:
        if len(salary) <= 3:
            if len(salary) < 3:
                return (sum(salary)/2)
            if len(salary) == 3:
                salary.sort()
                return salary[1]
        i = 0
        Sum = 0
        get_min = min(salary)
        get_max = max(salary)
        

        while i <= len(salary)-1:
            if salary [i] > get_min and salary [i] < get_max:
                Sum += salary[i]
                i += 1
            else:
                i += 1
        return (Sum / (len(salary)-2