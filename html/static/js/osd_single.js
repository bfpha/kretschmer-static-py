function load_image(el) {
    var $this = $(el);
    var image_id = $this.attr("id");
    console.log(image_id);
    console.log(el);
    if ( $this.children("div[class='openseadragon-container']").length == 0 ) {
        // console.log(osd_container_id);
        $this.css({
            'height': '600px'
        });
        // OpenSeaDragon Image Viewer
        var image = $this.attr("data-target");
        // var imageURL = {type: 'image', url: image};
        var viewer = OpenSeadragon({
            id: image_id,
            prefixUrl: 'https://cdnjs.cloudflare.com/ajax/libs/openseadragon/2.4.1/images/',
            // sequenceMode: true,
            // showReferenceStrip: true,
            // showNavigator: true,
            // imageLoaderLimit: 10,
            tileSources: image
        });

        // hide loading spinner if image fully loaded status changes
        // see issue: https://github.com/openseadragon/openseadragon/issues/1262

        viewer.addHandler('open', function() {
            var tiledImage = viewer.world.getItemAt(0);
            if (tiledImage.getFullyLoaded()) {
                hideLoading();
            } else {
                tiledImage.addOnceHandler('fully-loaded-change', hideLoading);
            }
        });
    }

    function hideLoading() {
        // var container = $(osd_container_id).attr("id");  
        var spinnerID = `spinner_${ image_id }`;
        if ( $("#" + spinnerID ) ) {
            // console.log(spinnerID);
            $("#" + spinnerID ).remove();
        }
    }
}
