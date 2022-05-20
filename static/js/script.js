$(document).ready(function() {

    $("#create-breed_group").modalForm({
        formURL: "{% url 'add_review' %}"
    });

}); 