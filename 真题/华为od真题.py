"""
  给定一个射击比赛成绩单
  包含多个选手若干次射击的成绩分数
  请对每个选手按其最高三个分数之和进行降序排名
  输出降序排名后的选手id序列
  条件如下
    1. 一个选手可以有多个射击成绩的分数，且次序不固定
    2. 如果一个选手成绩少于3个，则认为选手的所有成绩无效，排名忽略该选手
    3. 如果选手的成绩之和相等，则相等的选手按照其id降序排列

   输入描述:
     输入第一行
         一个整数N
         表示该场比赛总共进行了N次射击
         产生N个成绩分数
         2<=N<=100

     输入第二行
       一个长度为N整数序列
       表示参与每次射击的选手id
       0<=id<=99

     输入第三行
        一个长度为N整数序列
        表示参与每次射击选手对应的成绩
        0<=成绩<=100

   输出描述:
      符合题设条件的降序排名后的选手ID序列

   示例一
      输入:
        13
        3,3,7,4,4,4,4,7,7,3,5,5,5
        53,80,68,24,39,76,66,16,100,55,53,80,55
      输出:
        5,3,7,4
      说明:
        该场射击比赛进行了13次
        参赛的选手为{3,4,5,7}
        3号选手成绩53,80,55 最高三个成绩的和为188
        4号选手成绩24,39,76,66  最高三个成绩的和为181
        5号选手成绩53,80,55  最高三个成绩的和为188
        7号选手成绩68,16,100  最高三个成绩的和为184
        比较各个选手最高3个成绩的和
        有3号=5号>7号>4号
        由于3号和5号成绩相等  且id 5>3
        所以输出5,3,7,4
"""


n = int(input())
players = list(map(int, input().split(",")))
scores = list(map(int, input().split(",")))
import collections

d = collections.defaultdict()
for player, score in zip(players, scores):
    d[player].append(score)
res = []
for player, scores in d:
    if len(scores) < 3:
        continue
    res.append((sum(scores.sort()[:3], player)))
res = map(lambda x: x[1], sorted(res))

"""
    输入一个由N个大小写字母组成的字符串
    按照ASCII码值从小到大进行排序
    查找字符串中第K个最小ASCII码值的字母(k>=1)
    输出该字母所在字符串中的位置索引(字符串的第一个位置索引为0)
    k如果大于字符串长度则输出最大ASCII码值的字母所在字符串的位置索引
    如果有重复字母则输出字母的最小位置索引

    输入描述
      第一行输入一个由大小写字母组成的字符串
      第二行输入k k必须大于0 k可以大于输入字符串的长度

    输出描述
      输出字符串中第k个最小ASCII码值的字母所在字符串的位置索引
      k如果大于字符串长度则输出最大ASCII码值的字母所在字符串的位置索引
      如果第k个最小ASCII码值的字母存在重复  则输出该字母的最小位置索引

    示例一
     输入
        AbCdeFG
        3
     输出
        5
     说明
       根据ASCII码值排序，第三个ASCII码值的字母为F
       F在字符串中位置索引为5(0为字符串的第一个字母位置索引)

     示例二
       输入
        fAdDAkBbBq
        4
       输出
        6
       说明
        根据ASCII码值排序前4个字母为AABB由于B重复则只取B的第一个最小位置索引6
        而不是第二个B的位置索引8

"""

s = input()
n = int(input())
if n > len(s) + 1:
    n = len(s) + 1
ans = s.index(sorted(s)[n - 1])


"""
    有一个特殊的五键键盘
    上面有A、Ctrl-C、Ctrl-X、Ctrl-V、Ctrl-A
    A键在屏幕上输出一个字母A
    Ctrl-C将当前所选的字母复制到剪贴板
    Ctrl-X将当前选择的字母复制到剪贴板并清空所选择的字母
    Ctrl-V将当前剪贴板的字母输出到屏幕
    Ctrl-A选择当前屏幕中所有字母
    注意：
      1. 剪贴板初始为空
      2. 新的内容复制到剪贴板会覆盖原有内容
      3. 当屏幕中没有字母时,Ctrl-A无效
      4. 当没有选择字母时Ctrl-C、Ctrl-X无效
      5. 当有字母被选择时A和Ctrl-V这两个输出功能的键,
         会先清空所选的字母再进行输出

    给定一系列键盘输入,
    输出最终屏幕上字母的数量

    输入描述:
       输入为一行
       为简化解析用数字12345分别代替A、Ctrl-C、Ctrl-X、Ctrl-V、Ctrl-A的输入
       数字用空格分割

    输出描述:
        输出一个数字为屏幕上字母的总数量

    示例一:
        输入:
          1 1 1
        输出:
          3

   示例二:
        输入:
          1 1 5 1 5 2 4 4
        输出:
          2

"""


