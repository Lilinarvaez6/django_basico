$("[name='tipoA']").change( function(e){
    
        var id = $(this).val();
        var id2 = $("[name='tipoA'] option:selected" ).val();
        alert(id2);
    if(!(id2) == ''){
        $.ajax({
        type:'POST',
        url:'/ajax_armas}',
        data:{
            id_tipos:id,
            id_habilidades:id2,
            action: 'post',
            "csrfmiddlewaretoken" : "{{csrf_token}}"
        },
        success:function(resultado){
            
            var result = resultado['results'];
            var armas = "<option value=''>---------</option>";
            if (!(jQuery.isEmptyObject(result))) {
                 $.each(result, function (ind, elem) { 
                armas += "<option value="+elem.id+">"+elem.nombreA+"</option>";
                });
            }
            
            
            $("[name='nombreA']").html(armas);
           
        },
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); 
    }
    });

    }else{
        var armas = "<option value=''>---------</option>";
        $("[name='nombreA']").html(armas); 
    }
    

    return false;
});
 	 $("[name='habilidadA']").change( function(e){
   	
   		var id = $(this).val();
        
	
	$.ajax({
        type:'POST',
        url:'soldado/ajax_tipo',
        data:{
            id_habilidad:id,
            action: 'post',
            "csrfmiddlewaretoken" : "{{csrf_token}}"
        },
        success:function(resultado){
            
            var result = resultado['results'];
            var tipos = "<option value=''>---------</option>";
            if (!(jQuery.isEmptyObject(result))) {
                 $.each(result, function (ind, elem) { 
                tipos += "<option value="+elem.id+">"+elem.nombreT+"</option>" 
                });
            }
            
            
            $("[name='tipoA']").html(tipos);
             var armas = "<option value=''>---------</option>";
            $("[name='nombreA']").html(armas); 
           
		},
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); 
    }
    });

    return false;
});