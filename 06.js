let lines = document.documentElement.innerText.split("\n")
lines = lines.splice(0, lines.length - 1);

let solutionOne = "";
let solutionTwo = "";

const selector = (ref, original, value, result, func) => {
    if(func(ref, value)) {
        return [value, result];
    }
    return [ref, original];
}

let counter = [];
// strings are evenly distributed, no need to check it each time
for(var i = 0; i < lines[0].length; i++) { 
    const collector = {};
    lines.forEach((value) => {
        if(!value) return;
        let char = value.charAt(i);
        if(!collector[char]) {
            collector[char] = 1;
            return;
        }
        collector[char] += 1;
    });
    counter[i] = collector;
}

counter.forEach((value) => {
    let max = [0, ""];
    let min = [lines.length, ""];
    const keys = Object.keys(value);
    keys.forEach((key) => {
        max = selector(max[0], max[1], value[key], key, (a, b) => { return a < b; });
        min = selector(min[0], min[1], value[key], key, (a, b) => { return a > b; });
    });
    solutionOne += max[1];
    solutionTwo += min[1];
})

console.log("Column Selector Part One: " + solutionOne);
console.log("Column Selector Part Two: " + solutionTwo);
