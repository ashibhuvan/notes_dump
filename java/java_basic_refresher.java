Java Notes to touch up on

Main principles of OOP are

	1. Abstraction
	2. Encapsulation
	3. Inheritance
	4. Polymorphism
// Examples
// Abstraction
abstract class Shape {
	abstract double calculateArea();
}

class Circle extends Shape {
	private double radius;

	public Circle(double radius) {
		this.radius = radius;
	}
	
	@Override
	double calculateArea() {
		return Math.PI * radius * radius;
	}
}
// Abstract class serves as a base class to define common interface and common functionality for a group of 
// related subclasses. Abstract classes can contain both abstract and concrete methods. Lets you define some behaviour 
// or leave some to be defined
//
// Provides a template for subclasses to follow, ensuring that certain methods are implemented
//
// Abstract classes can contain fields and concrete methods that subclasses can inherit
// They let you define abstract concepts without full implementation, which is useful for representing general ideas or protocols
//
//
// Encapsulation
// No need for example, its just procedure of combining the data members and data methods of the class inside a user defined class
//
// Inheritance
class Animal {
	protected String name;
	public Animal(String name) {
		this.name = name;
	}
	public void eat() { System.out.println(name + " is eating"; }
}
class Dog extends Animal {
	public Dog(String name) {
		super(name);
	}
}
// Polymorphism
// Lets you define an common interface while
// Lets you define an interface and have different implementations while being the same 'type' of object
//

Random Tibits

- Default value of an object reference defined as an instance variable in an object is null
- Java provides a default constructor
- Abstract method have no body
- final method cannot be overridden 
- static method belongs to the class but no particular object
	- therefore constructor cannot be static, final, or abstract
- this refers to current instance of the object
- Object class in java is the super class of every other class
- You cannot have multiple inheritance in Java but you can implement multiple interfaces in Java

- Java uses references instead of pointers which points to objects in memory but you cannot directly access memory locations
- super() keyword refers to the immediate parent class of an object

-Object.clone() creates an exact copy of the object in Java. Returns object and has to be type cast
- static variables are common to all the objects of a class
- static method lets you control behaviour at the class level.
- to call a static method you do not need to create an object, to call instance method you need an object
- can do method overloading with different number of parameters, different data type of params, or different sequence of data
- types for params
- method overloading is static polymorphism, method overriding is runtime polymorphism
- method overriding is dynamic polymorphism because the known method to call is not known until runtime

- abstract class in java has one or more abstract methods. abstract class has to be extended in java and its abstract
methods have to be implemented by a child class. 

- if there is at least one abstract method in a class, the class has to be marked as abstract
- you cannot create an instance of an abstract class in java


- interface is abstract type blueprint of a class. contains methods the class must implement.
- you can define static and default methods in an interface

Difference between Abstract class and Interface 
1. Abstract class can have non abstract methods. Interface only has abstract methods
2. Abstract class can have instance member variables. Interface can only have constants
3. Abstract class can have a constructor while interface cannot
4. A class can only extend one abstract class but a class can implement multiple interfaces

- You can prohibit inheritance by marking a class as final, it cannot be extended
- mark member variables of an object as transient to indicate they should not be serialized

// Exceptions
//
Exception handling lets you handle runtime errors in JVM
Checked exceptions extend throwable class but they do not extend RuntimeException or Error classes.
Error class and Exception class are derived from Throwable class in java

try {}
catch {}
finally {}

throw keyword lets you throw an exception from a method or static block
throws is a method signature that lets JVM know what type of exception it throws

// Collections Framework
// 1. List (ArrayList, LinkedList, Vector, Stack)
// 2. Set (hashset, linkedhashset, treeset)
// 3. Queue (PriorityQueue, LinkedList)
// 4. Deque (ArrayDeque, LinkedList)
// Map (HashMap, LinkedHashMap, TreeMap, Hashtable)
//
ArrayList.toArray returns Array
Arrays.asList(list) returns list

HashSet elements are stored in random order
TreeSet elements are stored according to natural ordering

Hashmap is not sychronized collection and does not have thread safety
HashTable is synchronized collection
HashMap allows one null key and any null values
HashTable does not allow null keys and values

HashTable can neve rgaruntee ordering of elements

Hashmap has no order of its keys
TreeMap elements are sorted to natural ordering of elements
Hashmap uses hashing, treemap uses red-black tree implementation
HashMap implements Map interface
TreeMap implements Navigable Interface

when using hashCode() to get a hash code value, Object generates on memory address of instance

Queue
peek() lets you look at head, poll() will return null if queue is empty, remove() will throw nosuchmethod exception

Collectionns has static CollectionsynchronizedCollection(Collection c) that lets you turn a collection into a thread safe one
Threads and Processes
Process is an independent program in execution which contains its own memory space, code, data, and system resources
Every process runs in its own address space and has at least one thread but can have multiple threads
Thread is a smaller unit of a process. Threads within the same process share the same memory and resources but can execute
independently.

Process communicate with other processes with mechanisms like pipes, sockets, or shared memory which can be slower
Threads can communicate directly by accessing shared variables or objects in the same memory space but risk of concurrency issues

In java the process generally refers to the running of the JVM and threads live within the JVM
Due to this logic, each java program has at least one thread.

A java thread has the follwing: unique identifier (long), name (string), priority (int), state (java.lang.Thread.State),
Group (thread group)

A thread in java can be:
	New: not started yet
	Runnable: A thread exeucting in JVM is in runnable state
	Blocked: Thread waiting for a monitor lock
	Waiting: Thread waiting for another thread
	Timed_Waiting: thread waiting for another thread to preform an action upto a waiting time
	Terminate: A thread that has exited is in its terminated state
setPriority(int priority) 
Thread.MAX_PRIORITY, Thread.MIN_PRIORITY, Thread.NORM_PRIORITY

Every thread belongs to a group of threads. Lets you take collection action on threads

Create a thread in Java :
1. Extend Thread Class , java.lang.Thread and implement run() or calling start()
2. Implement java.lang.Runnable interface and pass the implemented object to the constructor of java.lang.Thread
	call start() and it starts running
3. ExecutorService lets you create a fixed thread pool and submit threads to it
4. Using Callable interface with ExecutorService
5. Timer class
6. ForkJoinPool

BusyWaiting is busy looping or spinning where you repeatedly check if a condition is true
Can be wastepul of compute
Use thread.sleep() to avoid this

Marking a method as synchronized, the method will acquire the intrinsic lock of the object that the method is using
Releases the lock once the method returns

Atomic operation is an operation that completes in a single step relative to other threads. Its either executed completely or not at all

Creating a threadpool with ExecutorService:
ExecutorService myService = Executors.newFixedThreadPool(5);
Future<Integer>[] futureList = new Future[5];
for (int i = 0; i < futureList.length; i++) {
	futureList[i] = myService.submit(new MyCallable());
}
for (int i = 0; i < futureList.length; i++) {
	Integer retVal = futureList[i].get();
	println(retVal);

Use Future interface to represent the result of an asynchronous computation
has isDone() to check if finished.

In Java, stacka nd heap are memory spaces that are available to an application. Every thread has its own stack
for variables, method parameters, and call stack. Local variables in one stack of a thread are not visible to another thread

Heap is a comon memory area in JVM that is shared by all threads. All objects are created in heap

Lambda expression is an anonymous function that accepts a set of input parametrs and returns a result.
Can be passed as a param in method so it is like a piece of data

Functional interface in Java is an interface that has exactly one abstract method
Intermediate vs Terminal Stream operations

1. Intermediate operations are not evaluated until we chain it with a terminal operation of stream
2. Output of intermediate operations is another stream. Output of terminal operations is not a stream
3. Intermediate is evaluated in a lazy manner, terminal in eager manner
4. Intermediate operations can be chained multiple times, terminal cannot
5. There are multiple intermediate operations in a stream operation but only one terminal operation

In Java 8 you can now provide a default method or static method in an interface and provide implementation
Static method as helper methods in interface

Optional is a container object that may have a null or non null value. Use to avoid nullpointerexception





.
