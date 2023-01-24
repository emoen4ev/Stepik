n, z_1, z_2 = int(input()), complex(input()), complex(input())

z_1_c, z_2_c = z_1.conjugate(), z_2.conjugate()

result = z_1 ** n + z_2 ** n + z_1_c ** n + z_2_c ** (n + 1)

print(result)