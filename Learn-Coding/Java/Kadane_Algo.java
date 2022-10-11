// UseCase: To print largest contiguous array sum in O(n) time complexity

import java.io.*;
import java.util.*;

class KadaneAlgo {

	public static void main(String[] args)
	{
		int[] arr = { -2, 2, 0, -1, 4, 2, 5,};
		System.out.println("Maximum contiguous array sum is "+ maxSubArray(arr));
	}

	static int maxSubArray(int arr[])
	{
		int size = arr.length;
		int max_so_far = Integer.MIN_VALUE, max_ending_here = 0;

		for (int i=0;i<size;i++) {
			max_ending_here+=a[i];
			if (max_so_far < max_ending_here)
				max_so_far = max_ending_here;
			if (max_ending_here < 0)
				max_ending_here = 0;
		}
		return max_so_far;
	}
}
