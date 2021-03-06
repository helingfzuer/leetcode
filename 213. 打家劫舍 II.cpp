#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int rob(vector<int>& nums){
        int n=nums.size();
        if(n==0)  return 0;
        if(n==1)  return nums[0];
        int dp0=helper(nums, 1, n-1), dp1=helper(nums, 0, n-2);
        return max(dp0, dp1);
    }

    int helper(vector<int> &nums, int left, int right){
        if(left==right)  return nums[left];
        int dp0=nums[left], dp1=max(nums[left], nums[left+1]);
        for(int i=left+2;i<=right;i++){
            int tmp=max(dp1, dp0+nums[i]);
            dp0=dp1, dp1=tmp;
        }
        return dp1;
    }
};

int main(){
    int n, res;
    scanf("%d", &n);
    vector<int> nums(n);
    for(int i=0;i<n;i++)  scanf("%d", &nums[i]);
    Solution s;
    res=s.rob(nums);
    cout<<res<<endl;
    return 0;
}