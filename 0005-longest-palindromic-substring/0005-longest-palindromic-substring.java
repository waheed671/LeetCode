// class Solution {
//     public static String palindrome(String st){
//         String rev="";
//         for(int i=0;i<st.length();i++){
//             char ch=st.charAt(i);
//             rev=ch+rev;
//         }
//         return rev;
//     }
//     public String longestPalindrome(String s) {
//         String max=s.substring(0,1);
//        for(int i=0;i<s.length();i++){
//          for(int j=i+1;j<=s.length();j++){
//             String sub=s.substring(i,j);
//             String revSub=palindrome(sub);
//             if(sub.equalsIgnoreCase(revSub)){
//                 if(max.length()<sub.length()){
//                     max=sub;
//                 }
//             }
//          }
//        } 
//        return max;
//     }
// }
class Solution {

    // check palindrome using two pointers (O(n))
    public static boolean isPalindrome(String s, int left, int right) {
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public String longestPalindrome(String s) {

        String max = s.substring(0, 1);

        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {

                if (isPalindrome(s, i, j)) {
                    if (j - i + 1 > max.length()) {
                        max = s.substring(i, j + 1);
                    }
                }
            }
        }
        return max;
    }
}
