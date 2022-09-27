class Solution {
    public int lengthOfLastWord(String s) {
        String [] str = s.split(" ");
        int count=str.length-1;
        return str[count].length();
    }
}