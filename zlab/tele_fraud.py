"""
Telefraud（电信诈骗） remains a common and persistent problem in our society.
In some cases, unsuspecting victims lose their entire life savings.
To stop this crime, you are supposed to write a program to detect those suspects from a huge amount of phone call records.

# Conditions

A person must be detected as a suspect if he/she
 - makes more than K short phone call_num to different people everyday
 - but no more than 20% of these people would call back.
And more,
 - if two suspects are calling each other, we say they might belong to the same gang.
A makes a short phone call to B means that the total duration of the call_num from A to B is no more than 5 minutes.

# Input Specification:

Each input file contains one test case.
For each case, the first line gives 3 positive integers:
 - K (≤500, the threshold（阈值） of the amount of short phone call_num)
 - N (≤10^3, the number of different phone numbers)
 - M (≤10^5, the number of phone call records).

Then M lines of one day's records are given, each in the format:
  caller receiver duration

where caller and receiver are numbered from 1 to N, and duration is no more than 1440 minutes in a day. 24*60=1440

# Output Specification:

Print in each line all the detected suspects in a gang, in ascending order of their numbers.
The gangs are printed in ascending order of their first members.
The numbers in a line must be separated by exactly 1 space, and there must be no extra space at the beginning or the end of the line.

If no one is detected, output None instead.
"""
import sys
from collections import OrderedDict

# 1st line
line = sys.stdin.readline().strip()
K, N, M = map(int, line.split(' '))  # N phones; M records

# N*N 数组，有向图，记录每条 edge 通话总时长 total duration
total_duration = [
    [0] * (N + 1) for _ in range(N + 1)  # each caller, N receivers; idx from [1,N]
]

# then M lines phone records
for i in range(M):
    line = sys.stdin.readline().strip()
    c, r, d = map(int, line.split(' '))  # caller receiver duration
    total_duration[c][r] += d

gang_headers = [i for i in range(N + 1)]


def find_header(x):
    """
    find the 1st suspect no. (header) of a gang
    """
    if x == gang_headers[x]:
        return x
    else:
        gang_headers[x] = find_header(gang_headers[x])  # 递归寻找 1st gang
        return gang_headers[x]


# find all suspects
suspects = []
for i in range(1, N + 1):  # each person
    call_num = recall_num = 0  # 打出/打入
    for j in range(1, N + 1):  # 不同人
        if 0 < total_duration[i][j] <= 5:  # short
            call_num += 1
            if total_duration[j][i] > 0:
                recall_num += 1
    if call_num > K:  # yes
        if recall_num * 1.0 / call_num <= 0.2:  # recall
            suspects.append(i)  # note: i 的判断是有序的

# find suspects in a gang
for i in range(len(suspects)):  # suspects
    for j in range(i + 1, len(suspects)):  # another
        if total_duration[suspects[i]][suspects[j]] > 0 and total_duration[suspects[j]][suspects[i]] > 0:  # 互相打了
            # headers of gang
            header1 = find_header(suspects[i])
            header2 = find_header(suspects[j])  # 一般更靠后，需要更新 j 的 header 为 i 的 header 并递归更新到 i 所在 gang 的 header
            # 互相打过，但是 headers 还不同
            if header1 < header2:
                gang_headers[header2] = header1
            elif header1 > header2:
                gang_headers[header1] = header2

gangs = OrderedDict()
for s in suspects:  # suspects array 有序
    header = find_header(s)
    if header not in gangs:
        gangs[header] = []
    gangs[header].append(s)  # gang add suspects

if len(gangs) == 0:
    print(None)
else:
    for header in gangs:
        print(' '.join([str(i) for i in gangs[header]]))

"""
Sample Input 1:
5 15 31
1 4 2
1 5 2
1 5 4
1 7 5
1 8 3
1 9 1
1 6 5
1 15 2
1 15 5
3 2 2
3 5 15
3 13 1
3 12 1
3 14 1
3 10 2
3 11 5
5 2 1
5 3 10
5 1 1
5 7 2
5 6 1
5 13 4
5 15 1
11 10 5
12 14 1
6 1 1
6 9 2
6 10 5
6 11 2
6 12 1
6 13 1
      
Sample Output 1:
3 5
6
"""

"""
Sample Input 2:
5 7 8
1 2 1
1 3 1
1 4 1
1 5 1
1 6 1
1 7 1
2 1 1
3 1 1

Sample Output 2:
None
"""
