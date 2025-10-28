//La clase de hoy ser trata de crear una función en el lenguaje de JavaScript, esta función nos tiene que solucionar el
// ingreso de una contraseña del usuario, la cuál debe ser correcta:
// Ejercicio 1: Función que valide una contraseña (mínimo 8 caracteres, 1 número, 1 mayúscula)

function validatePassword(password) {
    // pasa todo a minúsculas
    let minusculas = password.toLowerCase();

    // verifica si tiene mayúscula
    let tieneMayuscula = password !== minusculas;

    // verifica si tiene al menos 8 caracteres
    let tieneLongitud = password.length >= 8;

    // verifica si tiene al menos un número
    let tieneNumero = false;
    let numeros = ["0","1","2","3","4","5","6","7","8","9"];

    for (let i = 0; i < password.length; i++) {
        for (let j = 0; j < numeros.length; j++) {
            if (password[i] === numeros[j]) {
                tieneNumero = true;
            }
        }
    }

    // verifica si cumple todos los requisitos
    if (tieneMayuscula && tieneLongitud && tieneNumero) {
        return "la contraseña cumple con los requisitos";
    } else {
        return "la contraseña no cumple con los requisitos";
    }
}

// Pruebas
console.log(validatePassword("Abc12345")); 
console.log(validatePassword("weak"));     
