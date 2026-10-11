'''
list of strings = ["Hello3#", "102!World$$"]

encoding - use length as my delimiter 
caveat - need to know what is a number

              l
               i
encoded_str = 7#Hello3#11#102!World$$
prefixed by length + #
decoding:
    iterate through
        if hash is found:
            length = prefix until hash
            for i in range(length):
                iterate through
            add to list
'''
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ""
        for elem in strs:
            encoded_str += str(len(elem)) + "#" + elem
        # print(encoded_str)
        return encoded_str
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        strs = []
        i = 0
        l = 0
        currlen = ""
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            strs.append(s[j+1: j+1+length])
            i = j+1+length 
        return strs

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))