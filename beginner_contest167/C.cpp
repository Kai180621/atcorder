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

int N;
int M;
Int X;

Int price[15];
Int books[15][15];
Int ms[15];

int main() {
  cin >> N >> M >> X;
  for(int i = 0; i < N; i++) {
    cin >> price[i];
    for (int j = 0; j < M; j++) {
      cin >> books[i][j];
    }
  }

  Int ans = INF;
  // 2 ** N通り
  for(int bits = 0; bits < (1 << N); bits++) {
    for(int j = 0; j < M; j++) {
      ms[j] = 0;
    }
    Int sum_price = 0;
    for(int i = 0; i < N; i++) {
      // 買わない場合
      if(!(bits & (1 << (i)))) {
        continue;
      }
      // 買う場合
      sum_price += price[i];
      for(int j = 0; j < M; j++) {
        ms[j] += books[i][j];
      }
    }
    bool ok = true;
    for(int j = 0; j < M; j++) {
      if (ms[j] < X) {
        ok = false;
        break;
      }
    }
    if (ok) {
      ans = min(ans, sum_price);
    }
  }
  if (ans == INF) {
    cout << -1 << endl;
  } else {
    cout << ans << endl;
  }
  return 0;
}