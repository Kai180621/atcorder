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

Int n, c, ans, q;

int main() {
  cin >> n;
  ans = 0;

  for(Int p = 1; p <= n; p++) {
    c = n / p;
    q = c * p;
    ans += (p + q) * c / 2;
  }
  cout << ans << endl;
  return 0;
}