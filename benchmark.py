import time
import colormood

def benchmark(function, count):
    from numpy import mean

    results = []
    for x in range(count):
        start = time.time()
        function()
        end = time.time()
        results.append((end - start) * 1000.0)
    print(f'{function}, {count} times')
    print(f'longest:  {max(results)}')
    print(f'quickest: {min(results)}')
    print(f'mean:     {mean(results)}\n')

benchmark(colormood.blur_image,10)
