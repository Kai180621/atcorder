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
int order[30000];

int main() {
  cin >> N;
  int chairs[N][N];
  for(int i = 0; i < N; i++) {
    for(int j = 0; j < N; j++) {
      chairs[i][j] = N * i + j + 1;
    }
  }
  for(int i = 0; i < pow(N, 2); i++) {
    cin >> order[i];
  }

  for(int i = 0; i < pow(N, 2); i++) {
    
  }



  return 0;
}