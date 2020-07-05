#include <bits/stdc++.h>
using namespace std;
 
int N;
int A[20];
int x[20][20];
int y[20][20];
 
int counter(int x) {
    if(x == 0) return 0;
    return counter(x >> 1) + (x & 1);
}
 
void solve() {
    cin >> N;
    // 入力
    for(int i = 1; i <= N; i++) {
        cin >> A[i];
        for(int j = 1; j <= A[i]; j++) {
            cin >> x[i][j] >> y[i][j];
        }
    }
    int ans = 0;
    // bit演算 O(2**N)
    for(int bits = 1; bits < (1 << N); bits++) {
        bool ok = true;
        // 一人一人に対して処理
        for(int i = 1; i <= N; i++) {
            // 不親切な場合
            if(!(bits & (1 << (i-1)))) continue;
            // 正直な場合
            for(int j = 1; j <= A[i]; j++) {
                // 
                if(((bits >> (x[i][j]-1)) & 1) ^ y[i][j]) ok = false;
            }
        }
        if(ok) ans = max(ans, counter(bits));
    }
    cout << ans << endl;
    return;
}
 
int main() {
    solve();
    return 0;
}