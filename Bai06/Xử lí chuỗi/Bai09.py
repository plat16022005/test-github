def longest_unique_substring(s):
    start = 0
    max_len = 0
    max_substring = ""
    used_chars = {}
    for i, char in enumerate(s):
        if char in used_chars and start <= used_chars[char]:
            start = used_chars[char] + 1
        else:
            current_len = i - start + 1
            if current_len > max_len:
                max_len = current_len
                max_substring = s[start:i+1]
        used_chars[char] = i
    return max_substring, max_len
s = str(input())
result, length = longest_unique_substring(s)
print(f"Xâu con dài nhất không chứa ký tự lặp: '{result}' với độ dài: {length}")