# Leetcode Premium access so no real testcases to see if things break

# o(n) where n is the size of input_list, space is o(m) where m is the length of the whole list
def encode (input_list: list[str]) -> str:
    encodedstr = ""
    for each in input_list:
        encodedstr += str(len(each)) + each
    return encodedstr

# o(m) time and o(n) space?
def decode (encoded: str) -> list[str]:
    decoded_list = []
    ind = 0
    while ind < len(encoded):
        num = int(encoded[ind])
        decoded_list.append(encoded[ind+1: ind + num + 1])
        ind += num + 1
    return decoded_list

input_list = ["3neet4", "3code2", "lov2e", "y3ou"]
encoded_str = encode(input_list)
output = decode(encoded_str)

print(output)