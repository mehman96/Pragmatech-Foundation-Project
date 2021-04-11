// nb-contanier section start
var i = 0
var txt = 'Programmer' 
var txt ='Photographer'
var txt ='Designer'
var speed = 50

function typeWriter (){
    if (i<txt.length){
        document.getElementById("animation-text").innerHTML+=txt.charAt(i)
        i++
        setInterval(typeWriter, speed)
    }

}









// nb-contanier section end



// my_services section start
// var slider = document.querySelector('.box-contanier')
// console.log(box-contanier)





// my services section end
