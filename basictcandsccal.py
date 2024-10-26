import ast
import timeit
import sys

def estimate_python_complexity(code):
    """
    Estimate time and space complexity for Python code.
    """
    def estimate_time_complexity(code):
        tree = ast.parse(code)
        loop_count = sum(isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree))
        recursive = any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'recurse'
                        for node in ast.walk(tree))

        if recursive:
            return "O(2^N) (Assumed exponential due to recursion)"
        elif loop_count == 1:
            return "O(N) (Single loop detected)"
        elif loop_count == 2:
            return "O(N^2) (Two nested loops detected)"
        else:
            return "O(1) (No significant loops or recursion detected)"

    def run_code_for_time(code, test_input):
        exec_globals = {}
        exec(code, exec_globals)
        function_name = [name for name, obj in exec_globals.items() if callable(obj)][0]
        func = exec_globals[function_name]

        times = []
        for size in test_input:
            exec_globals['input_size'] = size
            time_taken = timeit.timeit(lambda: func(input_size), number=1)
            times.append((size, time_taken))

        return times

    def estimate_space_complexity(code):
        exec_globals = {}
        exec(code, exec_globals)
        variables = [var for var in exec_globals if not var.startswith("__") and not callable(exec_globals[var])]
        space = sum(sys.getsizeof(exec_globals[var]) for var in variables)
        return f"Approximate space usage: {space} bytes"

    # Input sizes for time testing
    test_input_sizes = [10, 100, 1000]
    time_complexity = estimate_time_complexity(code)
    time_results = run_code_for_time(code, test_input_sizes)
    space_complexity = estimate_space_complexity(code)
    
    return time_complexity, time_results, space_complexity

def estimate_cpp_complexity(code):
    """
    Provide a rough estimate for time and space complexity for C++ code based on loop
    detection and common patterns. Note that this is an approximation.
    """
    loop_count = code.count("for(") + code.count("while(")
    recursive = any(word in code for word in ["recurse", "recursive"])
    
    if recursive:
        time_complexity = "O(2^N) (Assumed exponential due to recursion)"
    elif loop_count == 1:
        time_complexity = "O(N) (Single loop detected)"
    elif loop_count == 2:
        time_complexity = "O(N^2) (Two nested loops detected)"
    else:
        time_complexity = "O(1) (No significant loops or recursion detected)"
    
    space_complexity = "Space complexity estimate is not available for C++ in this environment."
    
    return time_complexity, space_complexity

# Main Program
print("Select Language: 1) Python 2) C++")
choice = input("Enter 1 or 2: ")

if choice == '1':
    print("Enter your Python code below (end with an empty line):")
    user_code = ""
    while True:
        line = input()
        if line == "":
            break
        user_code += line + "\n"
    
    time_complexity, time_results, space_complexity = estimate_python_complexity(user_code)
    
    print("\nTime Complexity Estimation (Static Analysis):", time_complexity)
    print("Time Complexity Estimation (Empirical):")
    for size, time_taken in time_results:
        print(f"Input size {size}: {time_taken:.6f} seconds")
    print("Space Complexity Estimation:", space_complexity)

elif choice == '2':
    print("Enter your C++ code below (end with an empty line):")
    user_code = ""
    while True:
        line = input()
        if line == "":
            break
        user_code += line + "\n"
    
    time_complexity, space_complexity = estimate_cpp_complexity(user_code)
    print("\nTime Complexity Estimation (Static Analysis):", time_complexity)
    print("Space Complexity Estimation:", space_complexity)

else:
    print("Invalid choice. Please select 1 for Python or 2 for C++.")


#output
Select Language: 1) Python 2) C++
Enter 1 or 2: 2
Enter your C++ code below (end with an empty line):
#include <iostream>

int sum_of_n(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}

Time Complexity Estimation (Static Analysis): O(N) (Single loop detected)
Space Complexity Estimation: Space complexity estimate is not available for C++ in this environment.
