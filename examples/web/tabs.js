function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

function displayImages(){

	$.ajax({
    	url : "http://localhost:5000/picture",
    	success: function (data) {
        console.log(data)   ;
        //$('#Known').append("<div class='polaroid-images'>");
            for (var i in data) {
                //make a jquery to display image

                //$('#Known').append("<div class='imageBox'>");
                var name = data[i].slice(66, -4);
                $('#known-faces').append("<a href='' title='"+name+"'>" + "<img height='200' alt='" + name + "' title='" + name + "' src='" + data[i] + "'/></a>");

            }
        //$('#Known').append("</div>");
        }
	}); 

}

function displayImagesUnknown(){

    $.ajax({
        url : "http://localhost:5000/unknown",
        success: function (data) {
        console.log(data)   ;
        //$('#Known').append("<div class='polaroid-images'>");
            for (var i in data) {
                //make a jquery to display image

                //$('#Known').append("<div class='imageBox'>");
                var name = data[i].slice(68, -4);
                $('#unknown-images').append("<a href='' title='"+name+"'>" + "<img id=" +name+ " height='200' alt='" + name + "' title='" + name + "' src='" + data[i] + "'/></a>");

            }
        //$('#Known').append("</div>");
        //<div class='nameFunction' title:'"+name+"' onclick='namePerson("+name+")''>
        }
    }); 

}

function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#chosen')
                    .attr('src', e.target.result)
                    $('.nameform').append("<img id='chosen' src=" + e.target.result+ " alt='your image' />");

            };

            reader.readAsDataURL(input.files[0]);

        }
    }

function submitFaces() {
    var fileData = $('.nameBox').prop('files')[0];
    var nameData = $('.name').val();


    var reader = new FileReader();
    reader.readAsDataURL(fileData);


    // new array with reader.result and name
    //send array to ajax

    reader.onload = function(e) {

        var personInfo = {results: reader.result, name: nameData};
        console.log(personInfo);
        var dataURL = reader.result;
        $.ajax({
            url : "http://localhost:5000/savePicture",
            method : "POST",
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            data: JSON.stringify(personInfo),
            success: function (data) {
                displayImages(); 

            }
        }); 
    }

}

$('#unknown-images').on('click', '[data-editable]', function(){
  
  var $el = $(this);
              
  var $input = $('<input/>').val( $el.text() );
  $el.replaceWith( $input );
  
  var save = function(){
    var $p = $('<p data-editable />').text( $input.val() );
    $input.replaceWith( $p );
  };
  
  /**
    We're defining the callback with `one`, because we know that
    the element will be gone just after that, and we don't want 
    any callbacks leftovers take memory. 
    Next time `p` turns into `input` this single callback 
    will be applied again.
  */
  $input.one('blur', save).focus();
  
});

/*
function namePerson(name) {
    $('.polaroid-images')
        .attr('title')


}
*/



