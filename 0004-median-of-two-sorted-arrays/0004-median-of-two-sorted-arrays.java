class Solution {
    public static void sortedArray(int []arr){
        for(int i=0;i<arr.length;i++){
           for(int j=i+1;j<arr.length;j++){
            if(arr[i]>arr[j]){
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
           }
        }
    }
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int arr[]=new int[nums1.length+nums2.length];
        int index=0;
        for(int i=0;i<nums1.length;i++){
            arr[index++]=nums1[i];
        }
        for(int i=0;i<nums2.length;i++){
            arr[index++]=nums2[i];
        }
        sortedArray(arr);
        int median=0;
        if(arr.length%2==1){
             median=arr[arr.length / 2];
        }
        else{
            median=(arr[arr.length/2] + arr[(arr.length/2)-1])/2;

        }
        return median;
    }
    
}