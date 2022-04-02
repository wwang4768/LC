# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def shortestToChar(self, s: str, c: str) -> List[int]:
    occur = []
    result = []

    for i in range(len(s)):
        if s[i] == c:
            occur.append(i)

    for j in range(len(s)):
        min = len(s)
        for k in range(len(occur)):
            temp = abs(j - occur[k])

            if temp < min:
                min = temp
        result.append(min)
    return result


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
