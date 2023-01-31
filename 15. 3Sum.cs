// Not familiar with the C# grammar, but this method is subtle.
// Should try the HashSet solution in the future.
public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums){
        var res = new List<IList<int>>();
        var s = new HashSet<string>();
        Array.Sort(nums);
        var n = nums.Length;
        for (int i = 0; i < n - 2; i++){
            int start = i + 1;
            int end = n - 1;
            while (start < end){
                if (nums[i] + nums[start] + nums[end] >= 0){
                    if (nums[i] + nums[start] + nums[end] == 0){                            
                        var tmp = new int[]{nums[i], nums[start], nums[end]};
                        var key = string.Join(",", tmp);
                        if (s.Add(key))
                            res.Add(tmp.ToList());
                        start++;                           
                    }    
                    end--;                        
                }else{
                    start++;
                }
            }
        }
        return res;
    }
}