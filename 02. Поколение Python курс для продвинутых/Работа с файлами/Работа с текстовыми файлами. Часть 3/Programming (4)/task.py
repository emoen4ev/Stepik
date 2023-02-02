colors = []
goats = []
with open("goats.txt", "r") as f:
    lines = f.readlines()
    # print(lines)
    for i, line in enumerate(lines):
        line = line.strip()
        if line == "COLOURS":
            colors = [x.strip() for x in lines[i+1:]]
        elif line == "GOATS":
            goats = [x.strip() for x in lines[i+1:]]
    # print(colors)
    # print(goats)

color_count = {}
for color in colors:
    color_count[color] = goats.count(color)
# print(color_count)

with open("answer.txt", "w") as f:
    for color, count in sorted(color_count.items()):
        if count > len(goats) * 0.07:
            f.write(f"{color}\n")