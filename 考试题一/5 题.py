# 计算1+2+3...+49 的和


def total(s):
    if s == 1:
        return 1
    return total(s - 1) + s
print(total(49))