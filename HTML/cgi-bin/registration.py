import cgi,cgitb,os
cgitb.enable()
form=cgi.FieldStorage()
Sid=form.getvalue('id')
Sname=form.getvalue('name')
Sbranch=form.getvalue('dept')
Sarea=form.getvalue('aos')
Spassword=form.getvalue('password')
Sphoneno=form.getvalue('phno')
S_email=form.getvalue('email')
a=form.getvalue('actype')
import sqlite3 
conn=sqlite3.connect("e-articles.db")
if a=='f':
	d=conn.execute("select F_email from Faculty where F_email=?",(S_email,))
	data=d.fetchall()
	if len(data)==0:
		conn.execute("insert into Faculty values(?,?,?,?,?,?,?)",(Sid,Sname,Sbranch,Sarea,Spassword,Sphoneno,S_email))
		"""import smtplib
		from email.mime.multipart import MIMEMultipart
		from email.mime.base import MIMEBase
		from email.mime.text import MIMEText
		from email.utils import COMMASPACE, formatdate
		from email import encoders
		import datetime
		smtpUser = 'srkrearticles@gmail.com'
		smtpPass = 'bdy@12345'
		COMMASPACE = ', '

		def sendMail(to, subject, text, files=[]):
			assert type(to)==list
			assert type(files)==list

			msg = MIMEMultipart()
			msg['From'] = smtpUser
			msg['To'] = COMMASPACE.join(to)
			msg['Date'] = formatdate(localtime=True)
			msg['Subject'] = 'Mail sending Test'

			msg.attach( MIMEText(text) )

			for file in files:
				part = MIMEBase('application', "octet-stream")
				part.set_payload( open(file,"rb").read() )
				encoders.encode_base64(part)
				part.add_header('Content-Disposition', 'attachment; filename="%s"'
							   % os.path.basename(file))
				msg.attach(part)

			server = smtplib.SMTP('smtp.gmail.com:587')
			server.ehlo_or_helo_if_needed()
			server.starttls()
			server.ehlo_or_helo_if_needed()
			server.login(smtpUser,smtpPass)
			server.sendmail(smtpUser, to, msg.as_string())
			print ('Done')
			server.quit()

		sendMail( [S_email],'Hi Friend', 'Hello', [])"""
		print("Content-type:text/html")
		print()
		print("""<!DOCTYPE html>
<!-- ==============================
    Project:        Metronic "Asentus" Frontend Freebie - Responsive HTML Template Based On Twitter Bootstrap 3.3.4
    Version:        1.0
    Author:         KeenThemes
    Primary use:    Corporate, Business Themes.
    Email:          support@keenthemes.com
    Follow:         http://www.twitter.com/keenthemes
    Like:           http://www.facebook.com/keenthemes
    Website:        http://www.keenthemes.com
    Premium:        Premium Metronic Admin Theme: http://themeforest.net/item/metronic-responsive-admin-dashboard-template/4021469?ref=keenthemes
================================== -->
<html lang="en" class="no-js">
    <!-- BEGIN HEAD -->
    <head>
        <meta charset="utf-8"/>
        <title>E-ARTICLES</title>
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta content="width=device-width, initial-scale=1" name="viewport"/>
        <meta content="" name="description"/>
        <meta content="" name="author"/>

        <!-- GLOBAL MANDATORY STYLES -->
        <link href="http://fonts.googleapis.com/css?family=Hind:300,400,500,600,700" rel="stylesheet" type="text/css">
        <link href="/vendor/simple-line-icons/simple-line-icons.min.css" rel="stylesheet" type="text/css"/>
        <link href="/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>

        <!-- PAGE LEVEL PLUGIN STYLES -->
        <link href="/css/animate.css" rel="stylesheet">

        <!-- THEME STYLES -->
        <link href="/css/layout.min.css" rel="stylesheet" type="text/css"/>

        <!-- Favicon -->
        <link rel="shortcut icon" href="favicon.ico"/>
    </head>
    <!-- END HEAD -->

    <!-- BODY -->
    <body>

        <!--========== HEADER ==========-->
        <header class="header navbar-fixed-top">
            <!-- Navbar -->
            <nav class="navbar" role="navigation">
                <div class="container">
                    <!-- Brand and toggle get grouped for better mobile display -->
                    <div class="menu-container">
                        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".nav-collapse">
                            <span class="sr-only">Toggle navigation</span>
                            <span class="toggle-icon"></span>
                        </button>

                        <!-- Logo -->
                        <div class="logo">
                            <a class="logo-wrap" href="/index.html">
                                <img class="logo-img logo-img-main" src="/img/logo.png" alt="Asentus Logo">
                                <img class="logo-img logo-img-active" src="/img/logo-dark.png" alt="Asentus Logo">
                            </a>
                        </div>
                        <!-- End Logo -->
                    </div>

                    <!-- Collect the nav links, forms, and other content for toggling -->
                    <div class="collapse navbar-collapse nav-collapse">
                        <div class="menu-container">
                            <ul class="navbar-nav navbar-nav-right">
                                <li class="nav-item"><a class="nav-item-child nav-item-hover" href="/index.html">Home</a></li>
                                <li class="nav-item"><a class="nav-item-child nav-item-hover" href="#">Login</a></li>
                                <li class="nav-item"><a class="nav-item-child nav-item-hover" href="/registration.html">Register</a></li>
                                <li class="nav-item"><a class="nav-item-child nav-item-hover" href="/contact.html">contact</a></li>
                
                              </ul>
                        </div>
                    </div>
                    <!-- End Navbar Collapse -->
                </div>
            </nav>
            <!-- Navbar -->
        </header>
        <!--========== END HEADER ==========-->

        <!--========== PARALLAX ==========-->
       <div class="parallax-window" data-parallax="scroll" data-image-src="/img/1920x1080/01.jpg">
            <div class="parallax-content container">
                <h1 class="carousel-title">Sign In here</h1>
                <p>To share your valuable information to entire world through our website</p>
            </div>
        </div>
        <!--========== PARALLAX ==========-->

        <!--========== PAGE LAYOUT ==========-->
        <!-- Contact List -->
     <!--   <div class="section-seperator">
            <div class="content-lg container">
                <div class="row">
                    <!-- Contact List -->
               <!--     <div class="col-sm-4 sm-margin-b-50">
                        <div class="wow fadeInLeft" data-wow-duration=".3" data-wow-delay=".3s">
                            <h3><a href="#">New York</a> <span class="text-uppercase margin-l-20">Head Office</span></h3>
                            <p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed tempor incdidunt ut laboret dolor magna ut consequat siad esqudiat dolor</p>
                            <ul class="list-unstyled contact-list">
                                <li><i class="margin-r-10 color-base icon-call-out"></i> 1 012 3456 7890</li>
                                <li><i class="margin-r-10 color-base icon-envelope"></i> hq@acidus.com</li>
                            </ul>
                        </div>
                    </div>
                    <!-- End Contact List -->

                    <!-- Contact List -->
               <!--     <div class="col-sm-4 sm-margin-b-50">
                        <div class="wow fadeInLeft" data-wow-duration=".3" data-wow-delay=".3s">
                            <h3><a href="#">London</a> <span class="text-uppercase margin-l-20">Operation</span></h3>
                            <p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed tempor incdidunt ut laboret dolor magna ut consequat siad esqudiat dolor</p>
                            <ul class="list-unstyled contact-list">
                                <li><i class="margin-r-10 color-base icon-call-out"></i> 44 77 3456 7890</li>
                                <li><i class="margin-r-10 color-base icon-envelope"></i> operation@acidus.com</li>
                            </ul>
                        </div>
                    </div>
                    <!-- End Contact List -->

                    <!-- Contact List -->
             <!--       <div class="col-sm-4 sm-margin-b-50">
                        <div class="wow fadeInLeft" data-wow-duration=".3" data-wow-delay=".3s">
                            <h3><a href="#">Singapore</a> <span class="text-uppercase margin-l-20">Finance</span></h3>
                            <p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed tempor incdidunt ut laboret dolor magna ut consequat siad esqudiat dolor</p>
                            <ul class="list-unstyled contact-list">
                                <li><i class="margin-r-10 color-base icon-call-out"></i> 50 012 456 7890</li>
                                <li><i class="margin-r-10 color-base icon-envelope"></i> finance@acidus.com</li>
                            </ul>
                        </div>
                    </div>
                    <!-- End Contact List -->
                </div>
                <!--// end row -->
            </div>
        </div>
        <!-- End Contact List -->

        <!-- Google Map -->
      <!--  <div id="map" class="map height-400"></div>-->

        <!-- Promo Section -->
     <!--   <div class="promo-section overflow-h">
            <div class="container">
                <div class="clearfix">
                    <div class="ver-center">
                        <div class="ver-center-aligned">
                            <div class="promo-section-col">
                                <h2>Our Clients</h2>
                                <p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed tempor incididunt ut laboret dolore magna aliqua enim minim veniam exercitation ipsum dolor sit amet consectetur adipiscing elit sed tempor incididunt ut laboret dolore magna aliqua enim minim veniam exercitation</p>
                                <p>Ipsum dolor sit amet consectetur adipiscing elit sed tempor incididut ut sead laboret dolore magna aliqua enim minim veniam exercitation ipsum dolor sit amet consectetur adipiscing</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="promo-section-img-right">
                <img class="img-responsive" src="/img/970x970/01.jpg" alt="Content Image">
            </div>
        </div>-->
        <!-- End Promo Section -->
        <!--========== END PAGE LAYOUT ==========-->

        <!--========== FOOTER ==========-->
        <footer class="footer">
            <!-- Links -->
            <div class="footer-seperator">
                <div class="content-lg container">
                    <div class="row">
                       <!-- <div class="col-sm-2 sm-margin-b-50">
                            <!-- List -->
                          <!--  <ul class="list-unstyled footer-list">
                                <li class="footer-list-item"><a class="footer-list-link" href="#">Home</a></li>
                                <li class="footer-list-item"><a class="footer-list-link" href="#">About</a></li>
                                <li class="footer-list-item"><a class="footer-list-link" href="#">Products</a></li>
                                <li class="footer-list-item"><a class="footer-list-link" href="#">Pricing</a></li>
                                <li class="footer-list-item"><a class="footer-list-link" href="#">Clients</a></li>
                                <li class="footer-list-item"><a class="footer-list-link" href="#">Careers</a></li>
                                <li class="footer-list-item"><a class="footer-list-link" href="#">Contact</a></li>
                                <li class="footer-list-item"><a class="footer-list-link" href="#">Terms</a></li>
                            </ul>
                            <!-- End List -->
                     <!--   </div>
                        <div class="col-sm-4 sm-margin-b-30">
                            <!-- List -->
                         <!--   <ul class="list-unstyled footer-list">
                                <li class="footer-list-item"><a class="footer-list-link" href="#">Twitter</a></li>
                                <li class="footer-list-item"><a class="footer-list-link" href="#">Facebook</a></li>
                                <li class="footer-list-item"><a class="footer-list-link" href="#">Instagram</a></li>
                                <li class="footer-list-item"><a class="footer-list-link" href="#">YouTube</a></li>
                            </ul>
                            <!-- End List -->
                        </div>
                        <div class="col-sm-5 sm-margin-b-30" align="center">
							<form action="loginvali.py" method="post">
								<h2 class="color-white">Sign in</h2>
								<!--<input type="text" class="form-control footer-input margin-b-20" placeholder="Name" required>-->
								<select name="actype" class="form-control footer-input margin-b-20">
								    <option selected>Select Account Type</option>
									<option value="f" >Faculty</option>
									<option value="s" >Student</option>
								</select>
								<input type="email" class="form-control footer-input margin-b-20" placeholder="* Email" required name="email">
								<input type="password" class="form-control footer-input margin-b-20" placeholder="* Password" required name="password">
							    <!-- <textarea class="form-control footer-input margin-b-30" rows="6" placeholder="Message" required></textarea>-->
								<button type="submit" class="btn-theme btn-theme-sm btn-base-bg text-uppercase">Sign in</button><br><br>
								<a href="/registration.html">New user,Register here</a>
							</form>
                        </div>
                    </div>
                    <!--// end row -->
                </div>
            </div>
            <!-- End Links -->

            <!-- Copyright -->
            <div class="content container">
                <div class="row">
                    <div class="col-xs-6">
                        <img class="footer-logo" src="/img/logo.png" alt="Asentus Logo">
                    </div>
                    <div class="col-xs-6 text-right">
                        <!--<p class="margin-b-0"><a class="color-base fweight-700" href="http://keenthemes.com/preview/asentus/">Asentus</a> Theme Powered by: <a class="color-base fweight-700" href="http://www.keenthemes.com/">KeenThemes.com</a></p>-->
                    </div>
                </div>
                <!--// end row -->
            </div>
            <!-- End Copyright -->
        </footer>
        <!--========== END FOOTER ==========-->

        <!-- Back To Top -->
        <a href="javascript:void(0);" class="js-back-to-top back-to-top">Top</a>

        <!-- JAVASCRIPTS(Load javascripts at bottom, this will reduce page load time) -->
        <!-- CORE PLUGINS -->
        <script src="/vendor/jquery.min.js" type="text/javascript"></script>
        <script src="/vendor/jquery-migrate.min.js" type="text/javascript"></script>
        <script src="/vendor/bootstrap/js/bootstrap.min.js" type="text/javascript"></script>

        <!-- PAGE LEVEL PLUGINS -->
        <script src="/vendor/jquery.easing.js" type="text/javascript"></script>
        <script src="/vendor/jquery.back-to-top.js" type="text/javascript"></script>
        <script src="/vendor/jquery.smooth-scroll.js" type="text/javascript"></script>
        <script src="/vendor/jquery.wow.min.js" type="text/javascript"></script>
        <script src="/vendor/jquery.parallax.min.js" type="text/javascript"></script>

        <!-- PAGE LEVEL SCRIPTS -->
        <script src="/js/layout.min.js" type="text/javascript"></script>
        <script src="/js/components/wow.min.js" type="text/javascript"></script>
        <script src="/js/components/gmap.min.js" type="text/javascript"></script>
        <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBsXUGTFS09pLVdsYEE9YrO2y4IAncAO2U&amp;callback=initMap" async defer></script>

    </body>
    <!-- END BODY -->
</html>
		""")
	else:
		print("Content-type:text/html")
		print()
		print("""<h1><a href="/registration.html">Registration Failed Username already exists</a><h1>""")
	
