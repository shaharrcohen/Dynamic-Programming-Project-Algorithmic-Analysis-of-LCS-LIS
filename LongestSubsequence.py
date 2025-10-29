import bisect, ast


def build_lcs_matrix(A: list[int], B: list[int]) -> list[list[int]]:
    """Constructs the LCS table using dynamic programming."""
    n, m = len(A), len(B)
    lcs_table = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:  # Matching elements → move diagonally
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:  # No match → take the max from adjacent cells
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

    return lcs_table


def number_of_lcs(A: list[int], B: list[int]) -> int:
    """Counts the number of distinct longest common subsequences (LCS) between A and B."""
    dp = build_lcs_matrix(A, B)
    lcs_length = dp[len(A)][len(B)]

    lcs_list = all_lcs(A, B, 1000)  # Collect up to 1000 LCS results
    return len(lcs_list)  # Return the count of found sequences


def all_lcs(A: list[int], B: list[int], limit: int) -> list[list[int]]:
    """Finds all LCS subsequences (including duplicates) up to a given limit."""
    dp = build_lcs_matrix(A, B)
    n, m = len(A), len(B)
    lcs_length = dp[n][m]

    if lcs_length == 0:
        return []

    queue = [(n, m, [])]  # BFS queue: (i, j, current LCS path)
    results = []

    while queue and len(results) < limit:
        i, j, path = queue.pop(0)

        if len(path) == lcs_length:
            results.append(path)
            continue

        for x in range(i, 0, -1):
            for y in range(j, 0, -1):
                if A[x - 1] == B[y - 1] and dp[x][y] == lcs_length - len(path):
                    queue.append((x - 1, y - 1, [A[x - 1]] + path))

    return sorted(results, key=lambda seq: [A.index(num) for num in seq])  # Sort by order of appearance in A


def all_unique_lcs(A: list[int], B: list[int], limit: int) -> list[list[int]]:
    """Finds all unique longest common subsequences (LCS) up to a given limit, sorted in ascending order."""
    all_lcs_results = all_lcs(A, B, limit * 2)  # Extract extra to prevent missed sequences

    if not all_lcs_results:
        return []

    unique_sequences = sorted(set(tuple(seq) for seq in all_lcs_results))  # Remove duplicates
    return [list(seq) for seq in unique_sequences[:limit]]  # Return up to `limit` unique LCS results


def length_of_lis(A: list[int], C: list[int]) -> int:
    valid_numbers = [A[i] for i in range(len(A)) if C[i] == 1]
    if not valid_numbers:
        return 0
    lis = []
    for num in valid_numbers:
        pos = bisect.bisect_left(lis, num)
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num
    return len(lis)

def number_of_lis(A: list[int], C: list[int]) -> int:
    allowed = [A[i] for i in range(len(A)) if C[i] == 1]
    if not allowed:
        return 0

    n = len(allowed)
    dp = [1] * n
    count = [1] * n

    for i in range(n):
        for j in range(i):
            if allowed[j] < allowed[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    count[i] = count[j]
                elif dp[j] + 1 == dp[i]:
                    count[i] += count[j]

    L = max(dp)
    total = 0
    for i in range(n):
        if dp[i] == L:
            total += count[i]
    return total

def all_lis(A: list[int], C: list[int], teta: int) -> list[list[int]]:
    allowed = [A[i] for i in range(len(A)) if C[i] == 1]
    if not allowed:
        return []

    n = len(allowed)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if allowed[j] < allowed[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    L = max(dp)
    results = []

    def backtrack(i):
        if dp[i] == 1:
            return [[allowed[i]]]
        res = []
        for j in range(i):
            if allowed[j] < allowed[i] and dp[j] == dp[i] - 1:
                for seq in backtrack(j):
                    res.append(seq + [allowed[i]])
        return res

    for i in range(n):
        if dp[i] == L:
            results.extend(backtrack(i))

    results.sort()
    return results[:teta]

def all_unique_lis(A: list[int], C: list[int], teta: int) -> list[list[int]]:
    all_results = all_lis(A, C, teta * 10)
    unique_results = []
    seen = set()
    for seq in all_results:
        tup = tuple(seq)
        if tup not in seen:
            seen.add(tup)
            unique_results.append(seq)
        if len(unique_results) == teta:
            break
    return unique_results

def safe_input(prompt):
        """ Reads input safely as a list of integers or an empty list. """
        while True:
            try:
                user_input = input(prompt).strip()
                parsed_list = ast.literal_eval(user_input)
                if isinstance(parsed_list, list) and all(isinstance(x, int) for x in parsed_list):
                    return parsed_list
                else:
                    print("Invalid input. Please enter a list of integers, e.g., [1, 2, 3] or [].")
            except (SyntaxError, ValueError):
                print("Invalid input. Please enter a valid list format.")

def main():
    """ Main function to test LCS and LIS functions with user input """

    # Get sequences from user
    A = safe_input("Enter sequence A (as a list, e.g., [1,2,3] or []): ")
    B = safe_input("Enter sequence B (as a list, e.g., [4,5,6] or []): ")
    teta = number_of_lcs(A,B)

    # Compute LCS results
    num_lcs = number_of_lcs(A, B)
    print(f"Number of LCS occurrences: {num_lcs}")

    all_lcs_results = all_lcs(A, B, teta)
    print(f"All LCS sequences (up to {teta}): {all_lcs_results}")

    all_unique_lcs_results = all_unique_lcs(A, B, teta)
    print(f"All unique LCS sequences (up to {teta}): {all_unique_lcs_results}")

    A = safe_input("Enter sequence A (as a list, e.g., [1,2,3]): ")
    # Get sequence C for LIS calculations
    print("The length of C has to be equal to A's length")
    C = safe_input("Enter sequence C (as a binary list, e.g., [1,0,1] or []): ")

    # Compute LIS results
    lis_length = length_of_lis(A, C)
    print(f"Length of LIS: {lis_length}")

    num_lis = number_of_lis(A, C)
    print(f"Number of LIS occurrences: {num_lis}")

    all_lis_results = all_lis(A, C, teta)
    print(f"All LIS sequences (up to {teta}): {all_lis_results}")

    all_unique_lis_results = all_unique_lis(A, C, teta)
    print(f"All unique LIS sequences (up to {teta}): {all_unique_lis_results}")

# Run the main function if executed as a script
if __name__ == "__main__":
    main()
