function displayData(bundle){
	$("#news").html(bundle[0].long_name + bundle[1].long_name + bundle[2].long_name +bundle[3].long_name);
	$("#news").css({'display':'block'})
};

$("#kill").click(function(){
	$("#news").css({'display':'none'})
});





function initMap() {
    var myLatlng = {lat: -25.363, lng: 131.044};

    var map = new google.maps.Map(document.getElementById('map'), {
		zoom: 4,
		center: myLatlng
    });
    var geocoder = new google.maps.Geocoder;	

    map.addListener('click', function(event) {
		var input_latlng = event.latLng.lat() + ',' + event.latLng.lng()
		geocodeLatLng(geocoder,map,input_latlng)
	});

    function geocodeLatLng(geocoder, map,coords) {
    var input = coords;
    var latlngStr = input.split(',', 2);
    var latlng = {lat: parseFloat(latlngStr[0]), lng: parseFloat(latlngStr[1])};
	console.log(latlng)
    geocoder.geocode({'location': latlng}, function(results, status) {
      if (status === 'OK') {
        if (results[0]) {
			var address = results[0].address_components;
			var address_json = {};
			address_json['data'] = address
			console.log(results)
	   		$.ajax({
 					type: 'POST',
	                contentType: 'application/json',
	                data: JSON.stringify(address_json),
	                dataType: 'json',
	                url: 'http://localhost:5000/function_route',
	                success: function (e) {
	                    console.log(e.data);
	                    displayData(e.data);
	                },
	                error: function(error) {
	                console.log(error);
	            }
	        });

        } else {
          window.alert('No results found');
        }
      } else {
        window.alert('Geocoder failed due to: ' + status);
      }
    });
	}
};



	
