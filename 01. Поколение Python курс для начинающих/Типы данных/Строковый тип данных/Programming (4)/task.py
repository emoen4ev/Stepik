a, b, c = input(), input(), input()
mn = min(len(a), len(b), len(c))
mx = max(len(a), len(b), len(c))
md = len(a + b + c) - (mn + mx)
if (mx - md) == (md - mn):
    print("YES")
else:
    print("NO")




