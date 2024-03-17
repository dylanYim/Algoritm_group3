N, R, C = map(int,input().split())

def solve(n, r, c):
    if r == 0 and c == 0: return 0
    elif r == 0 and c == 1: return 1
    elif r == 1 and c == 0: return 2
    elif r == 1 and c == 1: return 3
    else:
        q_len = 2 ** (n - 1)
        q_size = q_len ** 2
        if r <= q_len - 1 and c <= q_len-1:
            return solve(n-1, r, c)
        elif r <= q_len - 1 and c > q_len - 1:
            return q_size + solve(n - 1, r, c - q_len)
        elif r > q_len - 1 and c <= q_len - 1:
            return 2 * q_size + solve(n - 1, r - q_len, c)
        elif r > q_len - 1 and c > q_len - 1:
            return 3 * q_size + solve(n - 1, r - q_len, c - q_len)

print(solve(N, R, C))

