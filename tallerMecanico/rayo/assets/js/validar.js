function login(){
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;


    console.log("Mensaje desde la consola: ");console.log("email: "+email+", Password: "+password);

    if(usuario == ''){
        alert("El email no puede ir vacío");
    } else {
        document.getElementById("enviar").submit();
    }
}

function registro(){
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    
    console.log("Mensaje desde la consola: ");console.log("email"+email+", Password: "+password);

    if(usuario == ''){
        alert("El email no puede ir vacío");
    } else {
        document.getElementById("enviar").submit();
    }    
}


function recuperar(){
    var email = document.getElementById("email").value;
    
    console.log("Mensaje desde la consola: ");console.log("email");

    if(usuario == ''){
        alert("El email no puede ir vacío");
    } else {
        document.getElementById("enviar").submit();
    }     
}