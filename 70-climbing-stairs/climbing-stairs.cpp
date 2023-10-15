class Solution {
public:
    int solver(int n, vector<int> &dp) {
        if(n <= 1) return n;
        if(dp[n] != -1) return dp[n];
        return dp[n] = solver(n-1, dp) + solver(n-2, dp);
    }
    int climbStairs(int n) {
        vector<int> dp(n+2, -1);
        return solver(n+1, dp);
    }
};