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

string s, t;
int dp[3300][3300];

int main() {
  cin >> s >> t;
  int n = s.size(), m = t.size();

  for (int i =1; i<= n; i++) {
    for (int j = 1; j<= m; j++) {
      if (i==0 || j == 0) {
        dp[i][j] = 0;
        continue;
      }
      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
      if(s[i] == t[j]) {
        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1);
      }
      
    }
  }
  string reans = "";
  while(n > 0 && m > 0) {
    if(dp[n][m] == dp[n-1][m]) n--;
    else if (dp[n][m] == dp[n][m-1]) m--;
    else {
      reans += s[n-1];
      n--;
      m--;
    }
  }
  int l = reans.size();
  for (int i = 0; i < l; i++) {
    cout << reans[l - i - 1];
  }
  cout << endl;
  return 0;
}