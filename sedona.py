<!DOCTYPE html>
<html lang="tg">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>SEDONA CAKE — Қаннодии шумо</title>

<!-- Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>

:root{
    --brown:#3b2118;
    --brown2:#5b3527;
    --coffee:#754936;
    --cream:#fff8ee;
    --cream2:#f5e6d2;
    --gold:#d6a15c;
    --white:#ffffff;
    --text:#35231d;
}

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    scroll-behavior:smooth;
}

body{
    font-family:'Montserrat',sans-serif;
    color:var(--text);
    background:var(--cream);
}

/* ================= HEADER ================= */

header{
    position:fixed;
    top:0;
    left:0;
    width:100%;
    z-index:1000;
    background:rgba(59,33,24,.94);
    backdrop-filter:blur(12px);
    border-bottom:1px solid rgba(255,255,255,.1);
}

.navbar{
    max-width:1200px;
    margin:auto;
    height:76px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:0 25px;
}

.logo{
    display:flex;
    align-items:center;
    gap:12px;
    color:white;
    text-decoration:none;
}

.logo-circle{
    width:48px;
    height:48px;
    border:2px solid var(--gold);
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:22px;
    background:#281610;
}

.logo-text{
    font-family:'Cormorant Garamond',serif;
    font-size:29px;
    font-weight:700;
    letter-spacing:2px;
}

.nav-links{
    display:flex;
    gap:28px;
    list-style:none;
}

.nav-links a{
    color:#fff;
    text-decoration:none;
    font-size:14px;
    font-weight:500;
    transition:.3s;
}

.nav-links a:hover{
    color:var(--gold);
}

.menu-btn{
    display:none;
    color:white;
    font-size:28px;
    cursor:pointer;
}

/* ================= HERO ================= */

.hero{
    min-height:100vh;
    display:flex;
    align-items:center;
    position:relative;
    overflow:hidden;

    background:
    linear-gradient(90deg,rgba(45,23,16,.93),rgba(45,23,16,.55),rgba(45,23,16,.25)),
    url("https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=1800&q=85");

    background-size:cover;
    background-position:center;
}

.hero::after{
    content:"";
    position:absolute;
    inset:0;
    background:
    radial-gradient(circle at 75% 50%,rgba(214,161,92,.18),transparent 35%);
}

.hero-content{
    position:relative;
    z-index:2;
    max-width:1200px;
    width:100%;
    margin:auto;
    padding:130px 25px 80px;
}

.small-title{
    color:var(--gold);
    font-size:14px;
    letter-spacing:5px;
    text-transform:uppercase;
    margin-bottom:20px;
}

.hero h1{
    color:white;
    font-family:'Cormorant Garamond',serif;
    font-size:clamp(65px,9vw,125px);
    line-height:.82;
    max-width:750px;
    font-weight:600;
}

.hero h1 span{
    color:var(--gold);
    font-style:italic;
}

.hero p{
    color:#f3e7dc;
    max-width:570px;
    line-height:1.8;
    margin:30px 0;
    font-size:16px;
}

.buttons{
    display:flex;
    gap:14px;
    flex-wrap:wrap;
}

.btn{
    padding:15px 26px;
    border-radius:50px;
    text-decoration:none;
    font-weight:600;
    display:inline-flex;
    align-items:center;
    gap:8px;
    transition:.3s;
}

.btn-main{
    color:#3a2118;
    background:var(--gold);
}

.btn-main:hover{
    transform:translateY(-4px);
    box-shadow:0 12px 30px rgba(214,161,92,.25);
}

.btn-outline{
    border:1px solid rgba(255,255,255,.5);
    color:white;
}

.btn-outline:hover{
    background:white;
    color:var(--brown);
}

.hero-badge{
    position:absolute;
    right:8%;
    bottom:12%;
    z-index:3;
    width:150px;
    height:150px;
    border-radius:50%;
    border:1px solid var(--gold);
    background:rgba(45,23,16,.7);
    backdrop-filter:blur(8px);
    color:white;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    text-align:center;
}

.hero-badge strong{
    font-family:'Cormorant Garamond',serif;
    font-size:38px;
    color:var(--gold);
}

