#include <iostream>
#include <list>
using namespace std;

int main() {
    string input;
    cin >> input;

    list<char> editor(input.begin(), input.end());
    auto cursor = editor.end();

    int n;
    cin >> n;
    
    while (n--) {
        char cmd;
        cin >> cmd;
        
        if (cmd == 'L' && cursor != editor.begin()) {
            --cursor;
        } else if (cmd == 'D' && cursor != editor.end()) {
            ++cursor;
        } else if (cmd == 'B' && cursor != editor.begin()) {
            cursor = editor.erase(--cursor);
        } else if (cmd == 'P') {
            char x;
            cin >> x;
            editor.insert(cursor, x);
        }
    }

    for (char c : editor) {
        cout << c;
    }
}