//javascript style is to capitalize
//every word except for the first

//example: fuzzyLittleTurtle

/*
Looping a triangle
Write a loop that makes seven calls to console.log to output the following triangle:

#
##
###
####
#####
######
#######
It may be useful to know that you can find the length of a string by writing .length after it.

let abc = "abc";
console.log(abc.length);
// → 3
Most exercises contain a piece of code that you can modify to solve the exercise. Remember that you can click code blocks to edit them.
*/
let spare = " "
while(spare.length <= 7) {
  spare += "#"
  console.log(spare)
}
console.log(spare)