.hero-badge span{
    font-size:11px;
}

/* ================= SECTION ================= */

section{
    padding:100px 20px;
}

.container{
    max-width:1200px;
    margin:auto;
}

.section-heading{
    text-align:center;
    margin-bottom:55px;
}

.section-heading small{
    color:var(--coffee);
    text-transform:uppercase;
    letter-spacing:4px;
    font-size:12px;
    font-weight:700;
}

.section-heading h2{
    font-family:'Cormorant Garamond',serif;
    font-size:60px;
    color:var(--brown);
    margin-top:8px;
}

.section-heading p{
    max-width:600px;
    margin:10px auto 0;
    color:#806c61;
    line-height:1.7;
}

/* ================= CATEGORIES ================= */

.categories{
    background:#f9ecdc;
}

.category-grid{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:20px;
}

.category{
    min-height:220px;
    border-radius:20px;
    overflow:hidden;
    position:relative;
    background-size:cover;
    background-position:center;
    cursor:pointer;
    transition:.4s;
}

.category:hover{
    transform:translateY(-8px);
}

.category::before{
    content:"";
    position:absolute;
    inset:0;
    background:linear-gradient(transparent,rgba(40,20,14,.9));
}

.category-content{
    position:absolute;
    bottom:20px;
    left:22px;
    color:white;
}

.category-content h3{
    font-family:'Cormorant Garamond',serif;
    font-size:31px;
}

.category-content p{
    font-size:12px;
    color:#ead7c7;
}

/* ================= PRODUCTS ================= */

.products{
    background:#fffaf3;
}

.product-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:28px;
}

.product-card{
    background:white;
    border-radius:22px;
    overflow:hidden;
    box-shadow:0 12px 35px rgba(75,40,25,.09);
    transition:.4s;
    border:1px solid #f0dfcc;
}

.product-card:hover{
    transform:translateY(-9px);
    box-shadow:0 20px 45px rgba(75,40,25,.16);
}

.product-image{
    height:280px;
    position:relative;
    overflow:hidden;
}

.product-image img{
    width:100%;
    height:100%;
    object-fit:cover;
    transition:.5s;
}

.product-card:hover img{
    transform:scale(1.07);
}

.tag{
    position:absolute;
    top:16px;
    left:16px;
    padding:7px 13px;
    border-radius:30px;
    background:rgba(59,33,24,.9);
    color:white;
    font-size:11px;
}

.product-info{
    padding:22px;
}

.product-info h3{
    font-family:'Cormorant Garamond',serif;
    font-size:30px;
    color:var(--brown);
}

.product-info p{
    color:#8a756a;
    font-size:13px;
    line-height:1.6;
    margin:7px 0 18px;
}

.product-bottom{
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.price{
    color:var(--coffee);
    font-weight:700;
    font-size:16px;
}

.order-btn{
    border:0;
    background:var(--brown);
    color:white;
    padding:10px 17px;
    border-radius:30px;
    cursor:pointer;
    text-decoration:none;
    font-size:12px;
    transition:.3s;
}

.order-btn:hover{
    background:var(--gold);
    color:var(--brown);
}

/* ================= SAMBUSA ================= */

.sambusa-section{
    background:var(--brown);
    color:white;
}

.sambusa-wrapper{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:60px;
    align-items:center;
}

.sambusa-image{
    height:520px;
    border-radius:30px;
    background:
    linear-gradient(rgba(59,33,24,.1),rgba(59,33,24,.25)),
    url("https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=1000&q=85");
    background-size:cover;
    background-position:center;
    box-shadow:0 25px 70px rgba(0,0,0,.3);
}

.sambusa-text small{
    color:var(--gold);
    letter-spacing:4px;
}

.sambusa-text h2{
    font-family:'Cormorant Garamond',serif;
    font-size:68px;
    line-height:.9;
    margin:15px 0 25px;
}

.sambusa-text p{
    color:#d9c8bd;
    line-height:1.8;
    max-width:500px;
}

.sambusa-price{
    font-size:25px;
    color:var(--gold);
    margin:25px 0;
    font-weight:700;
}

/* ================= HOT DOG ================= */

.hotdog-section{
    background:#f5e7d5;
}

.hotdog-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:25px;
}

