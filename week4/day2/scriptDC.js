let longest = 0;
let string = prompt('few words of wisdom please');
arr = string.split(' ');
for (let word of arr) {
    if (word.length > longest) {
        longest = word.length;
    }
}
let newWord = '';
let space = 0;
function wrapWord(word, longest) {
    space = longest - word.length + 1;
    for (i = 0; i < space; i++) {
        word += ' ';
    }
    word = word + '*';
    newWord = "* " + word;
    console.log(newWord)
}
let frame = '';
for (i = 0; i < (longest + 4); i++) {
    frame += '*';
}
console.log(frame);
for (b=0; b<arr.length; b++) {
    wrapWord(arr[b], longest);
}
console.log(frame);