"""
  小组中每位都有一张卡片
  卡片是6位以内的正整数
  将卡片连起来可以组成多种数字
  计算组成的最大数字

  输入描述：
    ","分割的多个正整数字符串
    不需要考虑非数字异常情况
    小组种最多25个人

   输出描述：
     最大数字字符串

   示例一
     输入
      22,221
     输出
      22221

    示例二
      输入
        4589,101,41425,9999
      输出
        9999458941425101

"""
import functools

nums = input().split(",")
cmp = lambda x, y: 1 if x + y < y + x else -1
nums.sort(key=functools.cmp_to_key(cmp))
res = "".join(nums)
if nums == ["0"]:
    res = "0"

"""
  1.输入字符串s输出s中包含所有整数的最小和，
  说明：1字符串s只包含a~z,A~Z,+,-，
  2.合法的整数包括正整数，一个或者多个0-9组成，如：0,2,3,002,102
  3.负整数，负号开头，数字部分由一个或者多个0-9组成，如-2,-012,-23,-00023
  输入描述：包含数字的字符串
  输出描述：所有整数的最小和
  示例：
    输入：
      bb1234aa
  　输出
      10
  　输入：
      bb12-34aa
  　输出：
      -31
  说明：1+2-(34)=-31
"""
s = input()
ans = 0
i = 0
while i < len(s):
    if s[i].isnumeric():
        ans += int(s[i])
    else:
        if s[i] == "-":
            neg = ""
            for num in s[i + 1 :]:
                if num.isnumeric():
                    neg += num
                else:
                    break
            if neg:
                ans -= int(neg)
                i += len(neg)
    i += 1
print(ans)


"""
  程序员小明打了一辆出租车去上班。出于职业敏感，他注意到这辆出租车的计费表有点问题，总是偏大。
  出租车司机解释说他不喜欢数字4，所以改装了计费表，任何数字位置遇到数字4就直接跳过，其余功能都正常。
  比如：
    1. 23再多一块钱就变为25；
    2. 39再多一块钱变为50；
    3. 399再多一块钱变为500；
    小明识破了司机的伎俩，准备利用自己的学识打败司机的阴谋。
    给出计费表的表面读数，返回实际产生的费用。

    输入描述:
      只有一行，数字N，表示里程表的读数。
      (1<=N<=888888888)。
    输出描述:
      一个数字，表示实际产生的费用。以回车结束。
    示例1：
    输入
      5
    输出
      4
    说明
      5表示计费表的表面读数。
      表示实际产生的费用其实只有4块钱。

    示例2：
    输入
      17
    输出
      15
    说明
      17表示计费表的表面读数。
      15表示实际产生的费用其实只有15块钱。
    示例3：
    输入
      100
    输出
      81
    说明：100表示计费表的表面读数，81表示实际产生的费用其实只有81块钱
"""
# 可以这样思考
# 题中的4可以换成任意的数字, 不改题解
# 因此相当于求9个数字中任意一个数字在某种情况下的通解, 对应解答中<4可以改成任意一个数字
s = input()
n = len(s)
ans = 0
for i in range(n):
    if s[i] < 4:
        ans += int(s[i]) * (9 ** (n - i - 1))
    else:
        ans += (int(s[i]) - 1) * (9 ** (n - i - 1))
    print(ans)

"""
给定参数n,从1到n会有n个整数:1,2,3,...,n,
        这n个数字共有n!种排列.
      按大小顺序升序列出所有排列的情况,并一一标记,
      当n=3时,所有排列如下:
      "123" "132" "213" "231" "312" "321"
      给定n和k,返回第k个排列.

      输入描述:
        输入两行，第一行为n，第二行为k，
        给定n的范围是[1,9],给定k的范围是[1,n!]。
      输出描述：
        输出排在第k位置的数字。

      实例1：
        输入:
          3
          3
        输出：
          213
        说明
          3的排列有123,132,213...,那么第三位置就是213

      实例2：
        输入
          2
          2
        输出：
          21
        说明
          2的排列有12,21，那么第二位置的为21
"""

from itertools import permutations

n = int(input())
k = int(input())
nums = list(map(str, range(1, n + 1)))
print("".join(list(permutations(nums, n))[k - 1]))


