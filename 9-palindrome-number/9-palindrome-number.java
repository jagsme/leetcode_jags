class Solution {
   public boolean isPalindrome(int x) {
        int oldNum= x;
        int reverseNum=0;
        while(x>0){
            reverseNum = reverseNum*10 + x%10;
            x = x/10;
        }
        if(oldNum==reverseNum)
            return true;
        else return false;
    }
}