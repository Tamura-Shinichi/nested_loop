"""
2重ループの例 (Double Loop Example)
Based on: https://ai-trend.jp/programming/python/nest-for/
"""

# 例1: 九九の表を出力する (Example 1: Multiplication table)
print("=== 九九の表 (Multiplication Table) ===")
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} × {j} = {i * j:2d}", end="  ")
    print()  # 改行

print()

# 例2: マトリックス形式で表示 (Example 2: Display in matrix format)
print("=== マトリックス形式 (Matrix Format) ===")
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i * j:3d}", end=" ")
    print()  # 改行

print()

# 例3: パターン表示 (Example 3: Pattern display)
print("=== パターン表示 (Pattern Display) ===")
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()  # 改行
