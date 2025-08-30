//palabra reservada breack
for (let i=0; i<=3; i++){
    console.log(i);
    if(i == 2){
        console.log("el seclo llego a 2");
        break;
    }
}

//palabra reservada continue
for (let i=0; i<=3; i++){
    console.log(i);
    if(i==2){
        console.log("el ciclo llego a 2");
        continue;
    }
}

//labels
inicio:
for (let i=0; i<=3; i++){
    console.log(i);
    if (i==2){
        break inicio;
    }
}