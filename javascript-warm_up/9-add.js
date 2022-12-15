#!/usr/bin/node
const args = process.argv.slice(2);
// prints the addition of 2 integers
function add (a, b) {
  console.log(a + b);
}
add(Number(args[0]), Number(args[1]));
