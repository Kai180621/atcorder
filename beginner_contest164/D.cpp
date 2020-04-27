#include <bits/stdc++.h>
#define rep(i,n) for (int i=0; i<(n); i++)
using namespace std;
using ll = long long;
using P = pair<int,int>;

const int INF = 1001001001;

int main() {

  string s;
  cin >> s;
  int l = s.length();
  int ans = 0;

  for(int i = 0; i < l - 3; i++) {
    for(int j = i + 4; j < l; j++) {
      string substr = s.substr(i, j);
      if (atoi(substr.c_str()) % 2019 == 0) {
        ans += 1;
      }
    }
  }
  cout << ans << endl;

  return 0;
}