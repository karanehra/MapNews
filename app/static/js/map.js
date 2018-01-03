function displayData(address,news){
	console.log(address.length)
	$("#click_popup_right").css("display","block")
	for (var i = 0; i < address.length; i++) {
		$("#add"+String(i)).empty();
		$("#add"+String(i)).html(String(address[i]["long_name"])+" "); 
	}
	$("#news").empty()
	if (news.length == 0) {
		$("#news").html("no news")
	}
	else{
		for (var j = 0; j < news.length; j++) {
			$("#news").append('<div class="newsitem"> \
				<div class="heading"><a href="'+news[j].link+'">'+news[j].heading+'</a> </div>\
				<div class="description">'+news[j].description+'</div></div>')
		}
	}
};

function initMap() {
    var myLatlng = {lat: 25.363, lng: 100.044};

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
    geocoder.geocode({'location': latlng}, function(results, status) {
      if (status === 'OK') {
        if (results[0]) {
			var address = results[1].address_components;
			for(i = 0; i < address.length; i++){
				str = String(address[i])
				if(str.match(".*\\d.*")){
				   var pop = i
				} 
			}
			var address_json = {};
			address_json['data'] = address
	   		$.ajax({
 					type: 'POST',
	                contentType: 'application/json',
	                data: JSON.stringify(address_json),
	                dataType: 'json',
	                url: 'http://localhost:5000/function_route',
	                success: function (news) {
	                    displayData(address,news);
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



	

