const text_box = '<div class="card-panel right" style="width: 75%; position: relative">' +
    '<div style="position: absolute; top: 0; left:3px; font-weight: bolder" class="title">{sender}</div>' +
    '{message}' +
    '</div>';

const image_box = '<div class="card-panel right" style="width: 75%; position: relative">' +
'<div style="position: absolute; top: 0; left:3px; font-weight: bolder" class="title">{sender}</div>' +
' <a href="{message}" download > <img src="media/file.png" height=50 weidth=25 > <p> {comment} </p></a> '+
'' +
'</div>';



let userState = ''

var sender_details ;
var receive_details ;


function set_user_details(user_id  ) {
    // get the user id for the user 
    
    $.ajax({
        url :"data/" + String(user_id) ,
        type :'GET' ,
        success: function(data) {
            
            sender_details = data[0]  ;

        } 
    })


}


function set_receiver_details(user_id  ) {
    // get the user id for the user 
    
    $.ajax({
        url :"data/" + String(user_id) ,
        type :'GET' ,  
        success: function(data) {
            
            receive_details = data[0]  ;

        } 
    })


}






function scrolltoend() {
    $('#board').stop().animate({
        scrollTop: $('#board')[0].scrollHeight
    }, 800);
}
var time = 0 ; 

function send(formData , sender )
{
    $.ajax({
        url: "api/messages",
        type: 'POST',
        data: formData,
        success: function (data) {
            

            var box = text_box.replace('{sender}', sender_details['first_name']);
            box = box.replace('{message}', data.message);
            console.log(parseInt(data.sender) ) ;

            if(parseInt(data.sender) != parseInt(sender) )
            {
                box = box.replace('right', 'left blue lighten-5');
            }$('#board').append(box);
            scrolltoend();
            if ( time < data.id)
            {
                time =  data.id ;
            }
            document.getElementById("post-form").reset();





        },
        cache: false,
        contentType: false,
        processData: false
    });



}















function receive(sender,connect_id,  trail ) {

    $.get('/api/messages/' + sender + '/' + connect_id+'/' + time + '/'  + trail , function (data) {
        if (data.length !== 0) {
            for (var i = 0; i < data.length; i++) {
                console.log(data[i]);



                if(data[i].message_type == 'text') {
                    var box = text_box ;
                    box = box.replace('{message}', data[i].message);
                    console.log(parseInt(data[i].sender) ) ;
                    if(parseInt(data[i].sender) != parseInt(sender) )
                    {   

                        box = box.replace('{sender}', receive_details['first_name'] );
                        box = box.replace('right', 'left blue lighten-5');
                    }else
                    {
                        
                        box = box.replace('{sender}', sender_details['first_name'] );
                    }


                    $('#board').append(box);
                    scrolltoend();
                    if ( time < data[i].id)
                    {
                        time =  data[i].id ;
                    }
                
                } else {


                    var box = image_box;
                    box = box.replace('{message}', data[i].message);
                    box = box.replace('{comment}', data[i].comment)
                    console.log(parseInt(data[i].sender) ) ;
                    if(parseInt(data[i].sender) != parseInt(sender) )
                    {   

                        box = box.replace('{sender}', receive_details['first_name'] );
                        box = box.replace('right', 'left blue lighten-5');
                    }else
                    {
                        
                        box = box.replace('{sender}', sender_details['first_name'] );
                    }

                    


                    
                    $('#board').append(box);
                    scrolltoend();
                    if ( time < data[i].id)
                    {
                        time =  data[i].id ;
                    }





                }

            }
        }
    })
}



function register(username, password , email , role_id) {
    $.post('/api/users', '{"username": "' + username + '", "password": "' + password + '", "email_id": "' + email + '", "role": "' + role_id + '"}',
        function (data) {
            console.log(data);
            window.location = '/';
        }).fail(function (response) {
            $('#id_username').addClass('invalid');
        })
}

/* for upload */

// AJAX for posting
function create_post( sender   , formData ) {

    $.ajax({
        url: "uploadfilechat",
        type: 'POST',
        data: formData,
        success: function (data) {
            

            var box = image_box ;
            box = box.replace('{message}', data.message);
            box = box.replace('{comment}', data.comment)
            console.log(parseInt(data.sender) ) ;
            if(parseInt(data.sender) != parseInt(sender) )
            {   box = box.replace('{sender}' , receive_details['first_name'] ) ;
                box = box.replace('right', 'left blue lighten-5');
            } else {
                box = box.replace('{sender}' , sender_details['first_name'] ) ;
            }
            
            $('#board').append(box);
            scrolltoend();
            if ( time < data.id)
            {
                time =  data.id ;
            }

            document.getElementById("post-form").reset();





        },
        cache: false,
        contentType: false,
        processData: false
    });


};

