def setMax(max: int, new: int):
    if (new > max):
        return new
    else:
        return max

def longest_substring_k_unique(s: str, k: int) -> int:
    max = 0
    for x in range(len(s)):
        count = 0
        charset = set()
        for y in range(x,len(s)):
            charset.add(s[y])
            if len(charset) > k:
                break
            count += 1
            print(count, len(charset))
        max = setMax(max,count)    
    return max
