from collections import deque

# g = [
#     [0, 0, 1, 1, 9, 0, 0, 0],
#     [0, 0, 9, 4, 0, 0, 5, 0],
#     [0, 9, 0, 0, 3, 0, 6, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 5, 0],
#     [0, 0, 7, 0, 8, 1, 0, 0],
#     [0, 0, 0, 0, 0, 1, 2, 0],
# ]
g = [
    [0, 14, 7, 0, 0, 9],
    [7, 0, 10, 15, 0, 0],
    [9, 10, 0, 11, 0, 2],
    [0, 15, 11, 0, 6, 0],
    [0, 0, 0, 6, 0, 9],
    [14, 0, 2, 0, 9, 0],
]


# Моё решение

def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length

    cost[start] = 0
    deq = deque([start])
    is_visited[start] = True

    while len(deq) > 0:
        current = deq.pop()

        d = dict()
        for i, vertex in enumerate(graph[current]):
            if vertex > 0 and not is_visited[i]:
                d[i] = vertex

        if d:
            dd = sorted(d.items(), key=lambda item: item[1])
            for k, v in dd:
                distance = cost[current] + v

                if distance < cost[k]:
                    cost[k] = distance

                deq.appendleft(k)
        is_visited[current] = True

    return cost


s = int(input('От какой вершины идти: '))
print(dijkstra(g, s))


# Решение из курса

def dijkstra2(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0  #двигаем дальше по графу или нет

    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:  # если есть ребро и не посещали ее то должны проверить расстояние
                # если расстояние до I вершины окажется больше чем сумма расстоянии
                # от вершины старт до вершины i + значение которое уже хранится в start То заменяем
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        # таким образом мы обошли все смежные вершины и записали мин расстояние для них

        # изменяем значение минимального пути на бесконечность
        min_cost = float('inf')
        for i in range(length):
            # если минимальная стоимость окажется больше чем стоимость пути до очередной вершины
            # и при этом эту вершину мы еще не  поещали то изменяем значние миимальной стоимости
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost


print(dijkstra2(g, s))
