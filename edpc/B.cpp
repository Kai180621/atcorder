#include <bits/stdc++.h>
#define rep(i,n) for (int i=0; i<(n); i++)
using namespace std;
using ll = long long;
using P = pair<int,int>;

const int INF = 1001001001;

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> hs(n);
  rep(i, n) {
    cin >> hs.at(i);
  }

  vector<int> dps(n, INF);
  dps.at(0) = 0;
  dps.at(1) = abs(hs.at(1) - hs.at(0));
  rep(i, n) {
    if (i == 0 || i == 1) {
      continue;
    }
    for (int j = 1; j <= k; j++) {
      if (i - j < 0) {
        break;
      }
      dps.at(i) = min(dps.at(i), abs(hs.at(i) - hs.at(i - j)) + dps.at(i-j));

      // cout << dps.at(i) << endl;
    }
  }

  // rep(i,n) {
  //   cout << dps.at(i) << endl;
  // }


  cout << dps.at(n-1) << endl;
  return 0;
}