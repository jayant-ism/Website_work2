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

const userDiv = (senderId, receiverId, name, online) =>
    (`<a href="/chat/${senderId}/${receiverId}" id="user${receiverId}" class="collection-item row">
                    <img src="https://frontend-1.adjust.com/new-assets/images/site-images/interface/user.svg" class="col s2">
                    <div class="col s10">
                    <span class="title" style="font-weight: bolder">${name}</span>
                    <span style="color: ${online ? 'green' : 'red'}; float: right">${online ? 'online' : 'offline'}</span>
                    </div>
                </a>`)

function scrolltoend() {
    $('#board').stop().animate({
        scrollTop: $('#board')[0].scrollHeight
    }, 800);
}
var time = 0 ; 





function send(formData )
{
    $.ajax({
        url: "api/messages",
        type: 'POST',
        data: formData,
        success: function (data) {
            

            var box = text_box.replace('{sender}', data.sender);
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
                    var box = text_box.replace('{sender}', data[i].sender);
                    box = box.replace('{message}', data[i].message);
                    console.log(parseInt(data[i].sender) ) ;
                    if(parseInt(data[i].sender) != parseInt(sender) )
                    {
                        box = box.replace('right', 'left blue lighten-5');
                    }$('#board').append(box);
                    scrolltoend();
                    if ( time < data[i].id)
                    {
                        time =  data[i].id ;
                    }
                
                } else {


                    var box = image_box.replace('{sender}', data[i].sender);
                    box = box.replace('{message}', data[i].message);
                    box = box.replace('{comment}', data[i].comment)
                    console.log(parseInt(data[i].sender) ) ;
                    if(parseInt(data[i].sender) != parseInt(sender) )
                    {
                        box = box.replace('right', 'left blue lighten-5');
                    }$('#board').append(box);
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

function getUsers(senderId, callback) {
    return $.get('/api/users', function (data) {
        if (userState !== JSON.stringify(data)) {
            userState = JSON.stringify(data);
            const doc = data.reduce((res, user) => {
                if (user.id === senderId) {
                    return res
                } else {
                    return [userDiv(senderId, user.id, user.username, user.online), ...res]
                }
            }, [])
            callback(doc)
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
            

            var box = image_box.replace('{sender}', data.sender);
            box = box.replace('{message}', data.message);
            box = box.replace('{comment}', data.comment)
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


};