.hotdog-card{
    background:white;
    padding:12px;
    border-radius:20px;
    box-shadow:0 10px 35px rgba(80,40,20,.1);
}

.hotdog-card img{
    width:100%;
    height:230px;
    object-fit:cover;
    border-radius:14px;
}

.hotdog-card h3{
    padding:16px 8px 4px;
    font-family:'Cormorant Garamond',serif;
    font-size:28px;
}

.hotdog-card p{
    padding:0 8px 15px;
    color:#806b60;
    font-size:13px;
}

/* ================= ABOUT ================= */

.about{
    background:#fffaf4;
}

.about-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:70px;
    align-items:center;
}

.about-image{
    height:500px;
    border-radius:30px;
    background:
    url("https://images.unsplash.com/photo-1551024601-bec78aea704b?auto=format&fit=crop&w=1000&q=85");
    background-size:cover;
    background-position:center;
}

.about-text small{
    color:var(--coffee);
    letter-spacing:4px;
}

.about-text h2{
    font-family:'Cormorant Garamond',serif;
    color:var(--brown);
    font-size:65px;
    line-height:.95;
    margin:15px 0 25px;
}

.about-text p{
    color:#756159;
    line-height:1.9;
    margin-bottom:20px;
}

.features{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:15px;
    margin-top:25px;
}

.feature{
    padding:17px;
    background:#f7eadb;
    border-radius:14px;
}

.feature strong{
    color:var(--brown);
}

.feature span{
    display:block;
    color:#806d63;
    font-size:12px;
    margin-top:5px;
}

/* ================= MENU ================= */

.menu-section{
    background:#3b2118;
}

.menu-box{
    max-width:900px;
    margin:auto;
    border:1px solid rgba(214,161,92,.45);
    padding:50px;
    border-radius:30px;
    background:rgba(255,255,255,.03);
}

.menu-title{
    text-align:center;
    color:white;
    font-family:'Cormorant Garamond',serif;
    font-size:55px;
    margin-bottom:35px;
}

.menu-row{
    display:flex;
    justify-content:space-between;
    gap:20px;
    padding:20px 0;
    border-bottom:1px dashed rgba(255,255,255,.2);
}

.menu-row:last-child{
    border-bottom:0;
}

.menu-row h3{
    color:white;
    font-family:'Cormorant Garamond',serif;
    font-size:25px;
}

.menu-row p{
    color:#bfaea3;
    font-size:12px;
    margin-top:5px;
}

.menu-price{
    color:var(--gold);
    font-weight:700;
    white-space:nowrap;
}

/* ================= CONTACT ================= */

.contact{
    background:
    linear-gradient(rgba(247,234,219,.94),rgba(247,234,219,.94)),
    url("https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1800&q=85");
    background-size:cover;
}

.contact-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:30px;
}

.contact-card{
    background:white;
    padding:35px;
    border-radius:25px;
    box-shadow:0 10px 35px rgba(70,40,20,.08);
}

.contact-card h3{
    font-family:'Cormorant Garamond',serif;
    font-size:38px;
    color:var(--brown);
    margin-bottom:20px;
}

.contact-item{
    display:flex;
    gap:15px;
    margin:20px 0;
    align-items:flex-start;
}

.contact-icon{
    width:45px;
    height:45px;
    min-width:45px;
    border-radius:50%;
    background:#f2dfca;
    display:flex;
    align-items:center;
    justify-content:center;
}

.contact-item strong{
    display:block;
    color:var(--brown);
    margin-bottom:4px;
}

.contact-item span{
    color:#806d63;
    font-size:13px;
}

.map-box{
    min-height:100%;
    border-radius:25px;
    background:
    linear-gradient(rgba(59,33,24,.72),rgba(59,33,24,.72)),
    url("https://images.unsplash.com/photo-1515003197210-e0cd71810b5f?auto=format&fit=crop&w=1000&q=85");
    background-size:cover;
    background-position:center;
    display:flex;
    align-items:center;
    justify-content:center;
    text-align:center;
    color:white;
    padding:30px;
}

