/*
Given an array, determine if it is flat.
An array is flat if none of its elements are arrays
*/

const isFlat = array => {
    let count = 0;
    for (element of array) {
        if (Array.isArray(element)) {
            count++;
        };
    }
    if (count === 0) {
            return true
    } else {
            return false
      }
};

console.log(isFlat([1, 2, 3, 4]));
console.log(isFlat([1, [2, 3], 4]));
console.log(isFlat([1, 0, false, true, "a", "b"]));
console.log(isFlat(["a", [0], "b", true]));
console.log(isFlat([1, [2, [3, [4, [5]]]], 6]));