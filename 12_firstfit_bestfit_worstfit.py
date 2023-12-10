def first_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)

    for i in range(len(process_sizes)):
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                allocation[i] = j
                memory_blocks[j] -= process_sizes[i]
                break

    return allocation

def best_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)

    for i in range(len(process_sizes)):
        best_fit_index = -1
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                if best_fit_index == -1 or memory_blocks[j] < memory_blocks[best_fit_index]:
                    best_fit_index = j

        if best_fit_index != -1:
            allocation[i] = best_fit_index
            memory_blocks[best_fit_index] -= process_sizes[i]

    return allocation

def worst_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)

    for i in range(len(process_sizes)):
        worst_fit_index = -1
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                if worst_fit_index == -1 or memory_blocks[j] > memory_blocks[worst_fit_index]:
                    worst_fit_index = j

        if worst_fit_index != -1:
            allocation[i] = worst_fit_index
            memory_blocks[worst_fit_index] -= process_sizes[i]

    return allocation

if __name__ == "__main__":
    # Example usage
    memory_blocks = [100, 500, 200, 300, 600]
    process_sizes = [212, 417, 112, 426]

    print("Memory Blocks:", memory_blocks)
    print("Process Sizes:", process_sizes)

    first_fit_allocation = first_fit(list(memory_blocks), list(process_sizes))
    print("\nFirst Fit Allocation:", first_fit_allocation)

    best_fit_allocation = best_fit(list(memory_blocks), list(process_sizes))
    print("Best Fit Allocation:", best_fit_allocation)

    worst_fit_allocation = worst_fit(list(memory_blocks), list(process_sizes))
    print("Worst Fit Allocation:", worst_fit_allocation)
