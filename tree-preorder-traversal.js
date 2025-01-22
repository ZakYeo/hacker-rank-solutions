/*
    Node is defined as
    var Node = function(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
*/

// https://www.hackerrank.com/challenges/one-week-preparation-kit-tree-preorder-traversal/problem

// This is a "method-only" submission.
// You only need to complete this method.

let stack = [];

function preOrder(root) {
  // Begin at the root
  let nodes = [];
  stack.push(root);
  while (stack.length > 0) {
    let currentNode = stack.pop();
    nodes.push(currentNode.data);
    if (currentNode.right) {
      stack.push(currentNode.right);
    }
    if (currentNode.left) {
      stack.push(currentNode.left);
    }
  }

  console.log(nodes.join(" "));
}
