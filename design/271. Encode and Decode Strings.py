'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
'''

class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs:
            leng = str(len(string))
            encoded.append('0'*(5-len(leng))+leng)
            encoded.append(string)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i<len(s):
            #capture length
            le = int(s[i:i+5])
            i += 5
            #capture string
            decoded.append(s[i:i+le])
            i += le
        return decoded


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
