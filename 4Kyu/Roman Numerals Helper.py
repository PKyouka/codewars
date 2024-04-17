class RomanNumerals:
    roman_dict = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }
    @staticmethod
    def to_roman(val : int) -> str:
        roman_num = ''
        for roman, num in sorted(RomanNumerals.roman_dict.items(), key=lambda x: x[1], reverse=True):
            while val >= num:
                roman_num += roman
                val -= num
        return roman_num

    @staticmethod
    def from_roman(roman_num : str) -> int:
        val = 0
        while roman_num:
            for roman, num in RomanNumerals.roman_dict.items():
                if roman_num.startswith(roman):
                    val += num
                    roman_num = roman_num[len(roman):]
                    break
        return val
    
print(RomanNumerals.to_roman(1000)) # M
print(RomanNumerals.from_roman('M')) # 1000
print(RomanNumerals.to_roman(1990)) # MCMXC
print(RomanNumerals.from_roman('MCMXC')) # 1990
print(RomanNumerals.to_roman(2008)) # MMVIII