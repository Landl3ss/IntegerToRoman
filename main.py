class Solution:
    def intToRoman(self, num: int) -> str:
        rnumbers = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        lengths = [10 ** f for f in range(len(str(num)) - 1, -1, -1)]
        roman = ''
        for i in lengths:
            e = num // i
            while e > 0:
                if e == 9:
                    e -= 9
                    num -= 9 * i
                    roman += rnumbers[i]
                    roman += rnumbers[i * 10]
                elif e >= 5:
                    if 5 * i in rnumbers:
                        e -= 5
                        num -= 5 * i
                        roman += rnumbers[5*i]
                elif e == 4:
                    e -= 4
                    num -= 4 * i
                    roman += rnumbers[i]
                    roman += rnumbers[5 * i]
                else:
                    e -= 1
                    num -= i
                    roman += rnumbers[i]

        return roman