let contador;   
function calificar(item) {
  contador = item.id[0]
  let nombre = item.id.substring(1);
  for (let i = 0; i < 5; i++) {
    if (i < contador) {
      document.getElementById((i + 1) + nombre).style.color = "orange";
    } else {
      document.getElementById((i + 1) + nombre).style.color = "black";
    }
  }
}

const confirm = document.getElementById("confirmar")
const nameUser = document.getElementById("nombre")
const review = document.getElementById("resena")
const reviewModal = document.getElementById("resena-modal")
const nameModal = document.getElementById("staticBackdropLabel")
const stars = document.getElementById("calificacion")
confirm.addEventListener("click", ()=>
{
  nameModal.innerText = nameUser.value + " quiere confirmar su reseña?"
  reviewModal.innerText = review.value
  stars.innerText = "Usted calificó con " + contador + " estrellas!"
  document.getElementsByName("nombre")[0].value = nameUser.value
  document.getElementsByName("calificacion")[0].value = review.value
  document.getElementsByName("estrella")[0].value = contador
})

setInterval(()=>
{
  let count = 0
  if(nameUser.value.length > 2){count++}
  if(review.value.length > 10){count++}
  if(contador > 0){count++}
  if(count == 3){confirm.disabled = false}else{confirm.disabled = true}
}, 200)
