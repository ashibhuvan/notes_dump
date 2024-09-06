# printing
console.log('Hello, World');

# Run tsc command to compile typescript to js
# Run node filename.js to run file

# Typescript variables can never be reassigned

let aged = true;
let realAge = 0;

if (aged) {
	realAge = 4;
}

let dogAge = realAge * 7;
console.log(`${dogAge} years`); # String interpolation in typescript is awful


##################################
let firstName = 'muriel';
console.log(firstName.toUpperCase());
console.log(firstName.length);
##################################
## You can reassign variable if its not assigned at initialization ## Why?

let guess;
guess = 'green'
guess = 5

### Type Annotations for Variables ###

let mustBeAString : string;
mustBeAString = 'CatDog';

let conditional : boolean;
let phoneNumber : number;
let random : any;

#### Terrible Syntax ###
#### Tsconfig.json ###
{
	"compilerOptions": {
		"target": "es2017",
		"module": "commonjs",
		"strictNullChecks": true
	},
	"include": ["**/*.ts"]
}
### Functions ###

function printOperations(a, b) {
	if (typeof a != 'number' or typeof b != 'number') {

		throw new Error('both arguments must be numbers!');
	}
	console.log(a + b, a / b);
}

### Functions with typ annotations ###
function triple(value : number) {
	return value * 3
}

### Optional Parameters
function triple(value: number, msg?: string) {
	console.log(number * 3);
	console.log($(msg) || 'No msg supplied');
}
### Return Types ###


