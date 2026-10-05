#include <iostream>
#include <vector>
using namespace std;

int binarySearch(const vector<int>& numbers, int target) {
    int low = 0;
    int high = numbers.size() - 1;

    while (low <= high) {
        int middle = (low + high) / 2;

        if (numbers[middle] == target) {
            return middle;
        } else if (numbers[middle] < target) {
            low = middle + 1;
        } else {
            high = middle - 1;
        }
    }

    return -1;
}

int main() {
    vector<int> numbers = {10, 20, 30, 40, 50};
    int target = 30;

    int result = binarySearch(numbers, target);

    cout << "Target found at index: " << result << endl;

    return 0;
}