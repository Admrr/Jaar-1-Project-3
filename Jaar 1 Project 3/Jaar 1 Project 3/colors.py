# Create color
def grey(): return "#999999"

# Return hex
def rgb_to_hex(result, base, cap, reversed):
    mod = result/cap
    if reversed:
        r = int((1 - mod) * base[0])
        g = int((1 - mod) * base[1])
        b = int((1 - mod) * base[2])
    else:
        r = int(base[0] * mod)
        g = int(base[1] * mod)
        b = int(base[2] * mod)
    return "#%02x%02x%02x" % (r, g, b)