"""
   某学校举行运动会,学生们按编号（1、2、3.....n)进行标识,
   现需要按照身高由低到高排列，
   对身高相同的人，按体重由轻到重排列，
   对于身高体重都相同的人，维持原有的编号顺序关系。
   请输出排列后的学生编号
   输入描述：
      两个序列，每个序列由N个正整数组成，(0<n<=100)。
      第一个序列中的数值代表身高，第二个序列中的数值代表体重，
   输出描述：
      排列结果，每个数据都是原始序列中的学生编号，编号从1开始，
   实例一：
      输入:
       4
       100 100 120 130
       40 30 60 50
      输出:
       2134
"""
nums = list(range(1, int(input()) + 1))
heights = list(map(int, input().split()))
weights = list(map(int, input().split()))
lst = [
    (height, weight, num)
    for num, height, weight in zip(nums, heights, weights)
]
lst.sort()
print("".join(map(lambda x: str(x[2]), lst)))

"""
运维工程师采集到某产品线网运行一天产生的日志n条
  现需根据日志时间先后顺序对日志进行排序
  日志时间格式为H:M:S.N
  H表示小时(0~23)
  M表示分钟(0~59)
  S表示秒(0~59)
  N表示毫秒(0~999)
  时间可能并没有补全
  也就是说
  01:01:01.001也可能表示为1:1:1.1

  输入描述
     第一行输入一个整数n表示日志条数
     1<=n<=100000
     接下来n行输入n个时间

   输出描述
     按时间升序排序之后的时间
     如果有两个时间表示的时间相同
     则保持输入顺序

   示例：
     输入：
      2
      01:41:8.9
      1:1:09.211
     输出
       1:1:09.211
       01:41:8.9
   示例
      输入
       3
       23:41:08.023
       1:1:09.211
       08:01:22.0
      输出
        1:1:09.211
        08:01:22.0
        23:41:08.023

    示例
      输入
        2
        22:41:08.023
        22:41:08.23
      输出
        22:41:08.023
        22:41:08.23
      时间相同保持输入顺序
"""
n = int(input())
time_dict = {i: input() for i, _ in enumerate(range(n))}
time_list = (time.split(":") for time in time_dict.values())
d = {}
for i, (h, m, s) in enumerate(time_list):
    d[i] = 60 * 60 * int(h) + 60 * int(m) + float(s)
index_list = map(lambda y: y[0], sorted(d.items(), key=lambda x: x[1]))
for index in index_list:
    print(time_dict[index])


"""
  双十一众多商品进行打折销售
  小明想购买自己心仪的一些物品
  但由于购买资金限制
  所以他决定从众多心仪商品中购买三件
  而且想尽可能得花完资金
  现在请你设计一个程序 计算小明尽可能花费的最大资金数

  输入描述：
    输入第一行为一维整型数组m
    数组长度小于100
    数组元素记录单个商品的价格
    单个商品加个小于1000

    输入第二行为购买资金的额度r
    r<100000

  输出描述：
     输出为满足上述条件的最大花费额度

   注意：如果不存在满足上述条件的商品请返回-1

  示例：
     输入
      23,26,36,27
      78
     输出
      76
     说明：
      金额23、26、27得到76而且最接近且小于输入金额78

   示例：
       输入
       23,30,40
       26
       输出
        -1
       说明
       因为输入的商品无法满足3件之和小于26
       故返回-1

   输入格式正确无需考虑输入错误情况
"""

nums = list(map(int, input().split(",")))
target = int(input())

n = len(nums)
if n < 3:
    print(nums)
ans = -1
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            tmp = nums[i] + nums[j] + nums[k]
            if tmp <= target:
                ans = max(ans, tmp)
print(ans)

"""
  在学校中
  N个小朋友站成一队
  第i个小朋友的身高为height[i]
  第i个小朋友可以看到第一个比自己身高更高的小朋友j
  那么j是i的好朋友
  (要求：j>i)
  请重新生成一个列表
  对应位置的输出是每个小朋友的好朋友的位置
  如果没有看到好朋友
  请在该位置用0代替
  小朋友人数范围 0~40000

  输入描述：
    第一行输入N
    N表示有N个小朋友

    第二行输入N个小朋友的身高height[i]
    都是整数

  输出描述：
    输出N个小朋友的好朋友的位置

  示例1：
     输入：
       2
       100 95
      输出
       0 0
     说明
       第一个小朋友身高100站在队伍末尾
       向队首看 没有比他身高高的小朋友
       所以输出第一个值为0
       第二个小朋友站在队首前面也没有比他身高高的小朋友
       所以输出第二个值为0

   示例2：
      输入
        8
        123 124 125 121 119 122 126 123
      输出
        1 2 6 5 5 6 0 0
       说明：
       123的好朋友是1位置上的124
       124的好朋友是2位置上的125
       125的好朋友是6位置上的126
        依此类推
"""

