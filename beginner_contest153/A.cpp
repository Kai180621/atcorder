#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main() {
  /* code */
  int h, a;
  cin >> h >> a;
  int ans = h / a;
  if (h % a != 0) ans += 1;
  cout << ans << endl;

  return 0;
}