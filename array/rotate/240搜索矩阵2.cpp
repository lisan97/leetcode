class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        if (m == 0) {
            return false;
        }
        bool found = false;
        int i = 0;
        int j = n - 1;
        while (i < m && j >= 0 && !found) {
            if (matrix[i][j] == target) {
                found = true;
            } else if (matrix[i][j] < target) {
                i++;
            } else {
                j--;
            }
        }
        return found;
    }
};