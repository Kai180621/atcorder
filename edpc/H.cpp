#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cassert>
#include<cmath>
#include<vector>
#include<map>
#include<set>
#include<string>
#include<queue>
#include<stack>
#define MOD 1000000007
#define MOD2 998244353
#define INF ((1<<30)-1)
#define LINF (1LL << 60)
#define EPS (1e-10)
using namespace std;
typedef long long Int;
typedef pair<int, int> P;

int h, w;
string field[1100];
Int dps[1100];

int dp(int i, int j) {
  if (i == 0 && j == 0)
    return 1;
  if (field[i][j] == '#')
    return 0;
  dps = 0;
  if (i - 1 > 0)
    dps += dp(i - 1, j);
  if (j - 1 > 0)
    dps += dp(i, j - 1);
  dps %= MOD;
  return dps;
}

int main(){
  cin >> h >> w;
  for(int i = 0; i < h; i++) {
    cin >> field[i];
  }

  Int ans = dp(h-1, w-1);
  for(int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      cout << dp(i, j);
    }
    cout << endl;
  }
  cout << ans << endl;

  return 0;
}