# Given a string that contains properly nested parentheses,
# this program returns the decoded version of the string.
# All characters inside each pair of parentheses should be reversed.
# Parentheses should be removed from the final result.
# If parentheses are nested, the innermost pair should be reversed first.

def decode(s):
    char0_indices = []
    char1_indices = []

    for i in range(len(s)):
        if s[i] == '(':
            char0_indices.append(i)

        if s[i] == ')':
            char1_indices.append(i)

    substring0 = s[char0_indices[0]:char1_indices[0] + 1]

    char2_indices = []
    char3_indices = []

    for i in range(len(substring0)):
        if substring0[i] == '(':
            char2_indices.append(i)

        if substring0[i] == ')':
            char3_indices.append(i)

    substring1 = substring0[char2_indices[-1]:char3_indices[0] + 1]

    new_substring = ''.join(list(reversed(substring1[1:-1])))

    s = s.replace(substring1, new_substring)

    while '(' in s:
        s = decode(s)

    return s


print(decode("(f(b(dc)e)a)"))
print(decode("((is?)(a(t d)h)e(n y( uo)r)aC)"))
print(decode("f(Ce(re))o((e(aC)m)d)p"))
