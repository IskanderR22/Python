

// /* 
//     Acronyms
//     Create a function that, given a string, returns the string’s acronym 
//     (first letter of each word capitalized). 
//     Do it with .split first if you need to, then try to do it without
// */

// const str1 = " there's no free lunch - gotta pay yer way. ";
// const expected1 = "TNFL-GPYW";

// const str2 = "Live from New York, it's Saturday Night!";
// const expected2 = "LFNYISN";

// function acronymize(str) {

//     // SETUP
// 	var wordsArr = str.split(" ") // Splits the original string into an array ["there's", "no", "free", "lunch"] etc
// 	var arr = []  // Create a variable to hold the new list of new letters

//     // WORK
// 	for( var i = 0; i < wordsArr.length; i++){ // Go through the new array  ^^^ [0, 1, 2, 3,]
// 		var acr = wordsArr[i].split('') // Create a new varible to hold splitting the words
//                                         // Split each word into letters, ["t", "h", "e", "r", "e",',"s",] -> [0, 1, 2, 3, 4, 5, 6, 7]
// 		arr.push(acr[0]) // Push the index of 0 at this new array into our first arr variable 
// 	}
//     // RETURN OR PRINT
// 	console.log(arr.join('').toUpperCase()) // This will remove the spaces between the varibles and uppercase the letters 
//                                             // And making it a string 
// } 

// acronymize(str1)


// /* 
//     String: Reverse
//     Given a string,
//     return a new string that is the given string reversed
// */

// const str1 = "creature";
// const expected1 = "erutaerc";

// const str2 = "dog";
// const expected2 = "god";

// function reverseString(str) {
//     // SETUP
// 	var reversed = " "

//     //WORK
// 	for( var i = str.length - 1 ; i >= 0; i-- ){ // This will start i at the end of the string value 2, 1, 0 so for dog, g, o, d
// 		reversed += str[i] // This will add the index value at i to our new variable
// 	}

//     //RETURN
// 	return reversed; // This returns our new string to our function 
// }

// reverseString(str1)
// reverseString(str2)
// console.log(reverseString(str2)) // This will print the return value of the function with the argument sent.




// Algos 07/08/2020

/* 
Parens Valid
	Given an str that has parenthesis in it
	return whether the parenthesis are valid
// */

// const str1 = "Y(3(p)p(3)r)s";
// const expected1 = true;

// const str2 = "N(0(p)3";
// const expected2 = false;
// // Explanation: not every parenthesis is closed.

// const str3 = "N(0)t ) 0(k";
// const expected3 = false;
// // Explanation: because the underlined ")" is premature: there is nothing open for it to close.

// const str4 = "a(b))(c";
// const expected4 = false;
// // Explanation: same number of opens and closes but the 2nd closing closes nothing

// function parensValid(str) {
//     var count = 0;
//     for( var i = 0; i < str.length; i++){
//         if(str[i] == "("){
//             count++;
//         }
//         else if (str[i] == ")"){
//             count--;
//         }

//         if(count < 0){
//             return false;
//         }
//     }
//     if(count == 0){
//         return true;
//     }
//     else{
//         return false;
//     }
// }

// var newString = parensValid(str3)
// console.log(newString);


/*****************************************************************************/

/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2 = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3 = "A(1)s[O (n]0{t) 0}k";
const expected3 = false;

function parensValid(str1) {
    testArray = []
    for(i = 0; i < str.length-1; i++){   
        if (str[i]=="(" || str[i]=="{" || str[i]=="["){;
            testArray.push(str[i]);
        } 
        else if(str[i]==")"){
        if(testArray.length==0)return false;
        else if(testArray[testArray.length-2]=="("){
            testArray.pop();
        }
        }
        else if(str[i]=="}"){
        if(testArray.length==0)return false;
        else if(testArray[testArray.length-2]=="{"){
                testArray.pop();
        }
        }        
        else if(str[i]=="]"){
        if(testArray.length==0)return false;
        else if(testArray[testArray.length-2]=="["){
                testArray.pop();
        }
    }
}
    if(testArray.length==0){
        return true;
    }
    else return false;
}


