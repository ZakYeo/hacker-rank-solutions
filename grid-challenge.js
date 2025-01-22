/*
 * Complete the 'gridChallenge' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING_ARRAY grid as parameter.
 */

// https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem

function gridChallenge(grid) {
  const sortedGridX = [];
  for (let i = 0; i < grid.length; i++) {
    sortedGridX.push(grid[i].split("").sort());
  }
  // We now have a grid that's sorted along the X axis
  console.log(sortedGridX);
  // Now we check the Y axis and check they are sorted

  for (let x = 0; x < sortedGridX[0].length; x++) {
    let previousLetter = sortedGridX[0][x];
    for (let y = 1; y < sortedGridX.length; y++) {
      // Assume each row is the same length
      console.log(`Comparing ${previousLetter} against ${sortedGridX[x][y]}`);
      console.log(`${x} ${y}`);
      if (previousLetter > sortedGridX[y][x]) {
        return "NO";
      }
      previousLetter = sortedGridX[y][x];
    }
  }
  return "YES";
}
