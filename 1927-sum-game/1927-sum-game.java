class Solution {
    public boolean sumGame(String num) {
        int n = num.length();
        int half = n / 2;
        int sum = 0;
        int a1 = 0;
        int a2 = 0;
        for (int i = 0; i < half; i++) {
            char ch = num.charAt(i);
            if (ch == '?') {
                a1++;
            } else {
                sum += ch - '0';
            }
        }
        for (int i = half; i < n; i++) {
            char ch = num.charAt(i);
            if (ch == '?') {
                a2++;
            } else {
                sum -= ch - '0';
            }
        }
        int aDiff = a1 - a2;
        if (aDiff % 2 != 0) {
            return true;
        }
        return sum + (aDiff / 2) * 9 != 0;
    }
}