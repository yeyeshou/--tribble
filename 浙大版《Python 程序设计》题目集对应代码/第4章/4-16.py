# 输入三角形的三边，判断是否能构成三角形。若能构成输出yes，否则输出no。
#
# 输入格式:
# 在一行中直接输入3个整数，3个整数之间各用一个空格间隔，没有其他任何附加字符。
#
# 输出格式:
# 直接输出yes或no，没有其他任何附加字符。
l = list(map(int, input().split()))
print('yes' if 2*max(l) < sum(l) else 'no')
