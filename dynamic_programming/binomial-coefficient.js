/*
	Author: Jaelson Carvalho
	Node.js v6.2.2
	Usage: node binomial-coefficient.js

	Inspired by:
		http://www.geeksforgeeks.org/dynamic-programming-set-9-binomial-coefficient/
		https://en.wikipedia.org/wiki/Binomial_coefficient
*/

var binomial_coefficient = function(n, k) {
	if(n >= k && k >= 0) {
		/*
			Create pascal triangle
		*/
		var C = new Array(k+1);
		/*
			Set 0 value to every positions of the array
		*/
		C.fill(0);

		/*
			Set the first position with 0
		*/
		C[0] = 1;

		for (var i = 0 ; i <= n ; i++) {

			/*
				Calculate the current row of pascal triangle using the previous row
        	*/
			j = Math.min(i, k) ;
			while(j > 0) {
				C[j] = C[j] + C[j-1];
				j--;
			}

		}

		return C[k];
	}
	else {
		return -1;
	}
}

module.exports = {
  binomial_coefficient: binomial_coefficient,
}

//console.log(binomial_coefficient(0, 0));
