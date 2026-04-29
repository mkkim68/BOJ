import java.util.Arrays;

class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        
        Arrays.sort(routes, (o1, o2) -> {
            return o1[0]-o2[0];
        });
        
        int length = routes.length;
        int s = routes[0][0];
        int e = routes[0][1];
        for ( int i=1; i<length; i++ ) {
            
            int start = routes[i][0];
            int end = routes[i][1];
            
            if (start <= e) {
                s = start;
                e = Math.min(end, e);
            } else {
                answer++;
                s = start;
                e = end;
            }
        }
        
        return answer+1;
    }
}