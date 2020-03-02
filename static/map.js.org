function startGmap() {
	var myLatlng = new google.maps.LatLng(35.687168, 139.757412),// 皇居
		mapElement = document.getElementById("mapDiv"),
		mapOptions = {
			zoom: 14,
			center: myLatlng
		},
		map = new google.maps.Map(mapElement, mapOptions);
}
google.maps.event.addDomListener(window, 'load', startGmap);