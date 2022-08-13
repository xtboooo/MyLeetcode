"""
绘图机器的绘图笔初始位置在原点(0,0)
机器启动后按照以下规则来进行绘制直线
1. 尝试沿着横线坐标正向绘制直线
  直到给定的终点E
2. 期间可以通过指令在纵坐标轴方向进行偏移
offsetY为正数表示正向偏移,为负数表示负向偏移

给定的横坐标终点值E 以及若干条绘制指令
请计算绘制的直线和横坐标轴以及x=E的直线组成的图形面积
输入描述:
首行为两个整数N 和 E
表示有N条指令,机器运行的横坐标终点值E
接下来N行 每行两个整数表示一条绘制指令x offsetY
用例保证横坐标x以递增排序的方式出现
且不会出现相同横坐标x
取值范围:
  0<N<=10000
  0<=x<=E<=20000
  -10000<=offsetY<=10000

输出描述:
  一个整数表示计算得到的面积 用例保证结果范围在0到4294967295之内
示例1:
  输入:
    4 10
    1 1
    2 1
    3 1
    4 -2
  输出:
    12

  示例2:
  输入:
    2 4
    0 1
    2 -2
  输出:
    4
"""
n, end = list(map(int, input().split()))
cmds = (list(map(int, input().split())) for _ in range(n))
ans = pre = y = 0
for lr, ud in cmds:
    ans += abs(y) * (lr - pre)
    pre = lr
    y += ud
ans += abs(y) * (end - pre)
print(ans)

"""
给定两个字符集合
一个是全量字符集
一个是已占用字符集
已占用字符集中的字符不能再使用
要求输出剩余可用字符集

输入描述
1. 输入一个字符串 一定包含@
@前为全量字符集  @后的为已占用字符集
2. 已占用字符集中的字符
一定是全量字符集中的字符
字符集中的字符跟字符之间使用英文逗号隔开
3. 每个字符都表示为字符+数字的形式
用英文冒号分隔
比如a:1标识一个a字符
4. 字符只考虑英文字母，区分大小写
数字只考虑正整型 不超过100
5. 如果一个字符都没被占用 @标识仍存在
例如 a:3,b:5,c:2@

输出描述：
输出可用字符集
不同的输出字符集之间用回车换行
注意 输出的字符顺序要跟输入的一致
不能输出b:3,a:2,c:2
如果某个字符已全部占用 则不需要再输出

示例一：
输入
a:3,b:5,c:2@a:1,b:2
输出
a:2,b:3,c:2
说明：
全量字符集为三个a，5个b，2个c
已占用字符集为1个a，2个b
由于已占用字符不能再使用
因此剩余可用字符为2个a，3个b，2个c
因此输出a:2,b:3,c:2
"""
all, used = input().split("@")
d = {s.split(":")[0]: int(s.split(":")[1]) for s in all.split(",")}
for s in used.split(","):
    d[s.split(":")[0]] -= int(s.split(":")[1])
print(",".join(f"{k}:{v}" for k, v in d.items() if v > 0))

"""
有一种简易压缩算法：针对全部为小写英文字母组成的字符串，
将其中连续超过两个相同字母的部分压缩为连续个数加该字母
其他部分保持原样不变.
例如字符串aaabbccccd  经过压缩变成字符串 3abb4cd
请您编写解压函数,根据输入的字符串,
判断其是否为合法压缩过的字符串
若输入合法则输出解压缩后的字符串
否则输出字符串"!error"来报告错误

输入描述
输入一行，为一个ASCII字符串
长度不超过100字符
用例保证输出的字符串长度也不会超过100字符串

输出描述
若判断输入为合法的经过压缩后的字符串
则输出压缩前的字符串
若输入不合法 则输出字符串"!error"

示例一：
输入
4dff
输出
ddddff
说明
4d扩展为4个d ，故解压后的字符串为ddddff

示例二
输入
    2dff
输出
    !error
说明
    2个d不需要压缩 故输入不合法

示例三
输入
4d@A
输出
!error
说明
    全部由小写英文字母做成的字符串，压缩后不会出现特殊字符@和大写字母A
    故输入不合法
"""


def un_zip(string: str) -> str:
    left = right = 0
    lst = []
    while right < len(string):
        if string[left].isdigit():
            right += 1
            if string[right].isalpha():
                lst.append(f"{string[right]}" * int(string[left]))
                right += 1
                left = right
        else:
            lst.append(string[right])
            right += 1
            left = right
    unzip_string = "".join(lst)
    if not unzip_string.isalpha():
        return "!error"
    else:
        return unzip_string


print(un_zip(input()))


"""
给你两个字符串t和p
    要求从t中找到一个和p相同的连续子串
    并输出该子串第一个字符的下标
    输入描述
        输入文件包括两行 分别表示字符串t和p
        保证t的长度不小于p
        且t的长度不超过1000000
        p的长度不超过10000
    输出描述
        如果能从t中找到一个和p相等的连续子串,
        则输出该子串第一个字符在t中的下标
        下标从左到右依次为1,2,3,...；
        如果不能则输出 "No"
        如果含有多个这样的子串
        则输出第一个字符下标最小的

     示例一：
        输入：
         AVERDXIVYERDIAN
         RDXI
        输出
         4
"""
t = input()
p = input()
if t.find(p) != -1:
    print(t.find(p) + 1)
else:
    print("No")