elif a=="s":
	d=conn.execute("select S_email from Students where S_email=?",(S_email,))
	data=d.fetchall()
	if len(data)==0:
		"""import smtplib
		from email.mime.multipart import MIMEMultipart
		from email.mime.base import MIMEBase
		from email.mime.text import MIMEText
		from email.utils import COMMASPACE, formatdate
		from email import encoders
		import datetime
		smtpUser = 'srkrearticles@gmail.com'
		smtpPass = 'bdy@12345'
		COMMASPACE = ', '

		def sendMail(to, subject, text, files=[]):
			assert type(to)==list
			assert type(files)==list

			msg = MIMEMultipart()
			msg['From'] = smtpUser
			msg['To'] = COMMASPACE.join(to)
			msg['Date'] = formatdate(localtime=True)
			msg['Subject'] = 'Mail sending Test'

			msg.attach( MIMEText(text) )

			for file in files:
				part = MIMEBase('application', "octet-stream")
				part.set_payload( open(file,"rb").read() )
				encoders.encode_base64(part)
				part.add_header('Content-Disposition', 'attachment; filename="%s"'
							   % os.path.basename(file))
				msg.attach(part)

			server = smtplib.SMTP('smtp.gmail.com:587')
			server.ehlo_or_helo_if_needed()
			server.starttls()
			server.ehlo_or_helo_if_needed()
			server.login(smtpUser,smtpPass)
			server.sendmail(smtpUser, to, msg.as_string())
			print ('Done')
			server.quit()

		sendMail( [S_email],'Hi Friend', 'Hello', [])"""
		conn.execute("insert into Students values(?,?,?,?,?,?,?)",(Sid,Sname,Sbranch,Sarea,Spassword,Sphoneno,S_email))
		print("Content-type:text/html")
		print()
		print("""<!DOCTYPE html>
<!-- ==============================
	Project:        Metronic "Asentus" Frontend Freebie - Responsive HTML Template Based On Twitter Bootstrap 3.3.4
	Version:        1.0
	Author:         KeenThemes
	Primary use:    Corporate, Business Themes.
	Email:          support@keenthemes.com
	Follow:         http://www.twitter.com/keenthemes
	Like:           http://www.facebook.com/keenthemes
	Website:        http://www.keenthemes.com
	Premium:        Premium Metronic Admin Theme: http://themeforest.net/item/metronic-responsive-admin-dashboard-template/4021469?ref=keenthemes
================================== -->
<html lang="en" class="no-js">
	<!-- BEGIN HEAD -->
	<head>
		<meta charset="utf-8"/>
		<title>E-ARTICLES</title>
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta content="width=device-width, initial-scale=1" name="viewport"/>
		<meta content="" name="description"/>
		<meta content="" name="author"/>

		<!-- GLOBAL MANDATORY STYLES -->
		<link href="http://fonts.googleapis.com/css?family=Hind:300,400,500,600,700" rel="stylesheet" type="text/css">
		<link href="/vendor/simple-line-icons/simple-line-icons.min.css" rel="stylesheet" type="text/css"/>
		<link href="/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>

		<!-- PAGE LEVEL PLUGIN STYLES -->
		<link href="/css/animate.css" rel="stylesheet">

		<!-- THEME STYLES -->
		<link href="/css/layout.min.css" rel="stylesheet" type="text/css"/>

		<!-- Favicon -->
		<link rel="shortcut icon" href="favicon.ico"/>
	</head>
	<!-- END HEAD -->

	<!-- BODY -->
	<body>

		<!--========== HEADER ==========-->
		<header class="header navbar-fixed-top">
			<!-- Navbar -->
			<nav class="navbar" role="navigation">
				<div class="container">
					<!-- Brand and toggle get grouped for better mobile display -->
					<div class="menu-container">
						<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".nav-collapse">
							<span class="sr-only">Toggle navigation</span>
							<span class="toggle-icon"></span>
						</button>

						<!-- Logo -->
						<div class="logo">
							<a class="logo-wrap" href="index.html">
								<img class="logo-img logo-img-main" src="/img/logo.png" alt="Asentus Logo">
								<img class="logo-img logo-img-active" src="/img/logo-dark.png" alt="Asentus Logo">
							</a>
						</div>
						<!-- End Logo -->
					</div>

					<!-- Collect the nav links, forms, and other content for toggling -->
					<div class="collapse navbar-collapse nav-collapse">
						<div class="menu-container">
							<ul class="navbar-nav navbar-nav-right">
								<li class="nav-item"><a class="nav-item-child nav-item-hover" href="index.html">Home</a></li>
								<li class="nav-item"><a class="nav-item-child nav-item-hover" href="#">Login</a></li>
								<li class="nav-item"><a class="nav-item-child nav-item-hover" href="/registration.html">Register</a></li>
								
								<li class="nav-item"><a class="nav-item-child nav-item-hover active" href="/contact.html">Contact</a></li>
							</ul>
						</div>
					</div>
					<!-- End Navbar Collapse -->
				</div>
			</nav>
			<!-- Navbar -->
		</header>
		<!--========== END HEADER ==========-->

		<!--========== PARALLAX ==========-->
	   <div class="parallax-window" data-parallax="scroll" data-image-src="/img/1920x1080/01.jpg">
			<div class="parallax-content container">
				<h1 class="carousel-title">Sign In here</h1>
				<p>To share your valuable information to entire world through our website</p>
			</div>
		</div>
		<!--========== PARALLAX ==========-->

		<!--========== PAGE LAYOUT ==========-->
		<!-- Contact List -->
	 <!--   <div class="section-seperator">
			<div class="content-lg container">
				<div class="row">
					<!-- Contact List -->
			   <!--     <div class="col-sm-4 sm-margin-b-50">
						<div class="wow fadeInLeft" data-wow-duration=".3" data-wow-delay=".3s">
							<h3><a href="#">New York</a> <span class="text-uppercase margin-l-20">Head Office</span></h3>
							<p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed tempor incdidunt ut laboret dolor magna ut consequat siad esqudiat dolor</p>
							<ul class="list-unstyled contact-list">
								<li><i class="margin-r-10 color-base icon-call-out"></i> 1 012 3456 7890</li>
								<li><i class="margin-r-10 color-base icon-envelope"></i> hq@acidus.com</li>
							</ul>
						</div>
					</div>
					<!-- End Contact List -->

					<!-- Contact List -->
			   <!--     <div class="col-sm-4 sm-margin-b-50">
						<div class="wow fadeInLeft" data-wow-duration=".3" data-wow-delay=".3s">
							<h3><a href="#">London</a> <span class="text-uppercase margin-l-20">Operation</span></h3>
							<p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed tempor incdidunt ut laboret dolor magna ut consequat siad esqudiat dolor</p>
							<ul class="list-unstyled contact-list">
								<li><i class="margin-r-10 color-base icon-call-out"></i> 44 77 3456 7890</li>
								<li><i class="margin-r-10 color-base icon-envelope"></i> operation@acidus.com</li>
							</ul>
						</div>
					</div>
					<!-- End Contact List -->

					<!-- Contact List -->
			 <!--       <div class="col-sm-4 sm-margin-b-50">
						<div class="wow fadeInLeft" data-wow-duration=".3" data-wow-delay=".3s">
							<h3><a href="#">Singapore</a> <span class="text-uppercase margin-l-20">Finance</span></h3>
							<p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed tempor incdidunt ut laboret dolor magna ut consequat siad esqudiat dolor</p>
							<ul class="list-unstyled contact-list">
								<li><i class="margin-r-10 color-base icon-call-out"></i> 50 012 456 7890</li>
								<li><i class="margin-r-10 color-base icon-envelope"></i> finance@acidus.com</li>
							</ul>
						</div>
					</div>
					<!-- End Contact List -->
				</div>
				<!--// end row -->
			</div>
		</div>
		<!-- End Contact List -->

		<!-- Google Map -->
	  <!--  <div id="map" class="map height-400"></div>-->

		<!-- Promo Section -->
	 <!--   <div class="promo-section overflow-h">
			<div class="container">
				<div class="clearfix">
					<div class="ver-center">
						<div class="ver-center-aligned">
							<div class="promo-section-col">
								<h2>Our Clients</h2>
								<p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed tempor incididunt ut laboret dolore magna aliqua enim minim veniam exercitation ipsum dolor sit amet consectetur adipiscing elit sed tempor incididunt ut laboret dolore magna aliqua enim minim veniam exercitation</p>
								<p>Ipsum dolor sit amet consectetur adipiscing elit sed tempor incididut ut sead laboret dolore magna aliqua enim minim veniam exercitation ipsum dolor sit amet consectetur adipiscing</p>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="promo-section-img-right">
				<img class="img-responsive" src="/img/970x970/01.jpg" alt="Content Image">
			</div>
		</div>-->
		<!-- End Promo Section -->
		<!--========== END PAGE LAYOUT ==========-->

		<!--========== FOOTER ==========-->
		<footer class="footer">
			<!-- Links -->
			<div class="footer-seperator">
				<div class="content-lg container">
					<div class="row">
					   <!-- <div class="col-sm-2 sm-margin-b-50">
							<!-- List -->
						  <!--  <ul class="list-unstyled footer-list">
								<li class="footer-list-item"><a class="footer-list-link" href="#">Home</a></li>
								<li class="footer-list-item"><a class="footer-list-link" href="#">About</a></li>
								<li class="footer-list-item"><a class="footer-list-link" href="#">Products</a></li>
								<li class="footer-list-item"><a class="footer-list-link" href="#">Pricing</a></li>
								<li class="footer-list-item"><a class="footer-list-link" href="#">Clients</a></li>
								<li class="footer-list-item"><a class="footer-list-link" href="#">Careers</a></li>
								<li class="footer-list-item"><a class="footer-list-link" href="#">Contact</a></li>
								<li class="footer-list-item"><a class="footer-list-link" href="#">Terms</a></li>
							</ul>
							<!-- End List -->
					 <!--   </div>
						<div class="col-sm-4 sm-margin-b-30">
							<!-- List -->
						 <!--   <ul class="list-unstyled footer-list">
								<li class="footer-list-item"><a class="footer-list-link" href="#">Twitter</a></li>
								<li class="footer-list-item"><a class="footer-list-link" href="#">Facebook</a></li>
								<li class="footer-list-item"><a class="footer-list-link" href="#">Instagram</a></li>
								<li class="footer-list-item"><a class="footer-list-link" href="#">YouTube</a></li>
							</ul>
							<!-- End List -->
						</div>
						<div class="col-sm-5 sm-margin-b-30" align="center">
							<form action="loginvali.py" method="post">
								<h2 class="color-white">Sign in</h2>
								<!--<input type="text" class="form-control footer-input margin-b-20" placeholder="Name" required>-->
								<select name="actype" class="form-control footer-input margin-b-20">
									<option selected>Select Account Type</option>
									<option value="f" >Faculty</option>
									<option value="s" >Student</option>
								</select>
								<input type="email" class="form-control footer-input margin-b-20" placeholder="* Email" required name="email">
								<input type="password" class="form-control footer-input margin-b-20" placeholder="* Password" required name="password">
								<!-- <textarea class="form-control footer-input margin-b-30" rows="6" placeholder="Message" required></textarea>-->
								<button type="submit" class="btn-theme btn-theme-sm btn-base-bg text-uppercase">Sign in</button><br><br>
								<a href="/registration.html">New user,Register here</a>
							</form>
						</div>
					</div>
					<!--// end row -->
				</div>
			</div>
			<!-- End Links -->

			<!-- Copyright -->
			<div class="content container">
				<div class="row">
					<div class="col-xs-6">
						<img class="footer-logo" src="/img/logo.png" alt="Asentus Logo">
					</div>
					<div class="col-xs-6 text-right">
						<p class="margin-b-0"><a class="color-base fweight-700" href="http://keenthemes.com/preview/asentus/">Asentus</a> Theme Powered by: <a class="color-base fweight-700" href="http://www.keenthemes.com/">KeenThemes.com</a></p>
					</div>
				</div>
				<!--// end row -->
			</div>
			<!-- End Copyright -->
		</footer>
		<!--========== END FOOTER ==========-->

		<!-- Back To Top -->
		<a href="javascript:void(0);" class="js-back-to-top back-to-top">Top</a>

		<!-- JAVASCRIPTS(Load javascripts at bottom, this will reduce page load time) -->
		<!-- CORE PLUGINS -->
		<script src="/vendor/jquery.min.js" type="text/javascript"></script>
		<script src="/vendor/jquery-migrate.min.js" type="text/javascript"></script>
		<script src="/vendor/bootstrap/js/bootstrap.min.js" type="text/javascript"></script>

		<!-- PAGE LEVEL PLUGINS -->
		<script src="/vendor/jquery.easing.js" type="text/javascript"></script>
		<script src="/vendor/jquery.back-to-top.js" type="text/javascript"></script>
		<script src="/vendor/jquery.smooth-scroll.js" type="text/javascript"></script>
		<script src="/vendor/jquery.wow.min.js" type="text/javascript"></script>
		<script src="/vendor/jquery.parallax.min.js" type="text/javascript"></script>

		<!-- PAGE LEVEL SCRIPTS -->
		<script src="/js/layout.min.js" type="text/javascript"></script>
		<script src="/js/components/wow.min.js" type="text/javascript"></script>
		<script src="/js/components/gmap.min.js" type="text/javascript"></script>
		<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBsXUGTFS09pLVdsYEE9YrO2y4IAncAO2U&amp;callback=initMap" async defer></script>

		 </body>
		<!-- END BODY -->
		</html>""")
	else:
		print("Content-type:text/html")
		print()
		print("""<h1><a href="/registration.html">Registration Failed Username already exists</a><h1>""")
conn.commit()
conn.close()
