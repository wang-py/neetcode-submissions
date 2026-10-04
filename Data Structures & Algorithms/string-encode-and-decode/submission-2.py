class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        delim = "$"
        for string in strs:
            n = len(string)
            output.append(str(n) + delim + string)

        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        print("string is encoded as %s"%s)
        while i < len(s):
            n = []
            while s[i] != "$":
                n += s[i]
                i += 1
            n = ''.join(n)
            print("n as string: %s"%n)
            n = int(n)
            print("n is %d"%n)
            output.append(s[i + 1:i + 1 + n])
            i += n + 1
        
        return output