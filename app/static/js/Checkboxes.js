     // Begin: Set checkboxes
     //var comp_type_data = [{"name":"Platform","sub":"PF"},{"name":"Academia","sub":"AC"},{"name":"Data Mining","sub":"DM"},{"name":"Computer Vision","sub":"CV"},{"name":"Natural Language Processing","sub":"NLP"},{"name":"Reinforcement Learning/Robotics","sub":"RL"},{"name":"Speech/Signal Proccessing","sub":"SP"}];
     var comp_type_data = [{
         "name": "Data Mining",
         "sub": "DM"
     }, {
         "name": "Computer Vision",
         "sub": "CV"
     }, {
         "name": "Natural Language Processing",
         "sub": "NLP"
     }, {
         "name": "Reinforcement Learning/Robotics",
         "sub": "RL"
     }, {
         "name": "Speech/Signal Proccessing",
         "sub": "SP"
     }];
     var all_subs = [];
     //var type1_subs = [];
     var type2_subs = [];

     //for (var i = 0; i < comp_type_data.length; i++) {
     //  all_subs[i] = comp_type_data[i]['sub'];
     //  if (i <= 1) {
     //    type1_subs[i] = comp_type_data[i]['sub'];
     //  }
     //  else {
     //    type2_subs[i] = comp_type_data[i]['sub'];
     //  }
     // }
     for (var i = 0; i < comp_type_data.length; i++) {
         all_subs[i] = comp_type_data[i]['sub'];
         type2_subs[i] = comp_type_data[i]['sub'];
     }

     //subs = all_subs;
     // Get subjects from URL
     window.history.pushState('', '', '/?sub=' + all_subs.join());
     var url = new URL(window.location);
     var subs = url.searchParams.get('sub');

     if (subs == undefined) {
         subs = store.get('/');
     } else {
         subs = subs.toUpperCase().split(',');
     }
     // Get subjects from browser cache
     //console.log(subs);

     if (subs == undefined) {
         subs = all_subs;
         for (var i = 0; i < subs.length; i++) {
             $('#' + subs[i] + '-checkbox').prop('checked', true);
         }
     } else {
         for (var i = 0; i < subs.length; i++) {
             $('#' + subs[i] + '-checkbox').prop('checked', true);
         }
     }
     // Hide unchecked subs
     for (var i = 0; i < all_subs.length; i++) {
         if (subs.indexOf(all_subs[i]) < 0) {
             $('.' + all_subs[i] + '-comp').hide();
         }
     }
     store.set('/', subs);
     window.history.pushState('', '', '/?sub=' + subs.join());

     // Event handler on checkbox change
     $('form :checkbox').change(function (e) {

         var checked = $(this).is(':checked');
         var cid = $(this).prop('id');
         var csub = cid.substring(0, cid.length - 9);
         if (checked == true) {
             // $('.' + csub + '-comp').show();
             if (subs.indexOf(csub) < 0)
                 subs.push(csub);
         } else {
             // $('.' + csub + '-comp').hide();
             var idx = subs.indexOf(csub);
             if (idx >= 0)
                 subs.splice(idx, 1);
         }
         // First, hide all
         for (var i = 0; i < all_subs.length; i++) {
             $('.' + all_subs[i] + '-comp').hide();
         }
         // Then, show the one with checked subs within PF/AC
         //for (var i = 0; i < type2_subs.length; i++) {
         //  if (subs.indexOf(type2_subs[i]) >= 0) {
         //    $('.' + type2_subs[i] + '-host').show();
         //  }
         //}
         for (var j = 0; j < type2_subs.length; j++) {
             if (subs.indexOf(type2_subs[j]) >= 0) {
                 $('.' + type2_subs[j] + '-comp').show();
             }
             if (subs.indexOf('rewarded') >= 0) {
                 $('.unrewarded-comp').hide();
             }
         }

         console.log(subs);
         store.set('/', subs);
         window.history.pushState('', '', '/?sub=' + subs.join());
     });

     // End: set checkbox