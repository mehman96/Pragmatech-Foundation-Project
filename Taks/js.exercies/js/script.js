let next=document.querySelector('#next')
let prev=document.querySelector('#prev')
let content=document.querySelector('.slide-content')
pos=0;
next.addEventListener('click',function(){
    content.style.transform=`translateX(${pos}px)`
    pos+=1000;
})

prev.addEventListener('click',function(){
    content.style.transform=`translateX(${pos}px)`
    pos-=1000;
})

