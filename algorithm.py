
---

#### **`algorithm_utilities.py`**

Add the provided code with minor enhancements for GitHub upload, ensuring function and comment consistency:

```python
import heapq
import networkx as nx
import matplotlib.pyplot as plt

# --- Binary Search ---
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Found!
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Not found.

# --- Selection Sort ---
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i + 1}: {arr}")

# --- Bubble Sort ---
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"Step {i + 1}: {arr}")

# --- Expression Conversions ---
def is_operator(char):
    return char in {'+', '-', '*', '/'}

def get_precedence(operator):
    return 1 if operator in {'+', '-'} else 2

def shunting_yard(infix_expression):
    output, operator_stack = [], []
    for char in infix_expression:
        if char.isalnum():
            output.append(char)
        elif is_operator(char):
            while operator_stack and is_operator(operator_stack[-1]) and get_precedence(operator_stack[-1]) >= get_precedence(char):
                output.append(operator_stack.pop())
            operator_stack.append(char)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()
    while operator_stack:
        output.append(operator_stack.pop())
    return output

def infix_to_prefix(infix_expression):
    return ''.join(reversed(shunting_yard(reversed(infix_expression))))

def infix_to_postfix(infix_expression):
    return ''.join(shunting_yard(infix_expression))

# --- Heap Construction ---
def build_heap(arr, heap_type='min'):
    if heap_type == 'min':
        heapq.heapify(arr)
    elif heap_type == 'max':
        arr = [-element for element in arr]
        heapq.heapify(arr)
        arr = [-element for element in arr]
    else:
        raise ValueError("Invalid heap type! Use 'min' or 'max'.")
    return arr

# --- Graph Operations ---
def create_graph_from_adjacency_matrix(adjacency_matrix):
    G = nx.Graph()
    for i in range(len(adjacency_matrix)):
        for j in range(i + 1, len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] == 1:
                G.add_edge(i, j)
    return G

def bfs(graph, start_node):
    visited, queue = set(), [start_node]
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            print(f"Visited node: {current_node}")
            visited.add(current_node)
            queue.extend(graph.neighbors(current_node))

# --- Main Menu ---
def main_menu():
    while True:
        print("1. Binary Search")
        print("2. Selection Sort")
        print("3. Bubble Sort")
        print("4. Infix to Prefix/Postfix Conversion")
        print("5. Build Heap")
        print("6. Graph Creation")
        print("8. Exit")

        choice = input("Please select an option (1-8): ")

        if choice == '1':
            binary_search_menu()
        elif choice == '2':
            arr = list(map(int, input("Enter an array (space-separated): ").split()))
            print("Array before sorting:", arr)
            selection_sort(arr)
            print("Sorted array:", arr)
        elif choice == '3':
            arr = list(map(int, input("Enter an array (space-separated): ").split()))
            print("Array before sorting:", arr)
            bubble_sort(arr)
            print("Sorted array:", arr)
        elif choice == '4':
            infix_expression = input("Enter an infix expression: ")
            prefix_expression = infix_to_prefix(infix_expression)
            postfix_expression = infix_to_postfix(infix_expression)
            print(f"Prefix Expression: {prefix_expression}")
            print(f"Postfix Expression: {postfix_expression}")
        elif choice == '5':
            try:
                arr = list(map(int, input("Enter an array (space-separated): ").split()))
                heap_type = input("Select heap type (min/max): ").lower()
                heap = build_heap(arr, heap_type)
                print(f"Constructed {heap_type} heap:", heap)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '6':
            try:
                adjacency_matrix = []
                n = int(input("Enter the number of vertices: "))
                print("Enter the adjacency matrix:")
                for _ in range(n):
                    row = list(map(int, input().split()))
                    adjacency_matrix.append(row)
                G = create_graph_from_adjacency_matrix(adjacency_matrix)
                nx.draw(G, with_labels=True, font_weight='bold', node_color='skyblue', font_color='black')
                plt.show()
            except ValueError:
                print("Invalid input! Ensure all values are integers.")
        elif choice == '7':
            try:
                if 'G' in locals():
                    start_node = int(input("Enter the starting node for BFS: "))
                    bfs(G, start_node)
                else:
                    print("Graph not created. Please create a graph first.")
            except ValueError:
                print("Invalid input! Ensure the starting node is an integer.")
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 8.")

def binary_search_menu():
    try:
        arr = list(map(int, input("Enter a sorted array (space-separated): ").split()))
        target = int(input("Enter the target value: "))
        result = binary_search(arr, target)
        if result != -1:
            print(f"Target found at index {result}.")
        else:
            print("Target not found.")
    except ValueError:
        print("Invalid input! Ensure the array is sorted and values are integers.")

if __name__ == "__main__":
    main_menu()