.map-box h3{
    font-family:'Cormorant Garamond',serif;
    font-size:45px;
}

.map-box p{
    color:#ead7c8;
    margin:15px 0 25px;
}

/* ================= FOOTER ================= */

footer{
    background:#24130e;
    color:#cdbbb0;
    text-align:center;
    padding:45px 20px;
}

.footer-logo{
    font-family:'Cormorant Garamond',serif;
    color:white;
    font-size:38px;
    letter-spacing:3px;
}

footer p{
    margin:8px 0;
    font-size:13px;
}

.social{
    margin:20px 0;
}

.social a{
    color:var(--gold);
    text-decoration:none;
    margin:0 8px;
}

/* ================= WHATSAPP ================= */

.whatsapp{
    position:fixed;
    right:22px;
    bottom:22px;
    z-index:999;
    width:60px;
    height:60px;
    border-radius:50%;
    background:#25D366;
    color:white;
    display:flex;
    align-items:center;
    justify-content:center;
    text-decoration:none;
    font-size:29px;
    box-shadow:0 10px 30px rgba(37,211,102,.35);
    animation:pulse 2s infinite;
}

@keyframes pulse{
    0%{box-shadow:0 0 0 0 rgba(37,211,102,.5)}
    70%{box-shadow:0 0 0 15px rgba(37,211,102,0)}
    100%{box-shadow:0 0 0 0 rgba(37,211,102,0)}
}

/* ================= MODAL ================= */

.modal{
    position:fixed;
    inset:0;
    background:rgba(20,10,5,.8);
    backdrop-filter:blur(8px);
    display:none;
    align-items:center;
    justify-content:center;
    z-index:3000;
    padding:20px;
}

.modal.active{
    display:flex;
}

.modal-box{
    background:#fffaf3;
    max-width:500px;
    width:100%;
    border-radius:25px;
    padding:35px;
    position:relative;
}

.close{
    position:absolute;
    right:20px;
    top:15px;
    font-size:30px;
    cursor:pointer;
    color:var(--brown);
}

.modal-box h2{
    font-family:'Cormorant Garamond',serif;
    font-size:40px;
    color:var(--brown);
}

.modal-box p{
    margin:12px 0 25px;
    color:#806d63;
}

.order-link{
    display:block;
    text-align:center;
    background:#25D366;
    color:white;
    padding:15px;
    border-radius:40px;
    text-decoration:none;
    font-weight:600;
}

/* ================= MOBILE ================= */

@media(max-width:900px){

    .nav-links{
        position:absolute;
        top:76px;
        left:0;
        width:100%;
        background:#3b2118;
        flex-direction:column;
        padding:25px;
        display:none;
    }

    .nav-links.active{
        display:flex;
    }

    .menu-btn{
        display:block;
    }

    .hero-badge{
        display:none;
    }

    .category-grid{
        grid-template-columns:1fr 1fr;
    }

    .product-grid{
        grid-template-columns:1fr 1fr;
    }

    .sambusa-wrapper,
    .about-grid,
    .contact-grid{
        grid-template-columns:1fr;
    }

    .hotdog-grid{
        grid-template-columns:1fr 1fr;
    }
}

@media(max-width:600px){

    section{
        padding:75px 15px;
    }

    .logo-text{
        font-size:23px;
    }

    .hero h1{
        font-size:67px;
    }

    .hero-content{
        padding-top:150px;
    }

    .section-heading h2{
        font-size:47px;
    }

    .category-grid,
    .product-grid,
    .hotdog-grid{
        grid-template-columns:1fr;
    }

    .category{
        min-height:250px;
    }

    .sambusa-image{
        height:380px;
    }

    .sambusa-text h2,
    .about-text h2{
        font-size:52px;
    }

    .menu-box{
        padding:25px;
    }

    .menu-title{
        font-size:45px;
    }

    .menu-row h3{
        font-size:21px;
    }

    .about-image{
        height:380px;
    }
}

</style>
</head>

