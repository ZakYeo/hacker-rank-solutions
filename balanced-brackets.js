// https://www.hackerrank.com/challenges/one-week-preparation-kit-balanced-brackets/problem

const bracketPairs = {
  "[": "]",
  "{": "}",
  "(": ")",
};
function isBalanced(s) {
  let queue = [];
  for (let i = 0; i < s.length; i++) {
    if (Object.keys(bracketPairs).includes(s[i])) {
      // This is an opening bracket
      // Add it to our queue
      queue.push(s[i]);
    } else {
      // This is a closing bracket
      // Pop and compare
      let bracketToTestAgainst = queue.pop();
      if (bracketToTestAgainst == undefined) {
        return "NO";
      }
      console.log(
        `Bracket ${s[i]} testing against ${bracketToTestAgainst} in dict: ${bracketPairs[bracketToTestAgainst]}`
      );
      if (bracketPairs[bracketToTestAgainst] != s[i]) {
        return "NO";
      }
    }
  }
  if (queue.length > 0) {
    return "NO";
  }
  return "YES";
}
