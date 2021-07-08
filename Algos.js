

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
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the underlined ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing

function parensValid(str) {
    var count = 0;
    for( var i = 0; i < str.length; i++){
        if(str[i] == "("){
            count++;
        }
        else if (str[i] == ")"){
            count--;
        }
        if(count < 0){
            return false;
        }
    if( count == 0){
        return true;
    }
    else{
        return false;
    }
        
    }
}

var newString = parensValid(str2)
console.log(newString);


/*****************************************************************************/

// /* 
// Braces Valid
// Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
// */

// const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
// const expected1 = true;

// const str2 = "D(i{a}l[ t]o)n{e";
// const expected2 = false;

// const str3 = "A(1)s[O (n]0{t) 0}k";
// const expected3 = false;

// function bracesValid(str) {
//     var count = 0;
//     var squareCount = 0;
//     var curlyCount = 0;
//     for( var i = 0; i < str.length; i++){
//         if(str[i] == "("){
//             count++;
//         }
//         else if (str[i] == ")"){
//             count--;
//         }
        
//         if (str[i] == "{"){
//             curlyCount++;
//         }
//         else if(str[i] == "}"){
//             curlyCount--;
//         }
//         if (str[i] == "["){
//             squareCount++;
//         }
//         else if(str[i] == "]"){
//             squareCount--;
//         }
//         if( count < 0){
//             return false
//         }
//         else if ( curlyCount < 0){
//             return false;
//         }
//         else if( squareCount < 0){
//             return false;
//         }
//         if( count == 0 && squareCount == 0 && curlyCount == 0){
//             return true;
//         }
//         else{
//             return false;
            
//         }
        
//     }
// }

// var test = bracesValid(str1)
// console.log(test)

// var test2 = bracesValid(str2)
// console.log(test2)