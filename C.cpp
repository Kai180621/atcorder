#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> h_list(n);
  for(int i = 0; i < n; i++) {
    cin >> h_list[i];
  }

  sort(h_list.begin(), h_list.end());

  if (n > k) {
    for(int i = 0; i < k; i++) {
      h_list.pop_back();
    }
  }
  else {
    cout << 0 << endl;
    return 0;
  }
  int64_t ans = 0;
  for(int i = 0; i < h_list.size(); i++) { 
    ans += h_list[i];
  }

  cout << ans << endl;
  return 0;
}