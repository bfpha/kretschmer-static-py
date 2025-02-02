# bin/bash

REDMINE_ID=20278
IMPRINT_XML=./templates/imprint.html
rm ${IMPRINT_XML}
echo '<html lang="en">'  >> ${IMPRINT_XML}
echo '<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Daniel Stoxreiter">
    <title>Die Reise von Paul und Leona Kretschmer nach Lesbos</title>
    <link href="assets/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="dist/fundament/css/fundament.min.css" rel="stylesheet">
    <link href="static/css/style.css" rel="stylesheet"> 
    <script  src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
    <script src="dist/fundament/vendor/jquery/jquery.min.js"></script> 
    <script src="dist/fundament/js/fundament.min.js"></script> 
    <script src="assets/dist/js/bootstrap.bundle.min.js"></script>      
  </head>'  >> ${IMPRINT_XML}
echo '<body class="page">
    <div class="wrapper-fluid wrapper-navbar bg-light sticky-navbar" id="wrapper-navbar" >
      <a class="skip-link screen-reader-text sr-only" href="#content">Skip to content</a>
      <nav class="navbar navbar-expand-lg navbar-light" style="background-color:#fff;color:#444;" id="wrapper-navbar-nav">
        <!-- Your site title as branding in the menu -->
        <a href="index.html" class="navbar-brand custom-logo-link text-right" rel="home" itemprop="url">
            <img id="main-logo" class="card-img-left flex-auto d-md-block" src="static/img/oeaw-logo.png" alt="Österreichische Akademie der Wissenschaften" title="Österreichische Akademie der Wissenschaften" />
        </a><!-- end custom logo -->
        <!-- 
        <a class="navbar-brand site-title-with-logo lead" rel="home" href="index.html" title="Die Reise von Paul und Leona Kretschmer nach Lesbos" itemprop="url">
            Kretschmer Lesbos Online
        </a>
         -->
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-end" id="navbarNavDropdown">
            <!-- Your menu goes here -->
            <ul id="main-menu" class="navbar-nav">
                <li class="nav-item dropdown-submenu">
                    <a title="Fotos" href="fotos-detail.html" class="nav-link lead text-muted">Fotografien</a>
                </li>
                <li class="nav-item dropdown-submenu">
                    <a title="Tonaufnahmen" href="tonaufnahmen-detail.html" class="nav-link lead text-muted">Tonaufnahmen</a>
                </li>
                <li class="nav-item dropdown">
                    <a title="Projekt" href="#" data-toggle="dropdown" class="nav-link dropdown-toggle lead text-muted">Projekt <span class="caret"></span></a>
                    <ul class=" dropdown-menu" role="menu">
                        <li class="nav-item dropdown-submenu">
                            <a title="Über das Projekt" href="about.html" class="nav-link lead text-muted">Über das Projekt</a>
                        </li>
                        <li class="nav-item dropdown-submenu">
                            <a title="Reise" href="journey.html" class="nav-link lead text-muted">Reise</a>
                        </li>
                        <li class="nav-item dropdown-submenu">
                            <a title="Team" href="team.html" class="nav-link lead text-muted">Team</a>
                        </li>
                    </ul>                                
                </li>
                <li class="nav-item dropdown">
                    <a title="Index" href="#" data-toggle="dropdown" class="nav-link dropdown-toggle lead text-muted">Index <span class="caret"></span></a>
                    <ul class="dropdown-menu" role="menu">
                        <li class="nav-item dropdown-submenu">
                            <a title="Orte" href="place-index.html" class="nav-link lead text-muted">Orte</a>
                        </li>
                        <li class="nav-item dropdown-submenu">
                            <a title="Personen" href="person-index.html" class="nav-link lead text-muted">Personen</a>
                        </li>
                        <li class="nav-item dropdown-submenu">
                            <a title="Fotos" href="table.html" class="nav-link lead text-muted">Fotografien</a>
                        </li>
                        <li class="nav-item dropdown-submenu">
                            <a title="Tonaufnahmen" href="table_audio.html" class="nav-link lead text-muted">Tonaufnahmen</a>
                        </li>
                    </ul>                                
                </li>
            </ul>                       
        </div>
            <!-- .collapse navbar-collapse -->
      </nav>
      <!-- .site-navigation -->
    </div><div class="hfeed site" id="page"><div style="width:80%;margin:0 auto;padding:2em;">' >> ${IMPRINT_XML}