n = int(input())
heights = list(map(int, input().split()))
ans = []
for i in range(n):
    for j in range(i + 1, n):
        if heights[j] > heights[i]:
            ans.append(str(j))
            break
    else:
        ans.append(str(0))
print(" ".join(ans))


"""
输入一串字符串
  字符串长度不超过100
  查找字符串中相同字符连续出现的最大次数

  输入描述
    输入只有一行，包含一个长度不超过100的字符串

  输出描述
    输出只有一行，输出相同字符串连续出现的最大次数

   说明：
     输出

   示例1：
     输入
       hello
     输出
       2

    示例2：
      输入
       word
      输出
       1

     示例3：
      输入
        aaabbc
       输出
        3

    字符串区分大小写
"""
s = input()
ans, count = 1, 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
        ans = max(ans, count)
    else:
        count = 1
print(ans)

"""
特定大小的停车场 数组cars表示
    其中1表示有车  0表示没车
    车辆大小不一，小车占一个车位(长度1)
    货车占两个车位(长度2)
    卡车占三个车位(长度3)
    统计停车场最少可以停多少辆车
    返回具体的数目

    输入描述：
      整型字符串数组cars
      其中1表示有车0表示没车
      数组长度<1000

    输出描述：
      整型数字字符串
      表示最少停车数

    示例1：
      输入
        1,0,1
      输出
        2
      说明：
        一个小车占第一个车位
        第二个车位空，一个小车占第三个车位
        最少有两辆车

     示例2:
       输入：
         1,1,0,0,1,1,1,0,1
       输出：
         3
       说明：
         一个货车占第1,2个车位
         第3,4个车位空
         一个卡车占第5,6,7个车位
         第8个车位空
         一个小车占第9个车位
         最少3俩个车
"""
nums = ("".join(input().split(","))).split("0")
ans = 0
for c in nums:
    x, y = divmod(len(c), 3)
    a, b = divmod(y, 2)
    ans += x + a + b
print(ans)

"""
给出一个只包含字母的字符串,
    不包含空格,统计字符串中各个子字母(区分大小写)出现的次数,
    并按照字母出现次数从大到小的顺序输出各个字母及其出现次数
    如果次数相同,按照自然顺序排序,且小写字母在大写字母之前

    输入描述:
      输入一行仅包含字母的字符串

    输出描述:
      按照字母出现次数从大到小的顺序输出各个字母和字母次数,
      用英文分号分割,
      注意末尾的分号
      字母和次数中间用英文冒号分隔

    示例:
        输入: xyxyXX
        输出:x:2;y:2;X:2;
    说明:每个字符出现的次数为2 故x排在y之前
    而小写字母x在大写X之前

    示例2:
        输入:
         abababb
        输出:
            b:4;a:3
        说明:b的出现个数比a多 故排在a前
"""
import collections

c = collections.Counter(input()).most_common()
print(";".join(f"{k}:{v}" for k, v in c))


"""
    现在有一队小朋友，他们高矮不同，
    我们以正整数数组表示这一队小朋友的身高，如数组{5,3,1,2,3}。
    我们现在希望小朋友排队，以“高”“矮”“高”“矮”顺序排列，
    每一个“高”位置的小朋友要比相邻的位置高或者相等；
    每一个“矮”位置的小朋友要比相邻的位置矮或者相等；
    要求小朋友们移动的距离和最小，第一个从“高”位开始排，输出最小移动距离即可。
    例如，在示范小队{5,3,1,2,3}中，{5, 1, 3, 2, 3}是排序结果。
    {5, 2, 3, 1, 3} 虽然也满足“高”“矮”“高”“矮”顺序排列，
    但小朋友们的移动距离大，所以不是最优结果。
    移动距离的定义如下所示：
    第二位小朋友移到第三位小朋友后面，移动距离为1，
    若移动到第四位小朋友后面，移动距离为2；

    输入描述:
        排序前的小朋友，以英文空格的正整数：
        4 3 5 7 8
        注：小朋友<100个
    输出描述:
        排序后的小朋友，以英文空格分割的正整数：
        4 3 7 5 8
    备注：4（高）3（矮）7（高）5（矮）8（高），
    输出结果为最小移动距离，只有5和7交换了位置，移动距离都是1.

     示例一：
     输入
       4 1 3 5 2
     输出
       4 1 5 2 3

     示例二：
     输入
       1 1 1 1 1
     输出
       1 1 1 1 1
     说明：相邻位置可以相等

     示例三：
     输入：
       xxx
     输出
       []
     说明：出现非法参数情况，返回空数组
"""
nums = list(map(int, input().split()))
for i in range(len(nums) - 1):
    if i % 2 and nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
    if not i % 2 and nums[i] < nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
