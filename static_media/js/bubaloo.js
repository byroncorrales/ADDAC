$(document).ready(function(){
    $('#id_pagina').parent().parent().hide();
    $('#id_url').parent().parent().hide();
    var selecto = $('#id_tipo').val();
    start(selecto);    
    $('#id_tipo').change(function(){
        var opcion = $('#id_tipo').val();
        start(opcion);
    });
});

function start(opcion){
    if(opcion==1){
        $('#id_url').parent().parent().show();
        $("#id_pagina").val($("#id_pagina option:first").val());
        $('#id_pagina').parent().parent().hide();
    }else{
        $('#id_pagina').parent().parent().show();
        $('#id_url').val('');
        $('#id_url').parent().parent().hide();
    }
}