curl https://shared.acdh.oeaw.ac.at/acdh-common-assets/api/imprint.php?serviceID=${REDMINE_ID} >> ${IMPRINT_XML}
echo '</div><div class="wrapper fundament-default-footer hide-reading" id="wrapper-footer-full">
        <div class="container-fluid" id="footer-full-content" tabindex="-1">
            <div class="footer-separator">
                Kontakt
            </div>
            <div class="row">
                <div class="footer-widget col-md-1 ml-auto text-center ">
                    <div class="textwidget custom-html-widget">
                        <a href="https://www.oeaw.ac.at/acdh"><img src="https://fundament.acdh.oeaw.ac.at/common-assets/images/acdh_logo.svg" class="image" alt="Austrian Centre for Digital Humanities and Cultural Heritage" style="max-width: 100%; height: auto;" title="Austrian Centre for Digital Humanities and Cultural Heritage"/></a>
                    </div>
                </div>
                <!-- .footer-widget -->
                <div class="footer-widget col-md-2">
                    <div class="textwidget custom-html-widget">
                        <p>
                            ACDH-CH OEAW
                            <br/>
                            Austrian Centre for Digital Humanities and Cultural Heritage
                            <br/>
                            Österreichischen Akademie der Wissenschaften
                        </p>
                        <p>
                            Bäckerstraße 13
                            <br/>
                            1010 Wien
                        </p>
                        <p>
                            T: +43 1 51581-2200
                            <br/>
                            E: <a href="mailto:acdh-ch-helpdesk@oeaw.ac.at">acdh-ch-helpdesk@oeaw.ac.at</a>
                        </p>
                    </div>
                </div>
                <div class="footer-widget col-md-1 ml-auto text-center">
                  <div class="textwidget custom-html-widget">
                      <a href="https://www.oeaw.ac.at/phonogrammarchiv/home"><img src="static/img/logo_akronym_pha_cali.png" class="image" alt="Phonogrammarchiv" style="max-width: 100%; height: auto;" title="Phonogrammarchiv"/></a>
                  </div>
                </div>
                <!-- .footer-widget -->
                <div class="footer-widget col-md-2">
                    <div class="textwidget custom-html-widget">
                        <p>
                            Phonogrammarchiv der
                            <br/>
                            Österreichischen Akademie der Wissenschaften
                        </p>
                        <p>
                            Liebiggasse 5
                            <br/>
                            1010 Vienna
                        </p>
                        <p>
                            T: +43 1 4277-29601
                            <br/>
                            E: <a href="mailto:pha@oeaw.ac.at">pha@oeaw.ac.at</a>
                        </p>
                    </div>
                </div>
                <div class="footer-widget col-md-5">
                    <h6 class="font-weight-bold" style="margin-bottom: 1em;">PROJEKTPARTNER</h6>
                    <div class="row">     
                        <div class="col-md-4">
                            <div class="flex-md-row mb-4 align-items-center">
                                <a href="https://www.onb.ac.at/"><img class="card-img-right flex-auto d-md-block" src="static/img/OeNB_cmyk.jpg" alt="Österreichische Nationalbibliothek" style="max-width: 200px; height: auto; vertical-align: middle;" title="Österreichische Nationalbibliothek" /></a>
                            </div>
                        </div>                       
                        <div class="col-md-4">
                            <div class="flex-md-row mb-4 align-items-center">
                                <a href="https://www.wien.gv.at"><img class="card-img-right flex-auto d-md-block" src="static/img/200px-Wien_logo.svg.png" alt="Stadt Wien" style="max-width: 140px; height: auto; padding: .5em;" title="Stadt Wien"/></a>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="flex-md-row mb-4 align-items-center">
                                <a href="http://kentrolaografias.gr/"><img class="card-img-right flex-auto d-md-block" src="static/img/logo_hfrc_chelidona_engl-1.jpg" alt="Kentrolaografias" style="max-width: 160px; height: auto; vertical-align: middle;" title="Kentrolaografias" /></a>
                            </div>
                        </div>                                
                    </div>
                    <div class="row">
                        <div class="col-md-4">
                            <div class="flex-md-row mb-4 align-items-center">
                                <a href="http://www.anagnostirioagiasou.gr/el"><img class="card-img-right flex-auto d-md-block" src="static/img/pastedImage.png" alt="Anagnostirioagiasou" style="max-width: 120px; height: auto; vertical-align: middle;" title="Anagnostirioagiasou" /></a>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="flex-md-row mb-4 align-items-center">
                                <a href="https://www.cplm.gr"><img class="card-img-right flex-auto d-md-block" src="static/img/logo_bibliothiki_mytilinis copy-1.jpg" alt="Bibliothek Mytilinis" style="max-width: 200px; height: auto; margin-top:1em;" title="Bibliothek Mytilinis" /></a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="footer-widget col-md-1">
                    <div class="row">
                        <div class="custom-html-widget" style="margin-left:0 !important;">
                            <div class="row">
                                <div class="textwidget custom-html-widget">
                                    <p style="margin-bottom:0 !important;">Soziale Medien: </p>                                    
                                </div>
                            </div>                                
                            <div class="row">                         
                                <div class="custom-html-widget col-md-4">                                    
                                    <a id="github-logo" title="Auden Musulin on GitHub" href="https://github.com/acdh-oeaw/kretschmer-static-py" class="nav-link" target="_blank">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-4.466 19.59c-.405.078-.534-.171-.534-.384v-2.195c0-.747-.262-1.233-.55-1.481 1.782-.198 3.654-.875 3.654-3.947 0-.874-.312-1.588-.823-2.147.082-.202.356-1.016-.079-2.117 0 0-.671-.215-2.198.82-.64-.18-1.324-.267-2.004-.271-.68.003-1.364.091-2.003.269-1.528-1.035-2.2-.82-2.2-.82-.434 1.102-.16 1.915-.077 2.118-.512.56-.824 1.273-.824 2.147 0 3.064 1.867 3.751 3.645 3.954-.229.2-.436.552-.508 1.07-.457.204-1.614.557-2.328-.666 0 0-.423-.768-1.227-.825 0 0-.78-.01-.055.487 0 0 .525.246.889 1.17 0 0 .463 1.428 2.688.944v1.489c0 .211-.129.459-.528.385-3.18-1.057-5.472-4.056-5.472-7.59 0-4.419 3.582-8 8-8s8 3.581 8 8c0 3.533-2.289 6.531-5.466 7.59z"/></svg>                                
                                    </a>
                                </div>
                            </div>                                
                        </div>
                    </div>
                </div>
                <!-- .footer-widget -->                       
                
                <!-- .footer-widget -->
            </div>
        </div>
      </div>
      <!-- #wrapper-footer-full -->
      <div class="footer-imprint-bar hide-reading" id="wrapper-footer-secondary" style="text-align:center; padding:0.4rem 0; font-size: 0.9rem;" >
        © Copyright OEAW | <a href="imprint.html">Impressum/Imprint</a>
      </div> 
    </div>
    <script type="text/javascript">
        // When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
        window.onscroll = function() {scrollFunction()};

        function scrollFunction() {
            if (document.body.scrollTop >= 80 || document.documentElement.scrollTop >= 80) {
                document.getElementById("main-logo").classList.add("fade-logo-transition");
            } else {
                document.getElementById("main-logo").classList.remove("fade-logo-transition");
            }
        }
    </script>   
  </body>
</html>' >> ${IMPRINT_XML}