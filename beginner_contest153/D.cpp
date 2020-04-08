#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main() {
  int64_t h;
  cin >> h;

  int count = 0;
  while(h != 1) {
    h /= 2;
    count += 1;
    // cout << h << endl;
  }

  int64_t ans = 0;
  for(int i = 0; i <= count; i++) {
    ans += pow(2, i);
  }

  cout << ans << endl;


  return 0;
}