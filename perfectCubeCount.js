/*
Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.
The lower number is not guaranteed to be the first argument.
A number is a perfect cube if there exists an integer (n) where n * n * n = number.
For example, 27 is a perfect cube because 3 * 3 * 3 = 27
*/

const countPerfectCubes = (a, b) => {
    let count = 0;

    const minimum = Math.min(a, b);
    const maximum = Math.max(a, b);

    for (i = minimum; i <= maximum; i++) {
        if (Number.isInteger(Math.cbrt(i))) {
            count++;
        }
    };
    return count;
}

console.log(countPerfectCubes(3, 30));
console.log(countPerfectCubes(1, 30));
console.log(countPerfectCubes(30, 0));
console.log(countPerfectCubes(-64, 64));
console.log(countPerfectCubes(9214, -8127));
