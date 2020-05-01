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

Int n;
Int happy[110000][3];
Int dp[110000][3];
// 0: umi
// 1: yama
// 2: HW

int main(){
    cin >> n;
    for(int i = 1;i <= n;i++){
        cin >> happy[i][0] >> happy[i][1] >> happy[i][2];
    }

    for(int i = 1;i <= n;i++){
        for(int place = 0;place < 3;place++){
            for(int placeY = 0; placeY < 3;placeY++){
                if(place == placeY)continue;
                dp[i][place] = max(dp[i][place],
                                   dp[i-1][placeY] + happy[i][place]);
            }
        }
    }
    
    Int ans = 0;
    for(int place = 0;place < 3;place++){
        ans = max(ans, dp[n][place]);
    }
    cout << ans << endl;
    return 0;
}
