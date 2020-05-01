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
using namespace std;
#define MOD 1000000007
#define MOD2 998244353
#define INF ((1<<30)-1)
#define LINF (1LL<<60)
#define EPS (1e-10)
typedef long long Int;
typedef pair<Int, Int> P;


Int n, W;
Int v[110], w[110];
Int dp[110][110000];

int main(){
    cin >> n >> W;
    for(int i = 1;i <= n;i++)cin >> w[i] >> v[i];

    for(int i = 1;i <= n;i++){
        for(int j = 0;j <= W;j++){
            dp[i][j] = dp[i-1][j];
            if(j-w[i] >= 0)
                dp[i][j] = max(dp[i][j], dp[i-1][j-w[i]] + v[i]);
        }
    }
    cout << dp[n][W] << endl;
    return 0;
}
