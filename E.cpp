#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main() {
  int h, n;
  cin >> h >> n;
  
  vector<vector<double>> data(n, vector<double>(2));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < 2; j++) {
      cin >> data.at(i).at(j);
    }
  }
  sort(data.begin(), data.end());

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < 2; j++) {
      cout << data.at(i).at(j) << endl;
    }
  }

  int mincost_i = 0;
  int mincost = 1000
  for (int i = 0; i < n; i++) {
    if data.at(i).at(1) < mincost {
      mincost = data.at(i).at(1)
      mincost_i = i
    }
  }
  dp(hp, mincost_i)

  return 0;
}

int dp(int hp, int mincost_i) {
  int value;
  if (hp <= data.at(mincost_i).at(0) ) {
    return data.at(mincost_i).at(1);
  }
  else {
    value = min(dp(hp-1)+data.at(mincost_i).at(1), 
  }
}