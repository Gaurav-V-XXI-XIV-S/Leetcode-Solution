class Solution {
    public int[] closestPrimes(int left, int right) {
        boolean[] prime = new boolean[right + 1];
        Arrays.fill(prime, true);
        if (right >= 0) prime[0] = false;
        if (right >= 1) prime[1] = false;
        for (int i = 2; i * i <= right; i++) {
            if (prime[i]) {
                for (int j = i * i; j <= right; j += i) {
                    prime[j] = false;
                }
            }
        }
        int prev = -1;
        int minGap = Integer.MAX_VALUE;
        int[] ans = {-1, -1};

        for (int i = left; i <= right; i++) {
            if (prime[i]) {
                if (prev != -1) {
                    if (i - prev < minGap) {
                        minGap = i - prev;
                        ans[0] = prev;
                        ans[1] = i;
                    }
                }
                prev = i;
            }
        }
        return ans;
    }
}