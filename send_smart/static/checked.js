; (function () {
    const checkboxes= document.getElementsByName('check[]');
    let listaCheck=[]

    for (let i=0; i<checkboxes.length; i++){
        checkboxes[i].addEventListener("click", function (){
            if (checkboxes[i].checked){
                listaCheck.push(checkboxes[i].value)
                console.log(listaCheck)           
                
            }
        });

    }
    console.log(listaCheck)

})()