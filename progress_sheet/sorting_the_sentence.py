class Solution:
    def sortSentence(self, s: str) -> str:
        a = list(s.split(' '))
        sort_arr = []
        for i in range(1,(len(a)+1)):
            for j in range(len(a)):
                if i == int(a[j][-1]):
                    x = a[j]
                    y = x[:-1]
                    sort_arr.append(y)
                    break;
        return " ".join(sort_arr)