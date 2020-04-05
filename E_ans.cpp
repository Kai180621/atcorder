#include <bits/stdc++.h>
using namespace std;

const int INF = 1001001001;

int main() {
  int h, n;
  cin >> h >> n;
  vector<int> dp(h+1, INF);
  // for(int i = 0; i < 10; i++) {
  //   cout << dp[i] << endl;
  // }
  dp[0] = 0;
  for(int i = 0; i < n; i++) {
    int a, b;
    cin >> a >> b;
    for(int j = 0; j < h; j++) {
      int nj = min(j+a, h);
      dp[nj] = min(dp[nj], dp[j] + b);
    }
  }
  cout << dp[h] << endl;
  return 0;
}