<body>

<!-- ================= HEADER ================= -->

<header>

<nav class="navbar">

<a href="#home" class="logo">
    <div class="logo-circle">🍰</div>
    <div class="logo-text">SEDONA</div>
</a>

<ul class="nav-links" id="navLinks">
    <li><a href="#home">Асосӣ</a></li>
    <li><a href="#catalog">Каталог</a></li>
    <li><a href="#sambusa">Самбуса</a></li>
    <li><a href="#menu">Меню</a></li>
    <li><a href="#about">Дар бораи мо</a></li>
    <li><a href="#contact">Тамос</a></li>
</ul>

<div class="menu-btn" onclick="toggleMenu()">☰</div>

</nav>

</header>


<!-- ================= HERO ================= -->

<section class="hero" id="home">

<div class="hero-content">

<div class="small-title">
    Қаннодии SEDONA · Душанбе
</div>

<h1>
    Лаззате,<br>
    ки <span>дар хотир</span><br>
    мемонад.
</h1>

<p>
    Тортҳои зебо, шириниҳои болаззат ва самбусаи гарм —
    бо муҳаббат барои лаҳзаҳои ширини шумо тайёр мекунем.
</p>

<div class="buttons">

<a href="#catalog" class="btn btn-main">
    🍰 Каталогро дидан
</a>

<a href="https://wa.me/992104143449" class="btn btn-outline" target="_blank">
    💬 WhatsApp
</a>

</div>

</div>

<div class="hero-badge">
    <strong>85</strong>
    <span>СОМОНӢ<br>1 КГ ТОРТ</span>
</div>

</section>


<!-- ================= CATEGORIES ================= -->

<section class="categories">

<div class="container">

<div class="section-heading">

<small>Интихоби шумо</small>

<h2>Аз менюи мо</h2>

<p>
Ҳар чизе барои як рӯзи ширин ва хотирмон.
</p>

</div>


<div class="category-grid">

<div class="category"
style="background-image:url('https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=800&q=80')">

<div class="category-content">
<h3>Тортҳо</h3>
<p>Тортҳои зебо барои ҳар ҷашн</p>
</div>

</div>


<div class="category"
style="background-image:url('https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=800&q=80')">

<div class="category-content">
<h3>Самбуса</h3>
<p>Гарм ва болаззат</p>
</div>

</div>


<div class="category"
style="background-image:url('https://images.unsplash.com/photo-1612392062631-94dd858cba88?auto=format&fit=crop&w=800&q=80')">

<div class="category-content">
<h3>Хот-Дог</h3>
<p>Барои газаки болаззат</p>
</div>

</div>


<div class="category"
style="background-image:url('https://images.unsplash.com/photo-1551024506-0bccd828d307?auto=format&fit=crop&w=800&q=80')">

<div class="category-content">
<h3>Шириниҳо</h3>
<p>Печенье ва шириниҳои махсус</p>
</div>

</div>

</div>

</div>

</section>


<!-- ================= CAKES ================= -->

<section class="products" id="catalog">

<div class="container">

<div class="section-heading">

<small>SEDONA CAKE</small>

<h2>Каталоги тортҳо</h2>

<p>
Тортҳои мо барои рӯзи таваллуд, тӯй, меҳмонӣ ва ҳар як лаҳзаи зебо.
</p>

</div>


<div class="product-grid">


<!-- CAKE 1 -->

<div class="product-card">

<div class="product-image">

<img src="https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=900&q=85">

<div class="tag">Машҳур ⭐</div>

</div>

<div class="product-info">

<h3>Chocolate Cake</h3>

<p>
Торти шоколадӣ бо креми мулоим ва таъми бой.
</p>

<div class="product-bottom">

<div class="price">85 сомонӣ / 1 кг</div>

<a href="javascript:void(0)" onclick="openOrder('Chocolate Cake')" class="order-btn">
Заказать
</a>

</div>

</div>

</div>


<!-- CAKE 2 -->

<div class="product-card">

<div class="product-image">

<img src="https://images.unsplash.com/photo-1565958011703-44f9829ba187?auto=format&fit=crop&w=900&q=85">

