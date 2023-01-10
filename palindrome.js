/**
 * @param {number} x
 * @return {boolean}
 */
 var isPalindrome = function(x) {
    var number_revert = new Array();
    var x= x.toString();
    var tam = x.length - 1;
    for(var i =0; i < x.length; i++){
        number_revert[tam-i] = x[i];
    }
    number_revert = number_revert.toString().replaceAll(',', '');
    return number_revert == x;
};