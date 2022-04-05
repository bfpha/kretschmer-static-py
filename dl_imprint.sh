# bin/bash

REDMINE_ID=20278
IMPRINT_XML=./templates/imprint.html
rm ${IMPRINT_XML}
echo '<html lang="en">'  >> ${IMPRINT_XML}
echo '<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.84.0">
    <title> Imprint </title>
    <link rel="canonical" href="https://getbootstrap.com/docs/5.0/examples/album/">
    <link href="assets/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="static/style.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script> 
  </head>
  <body>
    <header>
      <div class="collapse bg-dark" id="navbarHeader">
        <div class="container">
          <div class="row">
            <div class="col-sm-8 col-md-7 py-4">
              <h4 class="text-white">About</h4>
              <p class="text-muted">Add some information about the album below, the author, or any other background context. Make it a few sentences long so folks can pick up some informative tidbits. Then, link them off to some social networking sites or contact information.</p>
            </div>
            <div class="col-sm-4 offset-md-1 py-4">
              <h4 class="text-white">Contact</h4>
              <ul class="list-unstyled">
                <li><a href="#" class="text-white">Email me</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="navbar navbar-dark bg-dark shadow-sm">
        <div class="container">
          <a href="index.html" class="navbar-brand d-flex align-items-center">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="me-2" viewBox="0 0 24 24"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>
            <strong>Paul Kretschmer Reise nach Griechenland/Lesbos</strong>
            <span style="margin-left: 1.7em;" class="badge bg-light text-dark">in development</span>
          </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHeader" aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
        </div>
      </div>
    </header>'  >> ${IMPRINT_XML}
echo "<body><div class='container'><div class='card' style='margin-top:2em;'><div class='card-body'>" >> ${IMPRINT_XML}
curl https://shared.acdh.oeaw.ac.at/acdh-common-assets/api/imprint.php?serviceID=${REDMINE_ID} >> ${IMPRINT_XML}
echo "</div></div></div>" >> ${IMPRINT_XML}
echo '<div class="wrapper bg-dark" style="color:lightgrey;">
      <div class="container" style="padding:2em;" tabindex="-1">
          <div class="row">
              <div class="footer-widget col-lg-1 col-md-2 col-sm-2 col-xs-6  ml-auto text-center ">
                  <div class="textwidget custom-html-widget">
                      <a href="https://www.oeaw.ac.at/acdh"><img src="https://fundament.acdh.oeaw.ac.at/common-assets/images/acdh_logo.svg" class="image" alt="ACDH Logo" style="max-width: 100%; height: auto;" title="ACDH Logo"/></a>
                  </div>
              </div>
              <!-- .footer-widget -->
              <div class="footer-widget col-lg-4 col-md-3 col-sm-3">
                  <div class="textwidget custom-html-widget">
                      <p>
                          ACDH-CH OEAW
                          <br/>
                          Austrian Centre for Digital Humanities and Cultural Heritage
                          <br/>
                          Austrian Academy of Sciences
                      </p>
                      <p>
                          Sonnenfelsgasse 19
                          <br/>
                          1010 Vienna
                      </p>
                      <p>
                          T: +43 1 51581-2200
                          <br/>
                          E: <a href="mailto:acdh@oeaw.ac.at">acdh@oeaw.ac.at</a>
                      </p>
                  </div>
              </div>
              <div class="footer-widget col-lg-4 col-md-3 col-sm-4">
                  <h6 class="font-weight-bold">PROJECT PARTNERS</h6>
                  <div class="container">
                      <div class="row">
                             
                      </div>
                  </div>
              </div>
              <!-- .footer-widget -->                       
              <div class="footer-widget col-lg-3 col-md-4 col-sm-3 ml-auto">
                  <div class="row">
                      <div class="textwidget custom-html-widget">
                          <h6 class="font-weight-bold">HELPDESK</h6>
                          <p>ACDH-CH runs a helpdesk offering advice for questions related to various digital humanities topics.</p>
                          <p>
                              <a class="helpdesk-button" href="mailto:acdh-helpdesk@oeaw.ac.at">ASK US!</a>
                          </p>
                      </div>
                  </div>
                  <div class="row">
                      <div class="custom-html-widget" style="margin-left:0 !important;">
                          <div class="row">
                              <div class="textwidget custom-html-widget">
                                  <p style="margin-bottom:0 !important;">Social: </p>                                    
                              </div>
                          </div>                                
                          <div class="row">                         
                              <div class="custom-html-widget col-md-4">                                    
                                  <a id="github-logo" title="Paul Kretschmer Reise Griechenland/Lesbos" href="https://github.com/acdh-oeaw/kretschmer-static-py" class="nav-link" target="_blank">
                                      <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-4.466 19.59c-.405.078-.534-.171-.534-.384v-2.195c0-.747-.262-1.233-.55-1.481 1.782-.198 3.654-.875 3.654-3.947 0-.874-.312-1.588-.823-2.147.082-.202.356-1.016-.079-2.117 0 0-.671-.215-2.198.82-.64-.18-1.324-.267-2.004-.271-.68.003-1.364.091-2.003.269-1.528-1.035-2.2-.82-2.2-.82-.434 1.102-.16 1.915-.077 2.118-.512.56-.824 1.273-.824 2.147 0 3.064 1.867 3.751 3.645 3.954-.229.2-.436.552-.508 1.07-.457.204-1.614.557-2.328-.666 0 0-.423-.768-1.227-.825 0 0-.78-.01-.055.487 0 0 .525.246.889 1.17 0 0 .463 1.428 2.688.944v1.489c0 .211-.129.459-.528.385-3.18-1.057-5.472-4.056-5.472-7.59 0-4.419 3.582-8 8-8s8 3.581 8 8c0 3.533-2.289 6.531-5.466 7.59z"/></svg>                                
                                  </a>
                              </div>
                          </div>                                
                      </div>
                  </div>
              </div>
              <!-- .footer-widget -->
          </div>
      </div>
    </div>
    <div class="bg-dark" style="border-top:1px dashed lightgrey; text-align:center; padding:0.4rem 0; font-size: 0.9rem; color: lightgrey;">
        © Copyright OEAW | <a href="imprint.html">Impressum/Imprint</a>
    </div>    
    <script src="assets/dist/js/bootstrap.bundle.min.js"></script>
    </body></html>' >> ${IMPRINT_XML}