<div class="tag">SEDONA</div>

</div>

<div class="product-info">

<h3>Berry Cake</h3>

<p>
Торти сабук бо меваҳои тару тоза ва крем.
</p>

<div class="product-bottom">

<div class="price">85 сомонӣ / 1 кг</div>

<a href="javascript:void(0)" onclick="openOrder('Berry Cake')" class="order-btn">
Заказать
</a>

</div>

</div>

</div>


<!-- CAKE 3 -->

<div class="product-card">

<div class="product-image">

<img src="https://images.unsplash.com/photo-1586788224331-947f68671cf1?auto=format&fit=crop&w=900&q=85">

<div class="tag">Нав ✨</div>

</div>

<div class="product-info">

<h3>Red Velvet</h3>

<p>
Red Velvet-и мулоим бо креми сафеди хуштаъм.
</p>

<div class="product-bottom">

<div class="price">85 сомонӣ / 1 кг</div>

<a href="javascript:void(0)" onclick="openOrder('Red Velvet')" class="order-btn">
Заказать
</a>

</div>

</div>

</div>


<!-- CAKE 4 -->

<div class="product-card">

<div class="product-image">

<img src="https://images.unsplash.com/photo-1602351447937-745cb720612f?auto=format&fit=crop&w=900&q=85">

</div>

<div class="product-info">

<h3>Strawberry Cake</h3>

<p>
Торти тарбузагӣ бо крем ва меваҳои тару тоза.
</p>

<div class="product-bottom">

<div class="price">85 сомонӣ / 1 кг</div>

<a href="javascript:void(0)" onclick="openOrder('Strawberry Cake')" class="order-btn">
Заказать
</a>

</div>

</div>

</div>


<!-- CAKE 5 -->

<div class="product-card">

<div class="product-image">

<img src="https://images.unsplash.com/photo-1571115177098-24ec42ed204d?auto=format&fit=crop&w=900&q=85">

</div>

<div class="product-info">

<h3>Vanilla Cake</h3>

<p>
Торти классикии ванилӣ бо креми нозук.
</p>

<div class="product-bottom">

<div class="price">85 сомонӣ / 1 кг</div>

<a href="javascript:void(0)" onclick="openOrder('Vanilla Cake')" class="order-btn">
Заказать
</a>

</div>

</div>

</div>


<!-- CAKE 6 -->

<div class="product-card">

<div class="product-image">

<img src="https://images.unsplash.com/photo-1551024601-bec78aea704b?auto=format&fit=crop&w=900&q=85">

</div>

<div class="product-info">

<h3>Premium Cake</h3>

<p>
Тарҳи махсус барои ҷашнҳои махсус.
</p>

<div class="product-bottom">

<div class="price">85 сомонӣ / 1 кг</div>

<a href="javascript:void(0)" onclick="openOrder('Premium Cake')" class="order-btn">
Заказать
</a>

</div>

</div>

</div>

</div>

</div>

</section>


<!-- ================= SAMBUSA ================= -->

<section class="sambusa-section" id="sambusa">

<div class="container">

<div class="sambusa-wrapper">

<div class="sambusa-image"></div>

<div class="sambusa-text">

<small>Гарм · Тоза · Болаззат</small>

<h2>
Самбусаи<br>
SEDONA
</h2>

<p>
Самбусаҳои болаззат барои меҳмонӣ, ид ва ҳар рӯзи оддӣ.
Бо фармоиш барои шумо омода карда мешаванд.
</p>

<div class="sambusa-price">
Пот заказ · Фармоиш
</div>

<a href="https://wa.me/992104143449?text=Салом%2C%20ман%20мехоҳам%20самбуса%20фармоиш%20диҳам"
class="btn btn-main"
target="_blank">
💬 Фармоиш додан
</a>

</div>

</div>

</div>

</section>


<!-- ================= HOT DOG ================= -->

<section class="hotdog-section">

<div class="container">

<div class="section-heading">

<small>FAST FOOD</small>

<h2>Хот-Дог & Газаки гарм</h2>

