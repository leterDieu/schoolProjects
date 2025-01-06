def lcs_req(s1: str, s2: str) -> int:
    if not len(s1) or not len(s2):
        return 0

    if s1[-1] == s2[-1]:
        return 1 + lcs_req(s1[:-1], s2[:-1])

    return max(lcs_req(s1, s2[:-1]), lcs_req(s1[:-1], s2))


def lcs_dp(s1: str, s2: str) -> int:
    s1_length = len(s1)
    s2_length = len(s2)
    table = [[0] * (s2_length + 1) for _ in range(s1_length + 1)]

    for i, s1_char in enumerate(s1):
        for j, s2_char in enumerate(s2):
            if s1_char == s2_char:
                table[i + 1][j + 1] = 1 + table[i][j]
                continue
            table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j])

    return table[s1_length][s2_length]


a = 'AGGTAB'
b = 'GXTXAYB'
print(lcs_dp(a, b))
