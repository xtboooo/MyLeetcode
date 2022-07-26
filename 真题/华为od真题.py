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


"""
公司用一个字符串来标识员工的出勤信息

  absent:    缺勤
  late:      迟到
  leaveearly:早退
  present:   正常上班

  现需根据员工出勤信息,判断本次是否能获得出勤奖,
  能获得出勤奖的条件如下：
      1.缺勤不超过1次
      2.没有连续的迟到/早退
      3.任意连续7次考勤 缺勤/迟到/早退 不超过3次

   输入描述：
    用户的考勤数据字符串记录条数  >=1
    输入字符串长度 <10000 ;
    不存在非法输入
    如：
     2
     present
     present absent present present leaveearly present absent

    输出描述：
    根据考勤数据字符串
    如果能得到考勤奖输出true否则输出false
    对于输出示例的结果应为
     true false

    示例一：
     输入：
      2
      present
      present present

     输出：
      true true

    示例二
     输入：
      2
      present
      present absent present present leaveearly present absent
     输出：
      true false
"""

n = int(input())
s_list = (input().split() for _ in range(n))
ans = []
for lst in s_list:
    if lst.count("absent") > 1:
        ans.append("false")
        continue
    for i in range(len(lst) - 1):
        a, b = lst[i], lst[i + 1]
        if a in ["late", "leaveearly"] and b in ["late", "leaveearly"]:
            ans.append("false")
            break
    else:
        for i in range(len(lst) - 6):
            tmp = lst[i, i + 7]
            d = e = f = 0
            for j in tmp:
                if j == "absent":
                    d += 1
                elif j == "late":
                    e += 1
                elif j == "leaveearly":
                    f += 1
            if d + e + f > 3:
                ans.append("false")
                break
        else:
            ans.append("true")
print(" ".join(ans))


"""
一个工厂有m条流水线
来并行完成n个独立的作业
该工厂设置了一个调度系统
在安排作业时，总是优先执行处理时间最短的作业
现给定流水线个数m
需要完成的作业数n
每个作业的处理时间分别为 t1,t2...tn
请你编程计算处理完所有作业的耗时为多少
当n>m时 首先处理时间短的m个作业进入流水线
其他的等待
当某个作业完成时，
依次从剩余作业中取处理时间最短的
进入处理

输入描述：
第一行为两个整数(采取空格分隔)
分别表示流水线个数m和作业数n
第二行输入n个整数(采取空格分隔)
表示每个作业的处理时长 t1,t2...tn
0<m,n<100
0<t1,t2...tn<100

输出描述
输出处理完所有作业的总时长

案例
输入
3 7
8 4 3 2 10 15 21
输出
13
说明
先安排时间为2,3,4的三个作业
第一条流水线先完成作业
调度剩余时间最短的作业8
第二条流水线完成作业
调度剩余时间最短的作业10
总共耗时 就是二条流水线完成作业时间13(3+10)

3 9
1 1 1 2 3 4 6 7 8

"""
m, n = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()
if m >= n:
    print(nums[-1])
else:
    sum_time = 0
    current_jobs = nums[0:m]
    completed = 0
    while completed < n - m:
        min_value = current_jobs[0]
        sum_time += min_value
        current_jobs = [x - min_value for x in current_jobs]
        del current_jobs[0]
        current_jobs.append(nums[m + completed])
        completed += 1
    sum_time += current_jobs[-1]

    print(sum_time)

"""
给定一个字符串
只包含大写字母
求在包含同一字母的子串中
长度第K长的子串
相同字母只取最长的子串

输入
第一行 一个子串 1<len<=100
只包含大写字母
第二行为k的值

输出
输出连续出现次数第k多的字母的次数

例子：
输入
        AABAAA
        2
输出
        1
同一字母连续出现最多的A 3次
第二多2次  但A出现连续3次

输入

AAAAHHHBBCDHHHH
3

输出
2

//如果子串中只包含同一字母的子串数小于k

则输出-1
"""
s = input() + "a"
k = int(input())
left = right = 0
d = {}
while right < len(s):
    if s[left] == s[right]:
        right += 1
    else:
        d[s[left]] = max(d.get(s[left], 0), right - left)
        left = right
tmp = sorted(d.items(), key=lambda x: x[1], reverse=True)
if k > len(tmp):
    print(-1)
else:
    print(tmp[k - 1][1])