<p>
Барои онҳое, ки таъми болаззатро зуд дӯст медоранд.
</p>

</div>


<div class="hotdog-grid">

<div class="hotdog-card">

<img src="https://images.unsplash.com/photo-1612392062631-94dd858cba88?auto=format&fit=crop&w=900&q=85">

<h3>Classic Hot-Dog</h3>

<p>Хот-доги классикӣ бо соус ва сабзавоти тару тоза.</p>

</div>


<div class="hotdog-card">

<img src="https://images.unsplash.com/photo-1619740455993-9e612b1af08a?auto=format&fit=crop&w=900&q=85">

<h3>Special Hot-Dog</h3>

<p>Хот-доги махсуси SEDONA барои таъми дигар.</p>

</div>


<div class="hotdog-card">

<img src="https://images.unsplash.com/photo-1627054240313-8f2e2d2f1f5b?auto=format&fit=crop&w=900&q=85">

<h3>SEDONA Snack</h3>

<p>Интихоби хуб барои меҳмонӣ ва вохӯрӣ.</p>

</div>

</div>

</div>

</section>


<!-- ================= ABOUT ================= -->

<section class="about" id="about">

<div class="container">

<div class="about-grid">

<div class="about-image"></div>

<div class="about-text">

<small>ДАР БОРАИ SEDONA</small>

<h2>
Шириние,<br>
ки бо муҳаббат
тайёр мешавад.
</h2>

<p>
SEDONA — як гӯшаи шириниҳои дӯстдоштаи шумост.
Мо тортҳо, шириниҳо ва маҳсулоти болаззатро
бо диққат ба намуди зоҳирӣ ва таъм омода мекунем.
</p>

<p>
Барои рӯзи таваллуд, тӯй, меҳмонӣ ё танҳо барои
хуш кардани рӯзи худ — мо ҳамеша омодаем.
</p>


<div class="features">

<div class="feature">
<strong>🍰 Тортҳо</strong>
<span>Аз 85 сомонӣ / 1 кг</span>
</div>

<div class="feature">
<strong>🥟 Самбуса</strong>
<span>Бо фармоиш</span>
</div>

<div class="feature">
<strong>🚚 Доставка</strong>
<span>Фармоиш қабул мекунем</span>
</div>

<div class="feature">
<strong>💝 Муҳаббат</strong>
<span>Дар ҳар маҳсулот</span>
</div>

</div>

</div>

</div>

</div>

</section>


<!-- ================= MENU ================= -->

<section class="menu-section" id="menu">

<div class="container">

<div class="menu-box">

<div class="menu-title">
Менюи SEDONA
</div>


<div class="menu-row">

<div>
<h3>Тортҳои SEDONA</h3>
<p>Шоколадӣ · Red Velvet · Мевагӣ · Ванилӣ</p>
</div>

<div class="menu-price">
85 сомонӣ / кг
</div>

</div>


<div class="menu-row">

<div>
<h3>Самбуса</h3>
<p>Гарм · Болаззат · Барои фармоиш</p>
</div>

<div class="menu-price">
Пот заказ
</div>

</div>


<div class="menu-row">

<div>
<h3>Хот-Дог</h3>
<p>Classic · Special · SEDONA</p>
</div>

<div class="menu-price">
Пот заказ
</div>

</div>


<div class="menu-row">

<div>
<h3>Шириниҳо</h3>
<p>Печенье · Десерт · Шириниҳои махсус</p>
</div>

<div class="menu-price">
Пот заказ
</div>

</div>


<div class="menu-row">

<div>
<h3>Доставка</h3>
<p>Фармоишро тавассути WhatsApp қабул мекунем</p>
</div>

<div class="menu-price">
WhatsApp
</div>

</div>

</div>

</div>

</section>


<!-- ================= CONTACT ================= -->

<section class="contact" id="contact">

<div class="container">

<div class="section-heading">

<small>Биёед шинос шавем</small>

<h2>Тамос бо мо</h2>

<p>
Барои фармоиш ба мо занг занед ё дар WhatsApp нависед.
</p>

</div>


<div class="contact-grid">


<div class="contact-card">

