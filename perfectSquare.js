/* Given an integer, determine if it is a perfect square.
A number is a perfect square if you can multiply an integer by itself to achieve the number.
For example, 9 is a perfect square because you can multiply 3 by itself to get it. */

const isPerfectSquare = number => {
    if (Number.isInteger(Math.sqrt(number))) {
        return true;
    } else {
        return false;
    }
};

console.log(isPerfectSquare(9));
console.log(isPerfectSquare(49));
console.log(isPerfectSquare(1));
console.log(isPerfectSquare(2));
console.log(isPerfectSquare(99));
console.log(isPerfectSquare(-9));
console.log(isPerfectSquare(0));
console.log(isPerfectSquare(25281));
