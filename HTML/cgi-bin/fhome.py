import cgi,cgitb
cgitb.enable()
import sqlite3
form=cgi.FieldStorage()
conn=sqlite3.connect('e-articles.db')
d3=conn.execute("select count(distinct Area) from Articles")
data3=d3.fetchall()
d4=conn.execute("select distinct Area from Articles")
data4=d4.fetchall()
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
		<link href="/vendor/swiper/css/swiper.min.css" rel="stylesheet" type="text/css"/>

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
							<a class="logo-wrap" href="fhome.py">
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
								<li class="nav-item"><a class="nav-item-child nav-item-hover active" href="fhome.py">Read Articles</a></li>
								<li class="nav-item"><a class="nav-item-child nav-item-hover" href="fssearch.py">Read Students Articles</a></li>
                                <li class="nav-item"><a class="nav-item-child nav-item-hover " href="fpublish.py">Publish an Article</a></li>
                                <li class="nav-item"><a class="nav-item-child nav-item-hover" href="fprofile.py">Profile</a></li>
                                <li class="nav-item"><a class="nav-item-child nav-item-hover" href="fverify.py">Verify Articles</a></li>
								<li class="nav-item"><a class="nav-item-child nav-item-hover" href="/index.html">Sign Out</a></li>
								<!--<li class="nav-item"><a class="nav-item-child nav-item-hover" href="contact.html">Contact</a></li>-->
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
				<h1 class="carousel-title">READ ARTICLES</h1>
				<p>HERE YOU CAN FIND<br/> THE ARTICLES PUBLISHED AND YOU CAN READ THEM</p>
				<form action="fsearch.py" method="post">
							<h2 class="color-white">Search By Area</h2>
            <select name="genre" class="form-control footer-input margin-b-20">
            <option>Select Area</option>""")
for k in range(0,data3[0][0]):
    print("""<option value=""",data4[k][0],""">""",data4[k][0],"""</option>""")
print("""</select><input type="hidden">
<button type="submit" class="btn-theme btn-theme-sm btn-base-bg text-uppercase">Search</button>
            </form>
			</div>
		</div>
		<!--========== PARALLAX ==========-->

		<!--========== PAGE LAYOUT ==========-->
		<!-- Pricing -->
		<div class="bg-color-sky-light">
			<div class="content-lg container">""")
print("""</div>
		</div>
		<!-- End Pricing -->

		<!-- Testimonials -->
	  <!--  <div class="content-lg container">
			<div class="row">
				<div class="col-sm-9">
					<h2>Why Customers Are Choosing Asentus?</h2>

					<!-- Swiper Testimonials -->
				<!--    <div class="swiper-slider swiper-testimonials">
						<!-- Swiper Wrapper -->
				   <!--     <div class="swiper-wrapper">
							<div class="swiper-slide">
								<blockquote class="blockquote">
									<div class="margin-b-20">
										Lorem ipsum dolor sit amet consectetur adipiscing elit sed tempor incididunt ut laboret dolore magna aliqua. Ut enim minim veniam exercitation laboris ut siad consequat siad minim enum esqudiat dolore.
									</div>
									<div class="margin-b-20">
										Lorem ipsum dolor sit amet consectetur adipiscing elit sed tempor incididunt ut laboret tempor incididunt dolore magna consequat siad minim aliqua.
									</div>
									<p><span class="fweight-700 color-link">Joh Milner</span>, Metronic Customer</p>
								</blockquote>
							</div>
							<div class="swiper-slide">
								<blockquote class="blockquote">
									<div class="margin-b-20">
										Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
									</div>
									<div class="margin-b-20">
										Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
									</div>
									<p><span class="fweight-700 color-link">Alex Clarson</span>, Metronic Customer</p>
								</blockquote>
							</div>
						</div>
						<!-- End Swiper Wrapper -->

						<!-- Pagination -->
<!--<div class="swiper-testimonials-pagination"></div>
					</div>
					<!-- End Swiper Testimonials -->
			  <!--  </div>
			</div>
			<!--// end row -->
	 <!--   </div>-->
		<!-- End Testimonials -->

		<!-- Clients -->
		<!--<div class="bg-color-sky-light">
			<div class="content-lg container">
				<!-- Swiper Clients -->
			  <!--  <div class="swiper-slider swiper-clients">
					<!-- Swiper Wrapper -->
				  <!--  <div class="swiper-wrapper">
						<div class="swiper-slide">
							<img class="swiper-clients-img" src="/img/clients/01.png" alt="Clients Logo">
						</div>
						<div class="swiper-slide">
							<img class="swiper-clients-img" src="/img/clients/02.png" alt="Clients Logo">
						</div>
						<div class="swiper-slide">
							<img class="swiper-clients-img" src="/img/clients/03.png" alt="Clients Logo">
						</div>
						<div class="swiper-slide">
							<img class="swiper-clients-img" src="/img/clients/04.png" alt="Clients Logo">
						</div>
						<div class="swiper-slide">
							<img class="swiper-clients-img" src="/img/clients/05.png" alt="Clients Logo">
						</div>
						<div class="swiper-slide">
							<img class="swiper-clients-img" src="/img/clients/06.png" alt="Clients Logo">
						</div>
					</div>
					<!-- End Swiper Wrapper -->
			   <!-- </div>
				<!-- End Swiper Clients -->
		   <!-- </div>
		</div>
		<!-- End Clients -->
		<!--========== END PAGE LAYOUT ==========-->

		<!--========== FOOTER ==========-->
	   <footer class="footer">
			<!-- Links -->
			<div class="footer-seperator">
				<div class="content-lg container">
					<div class="row">
						<div class="col-sm-2 sm-margin-b-50">
							<!-- List -->
					   <!--     <ul class="list-unstyled footer-list">
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
					   <!-- </div>
						<div class="col-sm-4 sm-margin-b-30">
							<!-- List -->
						  <!--  <ul class="list-unstyled footer-list">
								<li class="footer-list-item"><a class="footer-list-link" href="#">Twitter</a></li>
								<li class="footer-list-item"><a class="footer-list-link" href="#">Facebook</a></li>
								<li class="footer-list-item"><a class="footer-list-link" href="#">Instagram</a></li>
								<li class="footer-list-item"><a class="footer-list-link" href="#">YouTube</a></li>
							</ul>
							<!-- End List -->
						</div>
					    <div class="col-sm-5 sm-margin-b-30">
						</div>
						
					</div>
					<!--// end row -->
			<!--    </div>
			</div> -->
			<!-- End Links -->

			<!-- Copyright -->
			<!--<div class="content container">
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
		<script src="/vendor/swiper/js/swiper.jquery.min.js" type="text/javascript"></script>

		<!-- PAGE LEVEL SCRIPTS -->
		<script src="/js/layout.min.js" type="text/javascript"></script>
		<script src="/js/components/wow.min.js" type="text/javascript"></script>
		<script src="/js/components/swiper.min.js" type="text/javascript"></script>

	</body>
	<!-- END BODY -->
</html>""")
