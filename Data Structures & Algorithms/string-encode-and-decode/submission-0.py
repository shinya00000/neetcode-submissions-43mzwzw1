class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_parts = []
        for s in strs:
            # format: length + delimiter + content
            encoded_parts.append(f"{len(s)}#{s}")
        return "".join(encoded_parts)
    def decode(self, s: str) -> List[str]:
        i = 0
        decode_parts = []
        while i<len(s):
            # Find the delimiter to determine how long the next segment is
            j = s.find('#', i)
            length = int(s[i:j])
            # Extract exactly 'length' characters after the delimiter
            content = s[j + 1 : j + 1 + length]
            decode_parts.append(content)
            # Update pointer to start of next segment
            i = j + 1 + length
        return decode_parts