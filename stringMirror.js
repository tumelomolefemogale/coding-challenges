// Given a string, return a new string that consists of the given string with a reversed copy of itself appended to the end of it.

const mirror = string => {
    let mirroredString = [];

    for (i = string.length - 1; i >= 0; i--) {
    mirroredString.push(string[i])
    };

    return string + mirroredString.join('');
};

console.log(mirror('freeCodeCamp'));
console.log(mirror('RaceCar'));
console.log(mirror('helloworld'));
console.log(mirror('The quick brown fox...'));
