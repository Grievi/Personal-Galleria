$(document).ready(function(){
    $("#btn-copy").click(function(e){
        var copied = e.target
        navigator.clipboard.writeText(copied.value)
        var copiedModal=new bootstrap.Modal(document.getElementById('copied-url'))
        copiedModal.show()
    })

})