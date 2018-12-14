var sortArrayByParity = function(A) {
    E = [];
    O = [];

    for (i = 0; i < A.length; i++){
        if (A[i] % 2 == 0){
            E.push(A[i]);
        }
         else {
            O.push(A[i]);
        }
    }
    return E.concat(O);
};
var res = sortArrayByParity([1,2,3,4]);
console.log(res);
