/* Given an array of integers representing the coins in your pocket, with each integer being the value of a coin in cents, return the total amount in the format "$D.CC".

100 cents equals 1 dollar.
In the return value, include a leading zero for amounts less than one dollar and always exactly two digits for the cents. */

const countChange = arr => {
    let cents = arr.reduce((a, b) => a + b, 0);

    if (cents < 100) {
        let rounded = (cents / 100).toFixed(2);
        return `$${rounded}`
    } else {
        let dollars = 0;
        while (cents >= 100) {
            cents -= 100;
            dollars++;
        }

        return `$${dollars}.${cents.toString().padStart(2, "0")}`;
    }
}

console.log(countChange([25, 10, 5, 1]));
console.log(countChange([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25]));
console.log(countChange([100, 25, 100, 1000, 5, 500, 2000, 25]));
console.log(countChange([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10]));
console.log(countChange([1]));
console.log(countChange([25, 25, 25, 25]));
