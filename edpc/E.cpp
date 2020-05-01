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
#include <bits/stdc++.h>
#define rep0(i,n) for (int i=0; i<(n); i++)
#define rep1(i,n) for (int i=1; i<=(n); i++)
#define MOD 1000000007
#define MOD2 998244353
#define INF ((1<<30)-1)
#define LINF (1LL << 60)
#define EPS (1e-10)
using namespace std;
typedef long long Int;
typedef pair<int,int> P;

int n, W;
Int w[110], v[110];
Int dp[110][110000];
int ans;

int main() {
  cin >> n >> W;
  rep1(i, n) {
    cin >> w[i] >> v[i];
  }
  dp[0][0] = 0;
  rep1(j, 100000) {
    dp[0][j] = INF;
  }
  rep1(i, n) rep0(j, 100000) {
    dp[i][j] = dp[i - 1][j];
    if (j-v[i] >= 0) {
      dp[i][j] = min(dp[i][j], dp[i - 1][j - v[i]] + w[i]);
    }
  }
  rep0(j, 100000) {
    if (dp[n][j] <= W) {
      ans = max(ans, j);
    }
  }
  // cout << dp[n][100] << endl;
  cout << ans << endl;

  return 0;
}