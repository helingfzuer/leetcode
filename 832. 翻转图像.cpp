#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A){
        int m=A.size(), n=A[0].size();
        for(int i=0;i<m;i++)  reverse(A[i].begin(), A[i].end());
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++)  A[i][j]=1-A[i][j];
        }
        return A;
    }
};

int main(){
    int m, n;
    scanf("%d %d", &m, &n);
    vector<vector<int> > A(m, vector<int> (n));
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++)  scanf("%d", &A[i][j]);
    }
    Solution s;
    A=s.flipAndInvertImage(A);
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++)  cout<<A[i][j]<<" ";
        cout<<endl;
    }
    return 0;
}