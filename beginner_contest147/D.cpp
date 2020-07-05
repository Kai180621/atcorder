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
Int aes[1100000];
Int ans = 0;

int main()
{
  cin >> N;
  for(int i = 0; i < N; i++) {
    cin >> aes[i];
  }
  for(int i = 0; i < 60; i++) {
    for(int j = 0; j < N; j++) {
      if (aes[j] >> i&1) {
        ++x;
      }
      
    } 
  }

  return 0;
}