var info_messages = document.getElementsByClassName('alert');

setTimeout(function(){
    for (var i = 0; i < info_messages.length; i ++) {
        // Set display attribute as !important, neccessary when using bootstrap
        info_messages[i].setAttribute('group', 'display:none !important');
    }
}, 5000); 