<h3>SEDONA CAKE</h3>


<div class="contact-item">

<div class="contact-icon">📍</div>

<div>
<strong>Адрес</strong>
<span>Душанбе, 112 мкр</span>
</div>

</div>


<div class="contact-item">

<div class="contact-icon">📞</div>

<div>
<strong>Телефон</strong>
<span>+992 104 143 449</span>
</div>

</div>


<div class="contact-item">

<div class="contact-icon">💬</div>

<div>
<strong>WhatsApp</strong>
<span>+992 104 143 449</span>
</div>

</div>


<div class="contact-item">

<div class="contact-icon">🍰</div>

<div>
<strong>Фармоиши торт</strong>
<span>85 сомонӣ барои 1 кг</span>
</div>

</div>


<a href="https://wa.me/992104143449"
target="_blank"
class="btn btn-main">
💬 Навиштан дар WhatsApp
</a>

</div>


<div class="map-box">

<div>

<h3>Мо шуморо интизорем 🤎</h3>

<p>
Душанбе · 112 мкр
</p>

<a href="https://www.google.com/maps/search/?api=1&query=Dushanbe+112+microdistrict"
target="_blank"
class="btn btn-main">
📍 Кушодани харита
</a>

</div>

</div>


</div>

</div>

</section>


<!-- ================= FOOTER ================= -->

<footer>

<div class="footer-logo">
SEDONA
</div>

<p>
Қаннодии шумо · Душанбе
</p>

<div class="social">

<a href="https://wa.me/992104143449" target="_blank">
WhatsApp
</a>

<a href="tel:+992104143449">
Телефон
</a>

</div>

<p>
© 2026 SEDONA CAKE. Ҳамаи ҳуқуқҳо ҳифз шудаанд.
</p>

</footer>


<!-- ================= WHATSAPP FLOAT ================= -->

<a href="https://wa.me/992104143449?text=Салом%2C%20ман%20мехоҳам%20фармоиш%20диҳам"
class="whatsapp"
target="_blank"
title="WhatsApp">
💬
</a>


<!-- ================= ORDER MODAL ================= -->

<div class="modal" id="orderModal">

<div class="modal-box">

<div class="close" onclick="closeOrder()">×</div>

<h2 id="orderTitle">
Фармоиш
</h2>

<p>
Барои фармоиши маҳсулот ба WhatsApp нависед.
Мо тафсилоти фармоишро бо шумо мувофиқа мекунем.
</p>

<a id="orderLink"
href="#"
target="_blank"
class="order-link">
💬 Фармоиш додан дар WhatsApp
</a>

</div>

</div>


<script>

/* MOBILE MENU */

function toggleMenu(){

    document
    .getElementById("navLinks")
    .classList.toggle("active");

}


/* ORDER MODAL */

function openOrder(product){

    const modal =
    document.getElementById("orderModal");

    const title =
    document.getElementById("orderTitle");

    const link =
    document.getElementById("orderLink");

    title.innerHTML =
    "Фармоиш: " + product;

    const message =
    "Салом, ман мехоҳам " +
    product +
    " фармоиш диҳам.";

    link.href =
    "https://wa.me/992104143449?text=" +
    encodeURIComponent(message);

    modal.classList.add("active");

}


function closeOrder(){

    document
    .getElementById("orderModal")
    .classList.remove("active");

}


/* CLOSE MODAL BY CLICKING OUTSIDE */

document
.getElementById("orderModal")
.addEventListener("click",function(e){

    if(e.target === this){
        closeOrder();
    }

});


/* CLOSE MOBILE MENU AFTER CLICK */

document
.querySelectorAll(".nav-links a")
.forEach(function(link){

    link.addEventListener("click",function(){

        document
        .getElementById("navLinks")
        .classList.remove("active");

    });

});


/* SCROLL EFFECT */

window.addEventListener("scroll",function(){

    const header =
    document.querySelector("header");

    if(window.scrollY > 50){

        header.style.boxShadow =
        "0 10px 35px rgba(0,0,0,.25)";

    }else{

        header.style.boxShadow = "none";

    }

});

</script>

</body>
</html>
