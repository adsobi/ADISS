$(document).ready(()=>{
    confirm('Potwierdzam wystarczające upojenie alkoholem, aby rozpocząć ten projekt');

    $('button').click(()=>{
        $.ajax({
            url: ":api/getData",
            success: (result)=>{
                $('#json').text(result.data);     
            },
            error: (result)=>{
                console.log(result); 
            }
          });
    })
})