/*
Given a window size, the width of an element in viewport width "vw" units, and the height of an element in viewport height "vh" units, determine the size of the element in pixels.
The given window size and returned element size are strings in the format "width x height", "1200 x 800" for example.
"vw" units are the percent of window width. "50vw" for example, is 50% of the width of the window.
"vh" units are the percent of window height. "50vh" for example, is 50% of the height of the window.
*/

const getElementSize = (windowSize, elementVw, elementVh) => {
    let windowSizeArray = windowSize.split(' x ');
    
    let width = Number(windowSizeArray[0]);
    let height = Number(windowSizeArray[1]);

    const elementVwPercent = parseInt(elementVw) / 100;
    const elementVhPercent = parseInt(elementVh) / 100;

    width = elementVwPercent * width;
    height = elementVhPercent * height;

    return `${width} x ${height}`
};

console.log(getElementSize("1200 x 800", "50vw", "50vh"));
console.log(getElementSize("320 x 480", "25vw", "50vh"));
console.log(getElementSize("1000 x 500", "7vw", "3vh"));
console.log(getElementSize("1920 x 1080", "95vw", "100vh"));
console.log(getElementSize("1200 x 800", "0vw", "0vh"));
console.log(getElementSize("1440 x 900", "100vw", "114vh"));