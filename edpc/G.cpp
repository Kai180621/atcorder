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

int n, m, u, v;
vector<int> edge[110000];
int memo[110000];
bool done[110000];

int dp(int v) {
  if(done[v])
    return memo[v];
  int ans = 0;
  for(int to: edge[v]) {
    ans = max(ans, dp(to) + 1);
  }
  done[v] = true;
  memo[v] = ans;
  return ans;
}

int main()
{
  cin >> n >> m;
  for(int i = 0; i < m; i++) {
    cin >> u >> v;
    edge[u].push_back(v);
  }
  int ans = 0;
  for (int v = 1; v <= n; v++) {
    ans = max(dp(v), ans);
  }

  cout << ans << endl;

  return 0;
}