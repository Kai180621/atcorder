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

Int n;
Int w;
Int items[110][2];
Int dp[110][110000];

int main() {
  cin >> n >> w;
  rep1(i, n) {
    cin >> items[i][0] >> items[i][1];
  }

  rep1(i, n) {
    for (int j = 0; j <= w; j++) {
      dp[i][j] = dp[i - 1][j];
      if (j - items[i][0] >= 0) {
        dp[i][j] = max(dp[i - 1][j],
                      dp[i - 1][j - items[i][0]] + items[i][1]);
      }
    }
    // cout << dp[i][w] << endl;
  }

  cout << dp[n][w] << endl;

  return 0;
}