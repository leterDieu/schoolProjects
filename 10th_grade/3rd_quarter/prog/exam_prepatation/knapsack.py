from typing import List


def knapsack_req(capacity: float, weights: List[int], profits: List[int], n: int = -1) -> float:
    if n == -1:
        n = len(weights)

    if not capacity or not n:
        return 0

    item_weight = weights[n - 1]

    if item_weight > capacity:
        return knapsack_req(capacity, weights, profits, n - 1)

    return max(
        profits[n - 1] + knapsack_req(capacity - item_weight, weights, profits, n - 1),
        knapsack_req(capacity, weights, profits, n - 1))


def knapsack_dp(capacity: int, weights: List[int], profits: List[int]) -> int:
    n = len(weights)
    table = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            item_weight = weights[i - 1]
            if item_weight > capacity:
                table[i][j] = table[i - 1][j]
                continue
            table[i][j] = max(
                profits[i - 1] + table[i - 1][j - item_weight],
                table[i - 1][j]
            )

    return table[n][capacity]
