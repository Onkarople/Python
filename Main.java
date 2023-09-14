
import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {

        Scanner sobj = new Scanner(System.in);

        int No = sobj.nextInt();

        int k = sobj.nextInt();

        String s = Integer.toString(No);

        char Arr[] = s.toCharArray();
        char j = '1';

        for (int i = 0; i < k; i++) {
            Arr[i] = j;

        }

        String N = Arr.toString();
        int No1 = Integer.parseInt(N);

        System.out.println(No1);

    }
}
