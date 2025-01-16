#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);           

    int n;
    cin >> n;
    priority_queue<int, vector<int>, greater<int>> minHeap;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        minHeap.push(num);
    }

    while (!minHeap.empty()) {
        cout << minHeap.top() << "\n";
        minHeap.pop();
    }

    return 0;
}
