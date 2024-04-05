function animacion() {
    let textoAnimado = [
        ["d","e","l","i","c","i","o","s","a","s"],
        ["c","r","e","a","t","i","v","a","s"],
        ["s","a","b","r","o","s","a","s"],
        ["i","n","n","o","v","a","d","o","r","a","s"],
        ["e","x","q","u","i","s","i","t","a","s"],
        ["s","o","r","p","r","e","n","d","e","n","t","e","s"],
        ["i","r","r","e","s","i","s","t","i","b","l","e","s"],
        ["f","r","e","s","c","a","s"],
        ["s","a","l","u","d","a","b","l","e","s"],
        ["f","á","c","i","l","e","s"],
        ["r","á","p","i","d","a","s"],
        ["a","t","e","m","p","o","r","a","l","e","s"],
        ["g","o","u","r","m","e","t"],
        ["e","c","o","n","ó","m","i","c","a","s"],
        ["o","r","g","á","n","i","c","a","s"],
        ["v","e","r","s","á","t","i","l","e","s"],
        ["i","n","s","p","i","r","a","d","o","r","a","s"],
        ["a","u","t","é","n","t","i","c","a","s"]
    ];
    

    let letraContador = -1;
    let nivelArray = 0;

    const contenedorAnimacion = document.querySelector(".header__title");

    function animarTexto() {
        letraContador++;
        
        let filler = "Descubre recetas " + textoAnimado[nivelArray].slice(0, letraContador + 1).join("");
        contenedorAnimacion.textContent = filler;

        if (letraContador === textoAnimado[nivelArray].length - 1) {
            clearInterval(intervalo);

            setTimeout(() => {
                intervalo = setInterval(() => {
                    contenedorAnimacion.textContent = "";
                    letraContador--;
                    textoAnimado[nivelArray].pop();

                    let filler = "Descubre recetas " + textoAnimado[nivelArray].slice(0, letraContador + 1).join("");
                    contenedorAnimacion.textContent = filler;

                    if (letraContador < 0) {
                        clearInterval(intervalo);
                        nivelArray++;
                        intervalo = setInterval(animarTexto, 150);

                        if (nivelArray > textoAnimado.length - 1) {
                            clearInterval(intervalo);
                            nivelArray = 0;
                            animacion();
                        }
                    }
                }, 150);
            }, 1000);
        }
    }

    let intervalo = setInterval(animarTexto, 150);
}

window.addEventListener("load", animacion);

/*faqs*/

const faqs = document.querySelectorAll(".faq");

faqs.forEach(faq => {
    faq.addEventListener("click", () => {
        if(faq.classList.contains("active")){
            faq.classList.remove("active")
        }else{
            faq.classList.add("active")
            faqs.forEach((otherFaq)=>{
                if(otherFaq !== faq){
                    otherFaq.classList.remove("active")
                }
            })
        }
    })
})