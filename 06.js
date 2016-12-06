var lines = document.documentElement.innerText.split("\n")
lines = lines.splice(0, 572);

var solutionOne = "";
var solutionTwo = "";

var counter = [];
for(var i = 0; i < 8; i++) { 
    var collector = {};
    lines.forEach((value) => {
        if(!value) return;
        var char = value.charAt(i);
        if(!collector[char]) {
            collector[char] = 1;
            return;
        }
        collector[char] += 1;
    });
    counter[i] = collector;
}

counter.forEach((value) => {
    var keys = Object.keys(value);
    var max = 0;
    var letter = "";
    keys.forEach((key) => {
        if(max < value[key]) {
            max = value[key]
            letter = key;
        }
    });
    solutionOne += letter;
})

counter.forEach((value) => {
    var keys = Object.keys(value);
    var min = 50;
    var letter = "";
    keys.forEach((key) => {
        if(min > value[key]) {
            min = value[key]
            letter = key;
        }
    });
    solutionTwo += letter;
})

console.log("Column Selector One: " + solutionOne);
console.log("Column Selector Two: " + solutionTwo);
