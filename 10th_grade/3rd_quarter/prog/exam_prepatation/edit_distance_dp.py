def edit_distance(s1: str, s2: str) -> int:
    s1_length = len(s1)
    s2_length = len(s2)

    table = [[0] * (s2_length + 1) for _ in range(s1_length + 1)]

    for i in range(1, s2_length + 1):
        table[0][i] = i
    for i in range(1, s1_length + 1):
        table[i][0] = i

    for i in range(s1_length):
        for j in range(s2_length):
            if s1[i] == s2[j]:
                table[i + 1][j + 1] = table[i][j]
                continue
            table[i + 1][j + 1] = 1 + min(
                table[i][j],
                table[i + 1][j],
                table[i][j + 1]
            )

    return table[s1_length][s2_length]
