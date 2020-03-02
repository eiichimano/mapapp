function startGmap() {
	var ns = google.maps,
		myLatlng = new ns.LatLng(35.687168, 139.757412),
		mapElement = document.getElementById("mapDiv"),
		mapOptions = {
			zoom: 12,
			center: myLatlng
		},
		map = new ns.Map(mapElement, mapOptions),
		// ========== 以下、ジオコーディング ==========
		geocoder = new ns.Geocoder(),
		request = {
    		address: "{{ shop.address }}"
			// 日本橋高島屋
			// address: "東京都中央区日本橋2丁目4番1号"
		};

	geocoder.geocode(request, function (result, status) {
		var latlng, marker;

		if (status !== ns.GeocoderStatus.OK) {
			alert(status);//検索失敗
			return;
		}
		latlng = result[0].geometry.location;
		marker = new ns.Marker({
			position: latlng,
			map: map
		});
	});

}
google.maps.event.addDomListener(window, 'load', startGmap);