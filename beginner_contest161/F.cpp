#include <bits/stdc++.h>
#define rep(i,n) for (int i=0; i<(n); i++)
using namespace std;

const int INF = 1001001001;

int main() {
  int n;
  cin >> n;
  int ans = 0;
  int temp_n = n;

  for (int k = 2; k <= (n); k++){
    if(n % k != 0){
      if(n % k == 1){
        ans += 1;
        cout << "a:" << k << endl;
      }
      continue;
    }
    temp_n = n;
    while (temp_n % k == 0){
      temp_n = temp_n / k;
    }

    if (temp_n % k == 1) {
      ans += 1;
      cout << "b:" << k << endl;
    }
  }

  cout << ans << endl;
  return 0;
}