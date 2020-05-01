#include <bits/stdc++.h>
#define rep(i,n) for (int i=0; i<(n); i++)
using namespace std;
using ll = long long;
using P = pair<int,int>;

const int INF = 1001001001;

int main() {
  int n;
  cin >> n;
  vector<int> hs(n);
  rep(i, n) {
    cin >> hs.at(i);
  }

  vector<int> dps(n);
  dps.at(0) = 0;
  dps.at(1) = abs(hs.at(1) - hs.at(0));
  rep(i, n) {
    if (i == 0 || i == 1) {
      continue;
    }
    dps.at(i) = min(abs(hs.at(i) - hs.at(i - 1)) + dps.at(i - 1), abs(hs.at(i) - hs.at(i - 2)) + dps.at(i - 2));
  }

  cout << dps.at(n-1) << endl;
  return 0;
}