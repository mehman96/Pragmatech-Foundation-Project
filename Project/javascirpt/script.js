
function icon(elem) {
document.body.removeChild(elem.parentElement)
}
function showimgbig(elem){
    console.log(elem)
let overline_=`
  
div class="overline_ ">
    <div class="image_" onclick="icon (this)" >
      <img src="/Project/img/pf(1).jpg" alt="">
      <div class="close " >
        <i class="fas fa-times-circle"></i>
      </div>
  </div>  
  
`
document.body.innerHTML+overline_

}