from collections import deque

visited = set()

def calculate_min_time_to_send_file(N, connections, M, queue_of_computers_hold_file):
    graph = build_graph(N, connections)

    visited.update(queue_of_computers_hold_file)
    queue_of_computers_hold_file = deque(queue_of_computers_hold_file) 
    time = 0

    while len(visited) < N:
        time += 1
        queue_of_computers_hold_file = continue_send_file(graph, queue_of_computers_hold_file)

    return time

def build_graph(N, connections):
    graph = {i: [] for i in range(1, N + 1)}
    for x, y in connections:
        graph[x].append(y)
        graph[y].append(x)

    return graph

def continue_send_file(graph, queue_of_computers_hold_file):
    next_queue = deque()

    while queue_of_computers_hold_file:
        current_computer_send_file = queue_of_computers_hold_file.popleft()
        transmitted = False 

        for neighbor in graph[current_computer_send_file]:
            if neighbor not in visited:
                if transmitted: 
                    next_queue.append(current_computer_send_file)
                    
                if not transmitted: 
                    transmitted = True
                    visited.add(neighbor)
                    next_queue.append(neighbor)

    return next_queue

def main():
    # Ví dụ 1:
    N1 = 6
    connections1 = [(1, 2), (2, 3), (2, 4), (1, 5), (5, 6)]
    M1 = 1
    computers_hold_file1 = [1]
    print(calculate_min_time_to_send_file(N1, connections1, M1, computers_hold_file1))  # Kết quả: 3

    # Ví dụ 2:
    visited.clear()
    N2 = 6
    connections2 = [(1, 2), (2, 3), (2, 4), (1, 5), (5, 6)]
    M2 = 2
    computers_hold_file2 = [1, 2]
    print(calculate_min_time_to_send_file(N2, connections2, M2, computers_hold_file2))  # Kết quả: 2

if __name__ == "__main__":
  main()