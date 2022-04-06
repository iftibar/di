let sentence = 'the movie is bad not, i like it!';
let wordNot = sentence.indexOf('not');
let wordBad = sentence.indexOf('bad');
if (wordNot<wordBad) {
    sentence = sentence.replace(sentence.slice(wordNot, wordBad+3),'good');
    console.log(sentence);}
else {
    console.log(sentence);
}