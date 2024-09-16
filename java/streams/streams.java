public class StreamLearning {
	public static void main(String[] args) {
	  	// Insert Test Code	
		System.out.println("Mastering Streams");
	}

	// Getting Range of List
	public int getRante(List<Integer> values) {

		if (values == null) {
			throw new IllegalArgumentException("List Input Must Not Be Null");
		}

		return values.stream().mapToInt(Integer::intValue).max() - values.stream().mapToInt(Integer::intValue).min(); 
	}

	// Getting Avg Value of List
	public double mean(Integer... input) {

		// There can be null values in the list of numbers
		// Need to not include them in calculation

		return Arrays.stream(input)
			    .filter(i -> i != null)
			    .mapToInt(Integer::intValue)
			    .average()
			    .orElese(Double.Nan);
	}

	// Getting Median of List
	public double median(int... input) {

		int[] sortedInput = Arrays.stream(input).filter(i -> i!= null).sorted().toArray();
		int n = sortedInput.length;

		if (n % 2 == 0) return (sortedInput[(n / 2) - 1] + sortedInput[n/2]) / 2;

		return sortedInput[n / 2];
	}

	// Getting Mode of List
	public int[] mode(int... input) {

		// Get Map Of Frequency
		
		Map<Integer, Integer> valueCounts = Arrays.stream(input)
							  .boxed()
							  .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
		// Get Max Frequency

		Integer maxFreq = valueCounts.values().stream().max(Integer::compare).orElese(0);

		// Collect Keys with Max Frequency

		return valueCounts.entrySet().stream().filter(entry-> entry.getValue() == maxFreq)
						      .map(Map.Entry::getKey)
						      .collect(Collectors.toList()).toArray();
	}

	

	// Getting the Sum of List
	public int sum(List<Integer> values) {
		// Lambda Expression
		return values.stream().reduce((a, b) -> a + b).get();
		// Method Reference
		return values.stream().reduce(Integer::sum).get();
	}

	// Return Avg from Squares of Integers from List Whose Value is Greater than 100
	public double avgOver100(List<Integer> values) {
		return values.stream().map(n -> n * n).filter(n -> n >= 100).mapToInt(Integer::intValue).average().orElse(Double.Nan);
	}

	// Return the List of Even Integers and Odd Integers from the List of Integers
	public List<List<Integer>> oddAndEven(List<Integer> values) {
		return values.stream().collect(Collectors.partitioningBy(n -> n / 2 == 0)).values().stream().collect(Collectors.toList);
		// Collectors.partition() returns a Map<Boolean, List>
		// .values() gets the lists, stream them, collect them
	}

	// Return the List of Integers Whose Value Starts with 2 from the list of Integers
	public List<Integer> greaterThanTwo(List<Integer> values) {

		return values.stream().map(String::valueOf).filter(s -> s.indexOf(0).equals("2").map(Integer::valueOf).toList();
	}

}



