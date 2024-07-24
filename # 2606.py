# 2606

import sys
from queue import Queue

num_of_com = int(sys.stdin.readline())

num_of_com_pair = int(sys.stdin.readline())

connection_pair = [[] for i in range(num_of_com+1)]
visit_computer = [False]*(num_of_com+1)
count = 0

for i in range(num_of_com_pair):
    a, b = map(int, sys.stdin.readline().split())
    connection_pair[a].append(b)
    connection_pair[b].append(a)

virus_connection_queue = Queue()
virus_connection_queue.put(1)
visit_computer[1] = True

while(virus_connection_queue.qsize() > 0):
    virus_computer = virus_connection_queue.get()
    for computer in connection_pair[virus_computer]:
        if visit_computer[computer] == False:
            visit_computer[computer] = True
            count += 1
            virus_connection_queue.put(computer)

print(count)
    