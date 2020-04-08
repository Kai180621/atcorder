#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main() {
  /* code */
  int h, n;
  cin >> h >> n;
  int skill;
  int sum_skill = 0;
  for(int i = 0; i < n; i++) {
    cin >> skill;
    sum_skill += skill;
  }
  if(sum_skill >= h){
    cout << "Yes" << endl;
  }
  else {
    cout << "No" << endl;
  }
  return 0;

}