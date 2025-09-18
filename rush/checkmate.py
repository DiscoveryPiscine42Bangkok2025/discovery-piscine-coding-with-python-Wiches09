def checkmate(board: str):

    rows = board.strip().splitlines()
    if not rows:
        print("Failed")
        return

    n_rows = len(rows)
    # check square
    if any(len(r) != n_rows for r in rows):
        print("Failed")
        return

    # normalize (upper case and replace other to ".")
    allowed = set("PBRQK")
    grid = []
    king_count = 0
    for r in rows:
        row = []
        for ch in r:
            cu = ch.upper()
            if cu in allowed:
                row.append(cu)
                if cu == "K":
                    king_count += 1
            else:
                row.append('.')
        grid.append(row)

    if king_count != 1:
        print("Failed")
        return

    # find King
    kr = kc = None
    for i in range(n_rows):
        for j in range(n_rows):
            if grid[i][j] == 'K':
                kr = i
                kc = j
                break
        if kr is not None:
            break

# Pawn
    for dc in (-1, 1):
        r, c = kr + 1, kc + dc
        if 0 <= r < n_rows and 0 <= c < n_rows and grid[r][c] == 'P':
            print("Success")
            return

# +
    straight_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dr, dc in straight_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < n_rows and 0 <= c < n_rows:
            ch = grid[r][c]
            if ch != '.':  # first obstacle
                if ch == 'R' or ch == 'Q':
                    print("Success")
                    return
                break
            r += dr
            c += dc


# X
    diag_dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dr, dc in diag_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < n_rows and 0 <= c < n_rows:
            ch = grid[r][c]
            if ch != '.':
                if ch == 'B' or ch == 'Q':
                    print("Success")
                    return
                break
            r += dr
            c += dc

    print("Failed")
