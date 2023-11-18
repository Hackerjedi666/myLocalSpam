import pyautogui
import time
time.sleep(3)
pyautogui.write("""
#include <iostream>
#include <vector>

using namespace std;

bool canMakeIncreasingOrder(int n, vector<int>& stacks) {
for (int i = 0; i < n - 1; i++) {
if (stacks[i] < i + 1) {
return false;
}
stacks[i + 1] += stacks[i] - (i + 1);
}
return true;
}

int main() {
int t;
cin >> t;

while (t--) {
int n;
cin >> n;
vector<int> stacks(n);

for (int i = 0; i < n; i++) {
cin >> stacks[i];
}

bool result = canMakeIncreasingOrder(n, stacks);
cout << (result ? "YES" : "NO") << endl;
}

return 0;
}
""")
