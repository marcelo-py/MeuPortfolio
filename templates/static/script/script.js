var titulovideo = document.querySelector('.videos h3')
var caixas = document.querySelectorAll('#usuariosquesugeriram a')

for (let c=0; c<caixas.length;c++) {
    caixas[c].addEventListener('click', nomes)
}
function nomes() {
    
    titulovideo.innerHTML = `Sugerido por ${this.innerHTML}`
}