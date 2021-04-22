// niedzialajaca nawiga z https://embed.plnkr.co/plunk/PBHp2Yli0BrfUm9h
(function($) {
  var routes = {},
    defaultRoute = 'pages';

  routes['pages'] = {
    url: '/',
    templateUrl: 'public/templates/index.html',
  };

  routes['page2'] = {
    url: 'page2',
    templateUrl: 'public/templates/page2.html',
  };

  $.router.setData(routes).setDefault(defaultRoute);

  $.when($.ready).then(function() {
    $.router.run('.my-view', 'pages');
  });

})(jQuery);

// $(document).ready(()=>{
//     confirm('Potwierdzam wystarczające upojenie alkoholem, aby rozpocząć ten projekt');

//     $('button').click(()=>{
//         $.ajax({
//             url: ":api/getData",
//             success: (result)=>{
//                 $('#json').text(result.data);     
//             },
//             error: (result)=>{
//                 console.log(result); 
//             }
//           });
//     })
// })
