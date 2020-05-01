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
using namespace std;
#define rep(i,n) for (int i=0; i<(n); i++)
#define MOD 1000000007
#define MOD2 998244353
#define INF ((1<<30)-1)
#define LINF (1LL << 60)
#define EPS (1e-10)
typedef long long Int;
typedef pair<int, int> P;


Int n;
Int happy[110000][3];
Int dp[110000][3];

int main() {
  cin >> n;
  rep(i, n) {
    cin >> happy[i][0] >> happy[i][1] >> happy[i][2];
  }

  rep(j, 3) {
    dp[0][j] = happy[0][j];
  }

  rep(i, n) {
    rep(j, 3) {
      rep(k, 3) {
        if (i == 0) {
          continue;
        }
        if (j == k) {
          continue;
        }
        dp[i][j] = max(dp[i][j], 
                      dp[i - 1][k] + happy[i][j]);
        // cout << dp[i][j] << endl;
      }
    } 
  }

  Int ans = 0;
  rep(j, 3) {
    // cout << dp[n-1][j] << endl;
    ans = max(ans, dp[n-1][j]);
  }
  
  cout << ans << endl;
  return 0;
}