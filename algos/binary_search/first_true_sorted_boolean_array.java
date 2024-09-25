


public static void main(String[] args) {

	// Run Function Here
}

public int getBoundaryIndex(List<Boolean> input) {

	int left = 0;
	int right = 0;
	int boundary = -1;

	while (left <= right) {
		int mid = (left + right) / 2;
		if (input.get(mid) == true) {
			right = mid - 1;
			boundary = mid;
		} else {
			left = mid + 1;
		}

	}
	return boundary;
}
