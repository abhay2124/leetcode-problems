class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> m1;
        
        for(int num : nums1) {
            m1.push_back(num);
        }
        

        for(int num : nums2) {
            m1.push_back(num);
        }
        
        sort(m1.begin(), m1.end());
        
        if(m1.size()%2==0){
            int n = m1.size();

            float s=(m1[(n/2)-1]+m1[(n/2)]);

            float t = s/2;

            return t;
            
        }
        if(m1.size()==1){
            return m1[0];
        }
        else{
            int x = m1[((m1.size() + 1) /2.0)-1];

            return x;
        }
        return 0;

    }
};