import heapq
import sys

n = int(sys.stdin.readline())
l = []
h = []
for i in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))
l.sort()
for i in l:
    heapq.heappush(h, i[1])
    if h[0] <= i[0]:
        heapq.heappop(h)
print(len(h))


'''
먼저 시작시각을 기준으로 수업시간들을 오름차순 정렬
종료시각을 리스트에 추가한 다음, 시간시각이 리스트의 최소 종료시각보다 작은지 확인 후
그렇지 않으면 리스트의 최소 종료시각 삭제
만약 리스트의 길이가 늘어난다면 시작시각이 리스트의 모든 종료시각보다 작으므로
그만큼의 강의실이 필요해진다.
위 과정을 위해 리스트의 최소 원소를 빠르게 꺼내올 수 있는 자료구조가 필요하기에
heap을 사용해 리스트를 관리한다.
'''
