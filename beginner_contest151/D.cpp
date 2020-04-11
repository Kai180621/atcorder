#include <bits/stdc++.h>
#define rep(i,n) for (int i=0; i<(n); i++)
using namespace std;
using ll = long long;
using P = pair<int,int>;
const int INF = 1001001001;

const int di[] = {-1, 0, 1, 0}
const int dj[] = {0, -1, 0, 1}

int main() {
  int h, w;
  cin >> h >> w;
  vector<string> s(h);
  rep(i, h) cin >> s[i];
  rep(si, h)rep(sj, w) {
    if (s[si][sj] == "#") continue;
    vector<vector<int>> data(h, vector<int>(w, INF));
    queue<P> q;
    auto update = [&]
  }

  return 0;
}