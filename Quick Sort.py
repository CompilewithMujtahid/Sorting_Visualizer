import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# --- QuickSort Algorithm with Visualization ---

def quicksort(arr, start, end, ims):
    if start < end:
        pivot_index = partition(arr, start, end, ims)
        quicksort(arr, start, pivot_index - 1, ims)
        quicksort(arr, pivot_index + 1, end, ims)


def partition(arr, start, end, ims):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        # Record the current frame highlighting the pivot and comparison
        ims.append(draw_bars(arr, pivot_index=end, compare_index=j))

        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            ims.append(draw_bars(arr, swap_indices=(i, j), pivot_index=end))

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    ims.append(draw_bars(arr, swap_indices=(i + 1, end)))

    return i + 1


def draw_bars(arr, swap_indices=None, pivot_index=None, compare_index=None):
    colors = ['skyblue'] * len(arr)
    if pivot_index is not None:
        colors[pivot_index] = 'purple'
    if compare_index is not None:
        colors[compare_index] = 'yellow'
    if swap_indices is not None:
        for i in swap_indices:
            colors[i] = 'red'
    bar = plt.bar(range(len(arr)), arr, color=colors)
    return bar


# --- Main Visualization ---
if __name__ == '__main__':
    n = 25
    arr = [random.randint(10, 100) for _ in range(n)]

    fig, ax = plt.subplots()
    ims = []

    plt.title('QuickSort Visualizer')
    plt.xlabel('Index')
    plt.ylabel('Value')

    # Run QuickSort and record the steps
    quicksort(arr, 0, len(arr) - 1, ims)

    # Create and show the animation
    ani = animation.ArtistAnimation(fig, ims, interval=200, repeat=False)
    plt.show()