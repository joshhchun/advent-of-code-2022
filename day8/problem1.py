trees = [[int(z) for z in y.rstrip()] for y in open("input.txt").readlines()]
length = len(trees)
visible = set()

def cond(r, c, tallest):
    if trees[r][c] > tallest:
        visible.add((r, c))
        return trees[r][c]
    return -1

def count_visible_trees():
    # East/west
    for r in range(length):
        tallest = -1
        for c in range(length):
            tallest = max(tallest, cond(r, c, tallest))
        tallest = -1
        for c in reversed(range(length)):
            tallest = max(tallest, cond(r, c, tallest))

    # Nort/south
    for c in range(length):
        tallest = -1
        for r in range(length):
            tallest = max(tallest, cond(r, c, tallest))
        tallest = -1
        for r in reversed(range(length)):
            tallest = max(tallest, cond(r, c, tallest))

count_visible_trees()
print(len(visible))
