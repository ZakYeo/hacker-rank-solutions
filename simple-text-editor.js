// https://www.hackerrank.com/challenges/one-week-preparation-kit-simple-text-editor/problem

let textArea = "";
let textAreaHistory = [];
function processData(input) {
  operations = input.split("\n");
  for (let i = 1; i < operations.length; i++) {
    // Begin from 1 to skip number of operations

    if (operations[i][0] == "1") {
      // Append(W)
      textAreaHistory.push(textArea);
      const textToAppend = operations[i].split(" ")[1];
      textArea = textArea + operations[i].split(" ")[1];
    } else if (operations[i][0] == "2") {
      // delete(k)
      textAreaHistory.push(textArea);
      const numberToDelete = Number(operations[i].split(" ")[1]);
      textArea = textArea.slice(0, -numberToDelete);
    } else if (operations[i][0] == "3") {
      // print(k)
      console.log(textArea[Number(operations[i].split(" ")[1] - 1)]);
    } else {
      // Undo
      textArea = textAreaHistory.pop();
    }
  }
}
