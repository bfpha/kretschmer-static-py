
`
replacing arche id with pid

`

var arche = document.getElementById("file1_get")
.getAttribute("href");
var archeMD = `${arche}?format=metadata`;
var query = ARCHEapi.ARCHErdfQuery;

fetch(archeMD)
  .then(response => response.text())
  .then(data => {
    // console.log(data);
    var identifier = query({
        "subject": null,
        "predicate": "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
        "object": "https://vocabs.acdh.oeaw.ac.at/schema#Resource",
        "expiry": null
    }, data);
    var values = identifier.value;
    var handles = [];
    values.forEach(function(rs) {
        var res = query({
            "subject": rs.type.subject,
            "predicate": "https://vocabs.acdh.oeaw.ac.at/schema#hasPid",
            "object": null,
            "expiry": null
        }, data);
        
        var handle = res.value[0].hasPid.object.replace("^^http://www.w3.org/2001/XMLSchema#anyURI","");
        handles.push(handle);
        // console.log(res.value[0].hasPid.object.replace("^^http://www.w3.org/2001/XMLSchema#anyURI",""));
        
    });
    if ( handles.length == 2 ) {
        var file1 = $(".file1");
        file1.each(function() {
            $(this).html(handles[0]);
            $(this).attr("href", handles[0]);
        });
        var file2 = $(".file2");
        file2.each(function() {
            $(this).html(handles[1]);
            $(this).attr("href", handles[1]);
        });
    }
    if ( handles.length == 3 ) {
        var file1 = $(".file1");
        file1.each(function() {
            $(this).html(handles[0]);
            $(this).attr("href", handles[0]);
        });
        var file2 = $(".file2");
        file2.each(function() {
            $(this).html(handles[1]);
            $(this).attr("href", handles[1]);
        });
        var journalfile1 = $(".journalfile1");
        journalfile1.each(function() {
            $(this).html(handles[2]);
            $(this).attr("href", handles[2]);
        });
    } 
    if ( handles.length == 4 ) {
        var file1 = $(".file1");
        file1.each(function() {
            $(this).html(handles[0]);
            $(this).attr("href", handles[0]);
        });
        var file2 = $(".file2");
        file2.each(function() {
            $(this).html(handles[0]);
            $(this).attr("href", handles[1]);
        });
        var journalfile1 = $(".journalfile1");
        journalfile1.each(function() {
            $(this).html(handles[2]);
            $(this).attr("href", handles[2]);
        });
        var journalfile2 = $(".journalfile2");
        journalfile2.each(function() {
            $(this).html(handles[3]);
            $(this).attr("href", handles[3]);
        });
    }
});

// var download = ARCHEapi.ARCHEdownloadResourceIdM2;
// var query = ARCHEapi.ARCHErdfQuery;
// setTimeout(function(){
//     download({
//         "host": "https://id.acdh.oeaw.ac.at",
//         "resourceID": arche,
//         "format": "metadata",
//         "readMode": "resource"
//     }).then((data) => {
//         console.log(data);
//     });
// },1000);