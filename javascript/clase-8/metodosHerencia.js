class Persona{
    //atributos estaticos  
    static contador = 0;
    //atributo no estatico
    noestatico = 10;

    //contador
    static contadorPersonas = 0;

    //como sumular una constante estatica
    static get CONSTANTE(){
        return 3
    }

    constructor(nombre, apellido){
        this._nombre = nombre
        this._apellido = apellido
        //para acceder a un atributo estatico en el constrctor no se ocupa el this  //se utiliza la clase
        Persona.contador++
        console.log("se aumento el contador: " + Persona.contador);

        //contador personas
        //this.IDpersonas = ++Persona.contadorPersonas;

        //comprobaciones de constante estatica
        if (Persona.contador <= 3){
            this.IDpersonas = ++Persona.contadorPersonas
        }else{
            console.log("llegaste al limite de objetos creados");
        }
    }
    //get y set nombre
    get nombre(){
        return this._name
    }
    set nombre(newName){
        return this._nombre = newName
    }
    //get y set apellido
    get apellido(){
        return this._apellido
    }
    set apelldio(newApellido){
        return this._apellido = newApellido
    }
    //metodo nombre complto
    nombreCompleto(){
        return this.IDpersonas + " " +this._nombre + " " + this._apellido
    }
    //devuelve un str
    toString(){
        return this.nombreCompleto()
    }

    //metodo estatic  /puede aser cualquier metodo
    static saludar(){
        console.log("saludos desde el metodo estatikco");
    }
}

//herencia  /para eredar todo de una clase padre se debe de usar extends
class Obrero extends Persona{
    constructor (departamento, nombre, apellido){
        //el super smpre se le debe de agregar con los parametro de la clase padrre, para invocar todo de la clase padre
        super(nombre, apellido)
        this._departamento = departamento
    }
    get departamento(){
        return this._departamento
    }
    set departamento(newDepartamento){
        return this._departamento = newDepartamento
    }

    //metodo sobre escritura  /se re escribe de una forma identica un metodo de la clase padre y se le agrega en la clase hija nuevas cosas
    nombreCompleto(){
        return super.nombreCompleto() + " " + this._departamento
    }
}

//creacion de un objeto
const laburante = new Obrero("piso 1", "zelada", "Gira")
console.log(laburante);


//como imprimir los metodos estaticos 
//console.log(laburante.saludar()); de esta manera no
Persona.saludar();


//como imprimir atrbutos estaticos  //se imprime por medio de la clase no de los objetos y las clases hijas
console.log(Persona.contador);
console.log(Obrero.contador);
//undefine por acceder por medio delo objeto
console.log(laburante.contador);

//la diferencia entre atributos estaticos y no estaticos  // los atributos estaticos son acesible atravez de las clases
console.log(Persona.contador);
console.log(laburante.contador);
//los no estaticos son acsibles atravez de un objeto creado
console.log(Persona.noestatico);
console.log(laburante.noestatico);

//imprimir contador de persona usando static
console.log(laburante.toString());

const persona2 = new Obrero("Matias", "Arturo", "piso 4")
//al crear un nuevo objeto el contador aumenta en 2
console.log(persona2.toString());


//comprobaciones  
const persona3 = new Persona("orlando", "zelada");
//en consola se imprimira la comnprobacion del simulador constante estatica
const persona4 = new Persona("Ian", "alexander")