

/* 
    Acronyms
    Create a function that, given a string, returns the string’s acronym 
    (first letter of each word capitalized). 
    Do it with .split first if you need to, then try to do it without
*/

const str1 = " there's no free lunch - gotta pay yer way. ";
const expected1 = "TNFL-GPYW";

const str2 = "Live from New York, it's Saturday Night!";
const expected2 = "LFNYISN";

function acronymize(str) {

    // SETUP
	var wordsArr = str.split(" ") // Splits the original string into an array ["there's", "no", "free", "lunch"] etc
	var arr = []  // Create a variable to hold the new list of new letters

    // WORK
	for( var i = 0; i < wordsArr.length; i++){ // Go through the new array  ^^^ [0, 1, 2, 3,]
		var acr = wordsArr[i].split('') // Create a new varible to hold splitting the words
                                        // Split each word into letters, ["t", "h", "e", "r", "e",',"s",] -> [0, 1, 2, 3, 4, 5, 6, 7]
		arr.push(acr[0]) // Push the index of 0 at this new array into our first arr variable 
	}
    // RETURN OR PRINT
	console.log(arr.join('').toUpperCase()) // This will remove the spaces between the varibles and uppercase the letters 
                                            // And making it a string 
} 

acronymize(str1)


/* 
    String: Reverse
    Given a string,
    return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

function reverseString(str) {
    // SETUP
	var reversed = " "

    //WORK
	for( var i = str.length - 1 ; i >= 0; i-- ){ // This will start i at the end of the string value 2, 1, 0 so for dog, g, o, d
		reversed += str[i] // This will add the index value at i to our new variable
	}

    //RETURN
	return reversed; // This returns our new string to our function 
}

reverseString(str1)
reverseString(str2)
console.log(reverseString(str2)) // This will print the return value of the function with the argument sent.