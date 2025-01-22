// Complete the mergeLists function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */

// https://www.hackerrank.com/challenges/one-week-preparation-kit-merge-two-sorted-linked-lists/problem
function mergeLists(head1, head2) {
  //console.log(head1);
  //console.log(head2);
  let sortedArray = [];
  let nextItem = head1;
  while (nextItem.next != null) {
    sortedArray.push(nextItem.data);
    nextItem = nextItem.next;
  }
  sortedArray.push(nextItem.data);
  nextItem = head2;
  while (nextItem.next != null) {
    sortedArray.push(nextItem.data);
    nextItem = nextItem.next;
  }
  sortedArray.push(nextItem.data);
  sortedArray = sortedArray.toSorted((a, b) => a - b);
  // Now from the sorted array, create a newly linked list with our items
  // Begin with the first item
  let previousLinkedList = new SinglyLinkedListNode(sortedArray.at(-1)); // Start with the last element
  previousLinkedList.next = null;
  console.log(previousLinkedList);

  for (let i = sortedArray.length - 2; i >= 0; i--) {
    let linkedList = new SinglyLinkedListNode(sortedArray[i]);
    linkedList.next = previousLinkedList;
    previousLinkedList = linkedList;
  }
  return previousLinkedList;
}
