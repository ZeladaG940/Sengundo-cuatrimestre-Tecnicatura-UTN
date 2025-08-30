//como crear un arry
let arr = new Array();
console.log(arr);

//otra forma
let array = ["perros", "gatos", "uwu"];
console.log(array);

//como recorrer elemtos de un arreglo
for(let i=0; i<=array.length - 1; i++){
    console.log(array[i]);
}

//otra forma
console.log(array[1]);
console.log(array[2]);
console.log(array[3]);

//como agregar elemtos a un array
array.push("owo")
console.log(array);

//otra forma
array[array.length] = "UWU";
console.log(array);

//otra forma
array[5] = ":b";

//como saber si es un array
console.log(Array.isArray(array));

//otra forma
console.log(array instanceof Array);