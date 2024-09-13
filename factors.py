import time
import multiprocessing

def factorize_number(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def factorize(*numbers):
    # Асинхронна версія 
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        result = pool.map(factorize_number, numbers)
    return result

    # Синхронна версія
    # return tuple(factorize_number(number) for number in numbers)

if __name__ == "__main__":
    start_time = time.time()
    result = factorize(128, 255, 99999, 10651060)  # Using *numbers
    end_time = time.time()
    
    # Виводимо результати
    for num, factors in zip([128, 255, 99999, 10651060], result):
        print(f"Factors of {num}: {factors}")
    
    print(f"Time taken with multiprocessing: {end_time - start_time:.4f} seconds")

    # Tests
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
