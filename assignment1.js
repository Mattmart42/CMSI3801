/*Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: T a c t Coa
Output: T r u e ( p e r m u t a t i o n s : " t a c o c a t " , " a t c o e t a " , e t c . )*/

function isPalindrome(query) {
    let lowQ = query.toLowerCase().split(" ").join("");
    let letters = {};
    let count = 0;

    for(let char of lowQ) {
        if (!letters[char]) {
            letters[char] = 1;
        }
        else {
            letters[char]++;
        }
    }
    for(l in letters) {
        if(letters[l] % 2) {
            count++;
        }
        if(count > 1) {
            return false;
        }
    }
    return true;
}

console.log(isPalindrome("cracera"));
console.log(isPalindrome("CracERa"));
console.log(isPalindrome("Cr acERa"));
console.log(isPalindrome("CracERat"));
console.log(isPalindrome("CracERatt"));
console.log((""));

/*Palindrome: Implement a function to check if a linked list is a palindrome.*/
class Node {
    constructor(next, data) {
        this.next = next;
        this.data = data;
    }
    append(data) {
        let child = new Node(null, data);
        let current = this;
        while(current.next !== null) {
            current = current.next;
        }
        current.next = child;
    }
}
function pally(head) {
    let current = head;
    let stack = [];
    while(current !== null) {
        stack.push(current.data);
        current = current.next;
    }
    current = head;
    for(i = 0; i < stack.length; i++) {
        if(current.data !== stack.pop()) {
            return false;
        }
        current = current.next;
    }
    return true;
}

let notPally = new Node(null, "a");
notPally.append("b");
notPally.append("c");
console.log(pally(notPally));

let isPally = new Node(null, "a");
isPally.append("b");
isPally.append("b");
isPally.append("a");
console.log(pally(isPally));