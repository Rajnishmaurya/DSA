class Solution {
public:
    bool ispalindrome(string s,int i,int j)
    {
        int start=i;
        int end=j;
        while(start<end)
        {
            if(s[start]!=s[end])
            {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
    int countSubstrings(string s) {
        int result=0;
        int n=s.size();
        vector<vector<int>>dp(n,vector<int>(n,-1));

        for(int i=0;i<n;i++)
        {
            for(int j=i;j<n;j++)
            {
                if(i-1>=0 && j+1<n && dp[i][j]!=-1)
                {
                    result++;
                }
                else if(ispalindrome(s,i,j))
                {
                    result++;
                    dp[i][j]=1;
                }
            }
        }
        return result;
        
    }
};