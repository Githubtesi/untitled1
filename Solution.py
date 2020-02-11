class Solution:
    def convertToTitle(self, n):

        # TODO Sample case 1~26
        base = ord("A") - 1

        # A=1 B=2 ....Z=26
        alphabet_size = 26

        # Error
        if n <= 0 or type(n) is not int:
            return None

        # 1の位のみ
        elif 1 <= n and n <= 26:
            ascii_num = base + n
            ascii_char = chr(ascii_num)
            return ascii_char

        # 2の位のみ
        elif 27 <= n and n <= 52:
            mod = n % alphabet_size
            div = n // alphabet_size

            # 　1の位
            one = base + mod
            ascii_one = chr(one)

            # 10の位
            ten = base + div
            ascii_ten = chr(ten)

            # return ten + one
            return ascii_ten + ascii_one
