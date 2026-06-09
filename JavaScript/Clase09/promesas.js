let miPromesa = new Promise((resolver, rechazar) => {
    let expresion = true;
    if (expresion) {
        resolver("Resolvio correctamente");
    } else {
        rechazar("Se produjo un error");
    }
});

//miPromesa.then(
//    valor => console.log(valor),
//    error => console.log(error)
//);

//miPromesa
//    .then(valor => console.log(valor))
//    .catch(error => console.log(error));

let promesa = new Promise((resolver) => {
    //console.log("Inicio de la promesa");
    setTimeout(() => resolver("Saludos desde promesa, callback, funcion fecha y setTimeout"), 3000);
    //console.log("Fin de la promesa");
});

//El llamado a la promesa
//promesa.then(valor => console.log(valor));

//async indica que una funcion regresa una promesa
async function miFuncionConPromesa() {
    return "Saludos con promesa y async";
}

//miFuncionConPromesa().then(valor => console.log(valor));

//async/await
async function funcionConPromesaYAwait() {
    let miPromesa = new Promise(resolver => {
        resolver("promesa con await");
    });
    console.log(await miPromesa);
}

//funcionConPromesaYAwait();

//Promesas, await, async y setTimeout
async function funcionConPromesaAwaitYSetTimeout() {
    let miPromesa = new Promise(resolver => {
        console.log("Inicio de la funcion")
        setTimeout(() => resolver("Promesa con await y setTimeout"), 3000);
        console.log("Fin de la funcion")
    });
    console.log(await miPromesa);
}

//Llamamos a la función
funcionConPromesaAwaitYSetTimeout();

