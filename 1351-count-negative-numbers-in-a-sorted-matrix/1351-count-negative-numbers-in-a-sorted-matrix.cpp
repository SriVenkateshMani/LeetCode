class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int res = 0;

        for (auto& row : grid) {
            int l = 0, r = row.size() - 1;
            int ans = row.size();   // index of first negative

            while (l <= r) {
                int mid = l + (r - l) / 2;

                if (row[mid] < 0) {
                    ans = mid;
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }
            res += row.size() - ans;
        }

        return res;
    }
};