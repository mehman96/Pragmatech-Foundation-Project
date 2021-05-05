// nb-continer start

const TypeWriter = function (txtELement, words, wait =3000){
this.txtELement=txtELement;
this.words =words;
this.txt = ''
this.wordIndex=0
this.wait = parseInt (wait, 10)
this.type();
this.isdeleting = false;
}

