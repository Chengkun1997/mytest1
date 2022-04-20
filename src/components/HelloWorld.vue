<template>
  <div id="map_container"></div>
</template>

<script>
// import mapboxgl from 'mapbox-gl'  //方式一
export default {
  name: "HelloWorld",
  mounted() {
    var mapboxgl = require("mapbox-gl/dist/mapbox-gl.js");  //方式二
    mapboxgl.accessToken =
      "pk.eyJ1IjoibWFyaW9jayIsImEiOiJja3B4aW50Y3owMHR5MnZ0OGU1cHMzemZyIn0._ddOLRXUamGoEEMvW84QqQ";

    // var map = new mapboxgl.Map({
    //   container: "map_container",
    //   style: "mapbox://styles/mariock/ckpxn4as114ok17mfvvvlj2x6",
    // });
    //

    var map = new mapboxgl.Map({
      style: "mapbox://styles/mapbox/light-v10",
      center: [-74.0066, 40.7135],
      zoom: 15.5,
      pitch: 45,
      bearing: -17.6,
      container: "map_container",
      antialias: true,
    });

    map.on("load", function () {
      // Insert the layer beneath any symbol layer.
      var layers = map.getStyle().layers;
      var labelLayerId;
      for (var i = 0; i < layers.length; i++) {
        if (layers[i].type === "symbol" && layers[i].layout["text-field"]) {
          labelLayerId = layers[i].id;
          break;
        }
      }

      // The 'building' layer in the Mapbox Streets
      // vector tileset contains building height data
      // from OpenStreetMap.
      map.addLayer(
        {
          id: "add-3d-buildings",
          source: "composite",
          "source-layer": "building",
          filter: ["==", "extrude", "true"],
          type: "fill-extrusion",
          minzoom: 15,
          paint: {
            "fill-extrusion-color": "#aaa",

            // Use an 'interpolate' expression to
            // add a smooth transition effect to
            // the buildings as the user zooms in.
            "fill-extrusion-height": [
              "interpolate",
              ["linear"],
              ["zoom"],
              15,
              0,
              15.05,
              ["get", "height"],
            ],
            "fill-extrusion-base": [
              "interpolate",
              ["linear"],
              ["zoom"],
              15,
              0,
              15.05,
              ["get", "min_height"],
            ],
            "fill-extrusion-opacity": 0.6,
          },
        },
        labelLayerId
      );
    });
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#map_container {
  width: 100%;
  height: 100%;
}
/* deep::mapboxgl-control-container {
  display: none;
} */
::v-deep .mapboxgl-control-container {
  display: none;
  /* visibility:hidden; */
}
/* #map_container >>> mapboxgl-control-container{
  visibility:hidden;
} */
</style>
