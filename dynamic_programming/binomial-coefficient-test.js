/*
	Author: Jaelson Carvalho
	Node.js v6.2.2
	Usage: node binomial-coefficient-test.js
*/

var test = require('./binomial-coefficient.js');
var assert = require( 'assert' );

/*
	- According to the Node.js source and doc, the assert
	message is only printed when the assertion fails.

	- All results can be checked in http://www.ohrt.com/odds/binomial.php
*/
assert.strictEqual(test.binomial_coefficient(0, 0), 1, 'C(n=8, k=0) => 1');
assert.strictEqual(test.binomial_coefficient(6, 6), 1, 'C(n=6, k=6) => 1');
assert.strictEqual(test.binomial_coefficient(8, 0), 1, 'C(n=8, k=0) => 1');
assert.strictEqual(test.binomial_coefficient(4, 2), 6, 'C(n=4, k=2) => 6');
assert.strictEqual(test.binomial_coefficient(5, 2), 10, 'C(n=5, k=2) => 10');
assert.strictEqual(test.binomial_coefficient(15, 11), 1365, 'C(n=15, k=11) => 1365');
assert.strictEqual(test.binomial_coefficient(50, 3), 19600, 'C(n=50, k=3) => 19600');
assert.strictEqual(test.binomial_coefficient(31, 17), 265182525, 'C(n=50, k=3) => 265182525');
assert.strictEqual(test.binomial_coefficient(70, 15), 721480692460864, 'C([n=70, k=15) => 721480692460864');

assert.strictEqual(test.binomial_coefficient(1, 2), -1, 'C(n=1, k=2) => The "k" should be less or equal to n');
assert.strictEqual(test.binomial_coefficient(3, 7), -1, 'C(n=3, k=7) => The "k" should be less or equal to n');

assert.strictEqual(test.binomial_coefficient(13, -2), -1, 'C(n=13, k=-2) => The "k" should be non-negative number');
assert.strictEqual(test.binomial_coefficient(3, -2), -1, 'C(n=13, k=-2) => The "k" should be non-negative number');

/*
	- Sucess message after unit tests
*/
console.log("All tests concluded with success ! ");