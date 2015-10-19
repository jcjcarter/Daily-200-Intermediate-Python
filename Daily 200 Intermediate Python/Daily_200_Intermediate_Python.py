_, *data = open("data.txt").read().splitlines()
w, h = len(data[0]), len(data)

for y in range(h):
    for x in range(w):
        c = data[y][x]
        if c != "." and (y-1 == -1 or data[y-1][x] != c) and (x-1 == -1 or data[y][x-1] != c):
            start_x, start_y = x, y
            while x != w and data[y][x] == c :
                x += 1
            while y != h and data[y][x-1] == c: #I've gone over the tile, that's why x-1
                y += 1
            area_w, area_h = x-start_x, y-start_y
            x, y = start_x, start_y
            print("%sx%s tile of character '%s' located at (%s,%s)" % (area_w, area_h, c, start_x, start_y))