print(" ".join(map(str, nums)))


"""
所谓的水仙花数是指一个n位的正整数其各位数字的n次方的和等于该数本身，
    例如153=1^3+5^3+3^3,153是一个三位数
    输入描述
        第一行输入一个整数N，
        表示N位的正整数N在3-7之间包含3,7
        第二行输入一个正整数M，
        表示需要返回第M个水仙花数
    输出描述
        返回长度是N的第M个水仙花数，
        个数从0开始编号，
        若M大于水仙花数的个数返回最后一个水仙花数和M的乘积，
        若输入不合法返回-1

    示例一：

        输入
         3
         0
        输出
         153
        说明：153是第一个水仙花数
     示例二：
        输入
        9
        1
        输出
        -1
"""


def is_true(num):
    s = str(num)
    n = len(s)
    ans = 0
    for i in s:
        ans += int(i) ** n
    if ans == num:
        return True


for i in range(10**7):
    if is_true(i):
        print(i)

d = {
    3: [153, 370, 371, 407],
    4: [1634, 8208, 9474],
    5: [54748, 92727, 93084],
    6: [548834],
    7: [1741725, 4210818, 9800817, 9926315],
}

n = int(input())
m = int(input())
if n in d:
    if m < len(d[n]):
        print(d[n][m])
    else:
        print(m * d[n][-1])
else:
    print(-1)

"""
游戏规则：输入一个只包含英文字母的字符串，
字符串中的俩个字母如果相邻且相同，就可以消除。
在字符串上反复执行消除的动作，
直到无法继续消除为止，
此时游戏结束。
输出最终得到的字符串长度。

输出：原始字符串str只能包含大小写英文字母，字母的大小写敏感，长度不超过100，
输出游戏结束后字符串的长度

备注：输入中包含非大小写英文字母是均为异常输入，直接返回0。

事例：mMbccbc输出为3
"""
s = input()
if not s.isalpha():
    print(0)
else:
    stack = []
    for ch in s:
        if stack and ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)
    print(len(stack))

"""
给定一个随机的整数数组(可能存在正整数和负整数)nums,
请你在该数组中找出两个数，其和的绝对值(|nums[x]+nums[y]|)为最小值
并返回这两个数(按从小到大返回)以及绝对值。
每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

输入描述：
 一个通过空格空格分割的有序整数序列字符串，最多1000个整数，
 且整数数值范围是[-65535,65535]

输出描述：
  两个数和两数之和绝对值

 示例一：
  输入
  -1 -3 7 5 11 15
  输出
  -3 5 2

说明：
因为|nums[0]+nums[2]|=|-3+5|=2最小，
所以返回-3 5 2
"""

nums = list(map(int, input().split()))
nums.sort()
n = len(nums)
min_value, l, r = float("inf"), None, None

for i in range(n):
    for j in range(i + 1, n):
        if abs(nums[i] + nums[j]) < min_value:
            min_value = abs(nums[i] + nums[j])
            l, r = nums[i], nums[j]
if min_value != float("inf"):
    print(f"{l} {r} {min_value}")

"""
    给定一个字符串S

    变化规则:
        交换字符串中任意两个不同位置的字符

    输入描述：
        一串小写字母组成的字符串
    输出描述：
        按照要求变换得到最小字符串

    实例1：
        输入：、
        abcdef
    输出
        abcdef

    实例2：
        输入
        bcdefa
        输出
        acdefb

    s都是小写字符组成
    1<=s.length<=1000
"""
s = list(input())
s_sorted = sorted(s)
for i, ch in enumerate(s_sorted):
    if ch == s[i]:
        continue
    else:
        indexes = [i for i, c in enumerate(s) if ch == c]
        s[indexes[-1]], s[i] = s[i], ch
        break
print("".join(s))