var test = parensValid(str1);

console.log(test);



// Algos 07/09/2021

/* 
String: Is Palindrome
Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards

Do not ignore spaces, punctuation and capitalization
 */

const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

function isPalindrome(str) {
    if(str.length <2) return false;
    for(var i = 0; i<str.length/2; i++){
        if(str[i]!=str[str.length-i-1])
        return false;

    }
    return true;
}

/*****************************************************************************/

/* 
Longest Palindrome
    For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring. 
    Strings longer or shorter than complete words are OK.
    All the substrings of "abc" are:
    a, ab, abc, b, bc, c
  */

const str1 = "what up, daddy-o?";
const expected1 = "dad";

const str2 = "uh, not much";
const expected2 = "u";

const str3 = "Yikes! my favorite racecar erupted!";
const expected3 = "e racecar e";

function longestPalindromicSubstring(str) {}




// Algos 07/12/2021

/* 
String Encode
You are given a string that may contain sequences of consecutive characters.
Create a function to shorten a string by including the character,
then the number of times it appears. 


If final result is not shorter (such as "bb" => "b2" ),
return the original string.
*/

const str1 = "aaaabbcddd";
const expected1 = "a4b2c1d3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

function encodeStr(str) {
    var newArray = [];
    

}

/*****************************************************************************/

/* 
String Decode  
*/

const str1 = "a3b2c1d3";
const expected1 = "aaabbcddd";

function decodeStr(str) {}





// Algos 07/13/2021

/*****************************************************************************/

/* 
Given an array of strings
return a sum to represent how many times each array item is found (a frequency table)
Useful methods:
Object.hasOwnProperty("keyName")
    - returns true or false if the object has the key or not
Python: key in dict
*/

const arr1 = ["a", "a", "a"];
const expected1 = {
a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
a: 2,
b: 1,
c: 3,
B: 1,
d: 1,
};

const arr3 = [];
const expected3 = {};


function frequencyTableBuilder(arr) {
charFrequency = {}
  // iterate array
for (var chr of arr){
      // if char not in object, store it in object and value is 1, or else increase its value
    charFrequency[chr] = charFrequency[chr] + 1 || 1
}

return charFrequency
}


console.log(frequencyTableBuilder(arr1))
console.log(frequencyTableBuilder(arr2))
console.log(frequencyTableBuilder(arr3))

//------------- Different solution 

function frequencyTableBuilder(arr) {
var dict = {}
for( var i = 0; i<arr.length; i++){
    if(dict.hasOwnProperty(arr[i])){
        dict[arr[i]]++
    }
    else{
    dict[arr[i]]=1
    console.log(dict)
    }
}
return dict
}

console.log(frequencyTableBuilder(arr2))

/*****************************************************************************/

/* 
Reverse Word Order
Given a string of words (with spaces)
return a new string with words in reverse sequence.
*/

// Single line solution 

const str1 = "This is a test";
const expected1 = "test a is This";

function reverseWordOrder(wordsStr) {
    return wordsStr.split(' ').reverse().join(" ")
}

console.log(reverseWordOrder(str1))

// -------- More efficient solution 

function reverseWordOrder(wordsStr) {
var arr = wordsStr.split(' ')
var arr2 = []
  // for(var i = arr.length-1; i>=0; i--){
for(var i = arr.length; i>=0;  i--){
    arr2.push(arr[i])
}
return arr2.join(" ")
}
console.log(reverseWordOrder(str1))

// ------------- Using two pointers 

const reverseArr = (arr) => {
  // reverse array uisng two pointers, time : O(N/2)
    let left = 0,
        right = arr.length - 1;
    while (left < right){
        [arr[left], arr[right]] = [arr[right], arr[left]]
    }
    return arr
}

// Two line solution with creating a variable 

function reverseWordOrder(wordsStr) {
    wordArr = wordsStr.split(' ')
    return reverseArr(wordArr).join(" ")
}
