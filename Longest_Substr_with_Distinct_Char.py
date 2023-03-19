def longestSubstrDistinctChars(s):
    if len(s) == 0:
        return 0
    n = len(s)
    st = set()
    leng = 1
    st.add(s[0])
    i = 1
    maxLen = 0
    while i < n:
        # check if consiqutive chars are distinct and non repeating
        if s[i] != s[i - 1] and s[i] not in st:
            st.add(s[i])
            leng += 1
            i += 1
            # back up the max length
            if leng > maxLen:
                maxLen = leng
        else:
            # move forward for repeating chars
            if leng == 1:
                i += 1
            else:
                # reset the substring and set the pivot for next sub string
                st.clear()
                i = i - leng + 1
                leng = 0
    return max(maxLen, leng)