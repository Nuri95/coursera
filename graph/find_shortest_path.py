from collections import deque

# схема https://idroo.com/board-7kkiElpwAJ

g = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]

def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]

    deq = deque([start])
    is_visited[start] = True
    # parent[start] =
    print('is_visited = ', is_visited)
    while len(deq) > 0:
        print('deq = ', deq)
        current = deq.pop()
        print('current = ', current)

        if current == finish:
            # return parent
            break

        for i, vertex in enumerate(graph[current]):
            if vertex == 1 and not is_visited[i]:
                print(i)
                is_visited[i] = True
                parent[i] = current
                deq.appendleft(i)
                print('parent =', parent)
        print('is_visited = ', is_visited)

    else:
        return f'Из вершины {start} нельзя попасть в вершину {finish}'

    cost = 0
    way = deque([finish])
    i = finish
    print('way = ', way)
    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]
        print('way = ', way)
        print(i, parent[i])

    cost += 1
    way.appendleft(start)

    return f'кратчайший путь {list(way)} длиною в {cost} условных единиц'


s = int(input('От какой вершины идти: '))
f = int(input('До какой вершины идти: '))
print(bfs(g, s, f))