"""
为了充分发挥Gpu算力，
需要尽可能多的将任务交给GPU执行，
现在有一个任务数组，
数组元素表示在这1s内新增的任务个数，
且每秒都有新增任务，
假设GPU最多一次执行n个任务，
一次执行耗时1s，
在保证Gpu不空闲的情况下，最少需要多长时间执行完成。

输入描述
第一个参数为gpu最多执行的任务个数
取值范围1~10000
第二个参数为任务数组的长度
取值范围1~10000
第三个参数为任务数组
数字范围1~10000

输出描述
执行完所有任务需要多少秒

例子
输入
3
5
1 2 3 4 5
输出
6

说明，一次最多执行3个任务  最少耗时6s

例子2
输入
    4
    5
    5 4 1 1 1
输出
    5

说明，一次最多执行4个任务  最少耗时5s
"""
n = int(input())
length = int(input())
nums = list(map(int, input().split()))

time = 0
more = 0
for num in nums:
    if num + more > n:
        more = num + more - n
    else:
        more = 0
    time += 1
while more > 0:
    more -= n
    time += 1
print(time)

"""
单词接龙的规则是
可用于接龙的单词首字母必须要与前一个单词的尾字母相同
当存在多个首字母相同的单词时
取长度最长的单词
如果长度也相等则取词典序最小的单词
已经参与接龙的单词不能重复使用
现给定一组全部由小写字母组成的单词数组
并指定其中的一个单词为起始单词
进行单词接龙
请输出最长的单词串
单词串是由单词拼接而成 中间没有空格

输入描述：
输入的第一行为一个非负整数
表示起始单词在数组中的索引k  0<=k<=n
第二行输入的是一个非负整数表示单词的个数n
接下来的n行分别表示单词数组中的单词

输出描述：
输出一个字符串表示最终拼接的字符串

示例1：
输入
0
6
word
dd
da
dc
dword
d

输出
worddwordda

说明：
先确定起始单词word
再确定d开头长度最长的单词dword
剩余以d开头且长度最长的由 da dd dc
则取字典序最小的da
所以最后输出worddwordda

示例二：
输入：
4
6
word
dd
da
dc
dword
d
输出：
dwordda
"""

index = int(input())
n = int(input())
words = [input() for _ in range(n)]
ans = words[index]
pass


"""
输入一个英文文章片段
    翻转指定区间的单词顺序，标点符号和普通字母一样处理
    例如输入字符串 "I am a developer."
     区间[0,3]则输出 "developer. a am I"

     输入描述：
     使用换行隔开三个参数
     第一个参数为英文文章内容即英文字符串
     第二个参数为反转起始单词下标，下标从0开始
     第三个参数为结束单词下标，

     输出描述
     反转后的英文文章片段，所有单词之间以一个半角空格分割进行输出

     示例一：
     输入
         I am a developer.
         1
         2
     输出
         I a am developer.

     示例二：
     输入
         Hello world!
         0
         1
     输出
         world! Hello

       说明：
       输入字符串可以在前面或者后面包含多余的空格，
       但是反转后的不能包含多余空格

     示例三：
     输入：
         I am a developer.
         0
         3
     输出
         developer. a am I

       说明：
       如果两个单词见有多余的空格
       将反转后单词间的空格减少到只含一个

      示例四：
      输入
       Hello!
       0
       3
      输出
       EMPTY

       说明：
       指定反转区间只有一个单词，或无有效单词则统一输出EMPTY
"""

s = input().split()
start = int(input())
end = int(input())
if not (0 <= start <= end < len(s)):
    print("EMPTY")
else:
    ans = s[:start] + s[start : end + 1][::-1] + s[end + 1 :]
    print(" ".join(ans))

"""
停车场有一横排车位0代表没有停车,1代表有车.
       至少停了一辆车在车位上,也至少有一个空位没有停车.
       为防止刮蹭,需为停车人找到一个车位
       使得停车人的车最近的车辆的距离是最大的
       返回此时的最大距离

       输入描述:
       1. 一个用半角逗号分割的停车标识字符串,停车标识为0或1,
        0为空位,1为已停车
       2. 停车位最多有100个

       输出描述
       1. 输出一个整数记录最大距离

       示例一:
       输入
       1,0,0,0,0,1,0,0,1,0,1,0,0,1,1,0,0
       输出
       2

       说明
       当车停在第三个位置上时,离其最近的车距离为2(1~3)
       当车停在第四个位置上时,离其最近的车距离为2(4~6)
       其他位置距离为1
       因此最大距离为2

"""
a = input()
nums = ("".join(a.split(","))).split("1")
max_len = 0
for num in nums:
    if num:
        max_len = max(max_len, len(num) - 2)
if max_len <= 0:
    print(1)
else:
    print(max_len)
