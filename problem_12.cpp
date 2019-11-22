#include <iostream>
#include <cmath>
#include <chrono>

// For an explanation of the problem see the jupyter notebook.

int count_divisors(const int &n) {
    size_t maxval = sqrt(n) + 1;
    size_t count = 0;

    for (size_t i = 1; i < maxval; i++) {
        if (n%i == 0){
            if (i == i/n) {
                count += 1;
            } else {
                count += 2;
            }
        }
    }

    return count;
}

int main(){
    auto start = std::chrono::high_resolution_clock::now();

    size_t number=0;
    size_t iteration=0;

    size_t divisors = 500;
    size_t counted_divisors = 0;

    while (counted_divisors < divisors) {
        iteration += 1;
        number += iteration;

        counted_divisors = count_divisors(number);
    }

    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop-start);

    std::cout << "Number = " << number << std::endl;
    std::cout << "Time = " << duration.count()/1000. << " ms" << std::endl;

    return 0;
}