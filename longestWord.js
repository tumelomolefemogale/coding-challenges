/* Given a sentence, return the longest word in the sentence.
Ignore periods (.) when determining word length.
If multiple words are ties for the longest, return the first one that occurs. */

const getLongestWord = sentence => {
    let lengthArray = [];
    let sentenceArray = sentence.replace('.', '').split(' ');

    for (element of sentenceArray) {
        lengthArray.push(element.length)
    }

    let maxIndex = lengthArray.indexOf(Math.max(...lengthArray));
    const longestWord = sentenceArray[maxIndex];

    return longestWord;

};

console.log(getLongestWord("The streetlights flickered like they were second-guessing their loyalty to the dark"));
console.log(getLongestWord("The medical student casually mentioned pneumonoultramicroscopicsilicovolcanoconiosis as if it were just another Tuesday vocabulary word."));
console.log(getLongestWord("The quick brown fox jumps over the lazy dog."));
