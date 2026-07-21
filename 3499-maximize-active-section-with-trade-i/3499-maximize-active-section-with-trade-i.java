class Solution {
    public int maxActiveSectionsAfterTrade(String s) {
        int n = s.length();
        int ones = 0;
        for (char c : s.toCharArray()) {
            if (c == '1') ones++;
        }
        String t = "1" + s + "1";
        ArrayList<Character> ch = new ArrayList<>();
        ArrayList<Integer> len = new ArrayList<>();
        int i = 0;
        while (i < t.length()) {
            char c = t.charAt(i);
            int j = i;
            while (j < t.length() && t.charAt(j) == c) j++;
            ch.add(c);
            len.add(j - i);
            i = j;
        }
        int gain = 0;
        for (i = 1; i + 1 < ch.size(); i++) {
            if (ch.get(i) == '1'
                    && ch.get(i - 1) == '0'
                    && ch.get(i + 1) == '0') {
                gain = Math.max(gain,
                        len.get(i - 1) + len.get(i + 1));
            }
        }

        return ones + gain;
    }
}