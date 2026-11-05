
from pathlib import Path
import base64
import html
import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# CONFIGURACIÓN
# ============================================================

BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"

CORREO = ""  # Agrega tu correo
WHATSAPP = ""  # Número con código de país, si lo necesitas

st.set_page_config(
    page_title="Nexo | Soluciones Comerciales",
    page_icon="🔵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# FUNCIONES
# ============================================================

def imagen_base64(nombre):
    ruta = ASSETS / nombre

    if not ruta.exists():
        return ""

    extension = ruta.suffix.lower().replace(".", "")
    mime = "image/svg+xml" if extension == "svg" else f"image/{extension}"

    with open(ruta, "rb") as archivo:
        contenido = base64.b64encode(archivo.read()).decode()

    return f"data:{mime};base64,{contenido}"


def bloque_imagen(nombre, alt="Imagen de proyecto"):
    imagen = imagen_base64(nombre)

    if imagen:
        return f'<img src="{imagen}" alt="{html.escape(alt)}">'

    return f"""
    <div class="image-placeholder">
        <span>IMAGEN PENDIENTE</span>
        <small>{html.escape(nombre)}</small>
    </div>
    """


def cargar_logo(nombre, clase="logo-img", alt="Nexo"):
    imagen = imagen_base64(nombre)

    if imagen:
        return f'<img src="{imagen}" class="{clase}" alt="{html.escape(alt)}">'

    return '<span class="logo-text">NEXO<span>.</span></span>'


def carrusel_imagenes(imagenes, alt):
    slides = []

    for nombre in imagenes:
        slides.append(
            f"""
            <div class="carousel-slide">
                {bloque_imagen(nombre, alt)}
            </div>
            """
        )

    return f"""
    <div class="carousel" data-carousel>
        <div class="carousel-track">
            {''.join(slides)}
        </div>
        <div class="carousel-overlay"></div>
        <div class="carousel-controls">
            <button class="carousel-prev" aria-label="Anterior">←</button>
            <div class="carousel-dots"></div>
            <button class="carousel-next" aria-label="Siguiente">→</button>
        </div>
    </div>
    """


# ============================================================
# LOGOTIPOS
# ============================================================

logo_nexo = cargar_logo(
    "nexo-horizontal.svg",
    "logo-img",
    "Nexo Comercial"
)

logo_amh = cargar_logo(
    "logo-hepatologia.svg",
    "client-logo amh-logo",
    "AMH"
)

logo_roothua = cargar_logo(
    "roothua_logo.svg",
    "client-logo roothua-logo",
    "Roothúa"
)

# ============================================================
# IMÁGENES DE PROYECTOS
# ============================================================

amh_images = [
    "amh-entrega-01.jpg",
    "amh-planeacion.jpg",
    "amh-tazas.jpg",
    "amh-rollup.jpg",
    "amh-gafetes.jpg",
    "amh-muro-3x3.jpg",
]

roothua_images = [
    "roothua-proyecto.jpg",
    "roothua-redes.jpg",
    "roothua-publicaciones.jpg",
    "roothua-contenido.jpg",
    "roothua-muebles.jpg",
    "roothua-procesos.jpg",
]

# ============================================================
# HTML
# ============================================================

pagina = r"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --blue: #087BFF;
    --blue-dark: #075EAD;
    --black: #08090B;
    --gray: #A4A8B0;
    --white: #F7F8FA;
    --border: rgba(255,255,255,.12);
    --nav-height: 82px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
    scroll-padding-top: calc(var(--nav-height) + 20px);
}

body {
    background: var(--black);
    color: var(--white);
    font-family: 'DM Sans', sans-serif;
    overflow-x: hidden;
    padding-top: var(--nav-height);
}

a {
    text-decoration: none;
    color: inherit;
}

button {
    font-family: inherit;
}

section {
    position: relative;
    padding: 105px 8%;
    scroll-margin-top: calc(var(--nav-height) + 20px);
}

.container {
    max-width: 1300px;
    margin: auto;
}

.eyebrow {
    color: var(--blue);
    font-size: 12px;
    letter-spacing: 3px;
    font-weight: 700;
    text-transform: uppercase;
    margin-bottom: 22px;
}

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif;
    letter-spacing: -1.5px;
}

h1 {
    font-size: clamp(48px, 7vw, 96px);
    line-height: .98;
    font-weight: 600;
}

h2 {
    font-size: clamp(36px, 5vw, 64px);
    line-height: 1.05;
}

h3 {
    font-size: 25px;
}

p {
    color: var(--gray);
    line-height: 1.8;
}

.blue {
    color: var(--blue);
}

.muted {
    color: var(--gray);
}

.btn {
    display: inline-flex;
    align-items: center;
    gap: 18px;
    padding: 16px 23px;
    background: var(--blue);
    color: white;
    border: 1px solid var(--blue);
    border-radius: 4px;
    font-size: 13px;
    font-weight: 600;
    transition: .3s;
    cursor: pointer;
}

.btn:hover {
    background: transparent;
    transform: translateY(-3px);
}

.btn-outline {
    background: transparent;
    border-color: var(--border);
}

.btn-outline:hover {
    background: var(--blue);
    border-color: var(--blue);
}

.tag {
    display: inline-block;
    padding: 8px 12px;
    border: 1px solid var(--border);
    border-radius: 30px;
    color: #C4C7CE;
    font-size: 11px;
    margin: 4px;
}

/* ============================================================
   CABECERA FIJA
============================================================ */

.nav {
    position: fixed;
    width: 100%;
    height: var(--nav-height);
    top: 0;
    left: 0;
    z-index: 1000;
    padding: 10px 7%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(8,9,11,.96);
    backdrop-filter: blur(18px);
    border-bottom: 1px solid rgba(255,255,255,.08);
}

.logo-img {
    width: 305px;
    max-height: 66px;
    object-fit: contain;
    display: block;
}

.logo-text {
    font-family: 'Space Grotesk';
    font-weight: 700;
    font-size: 32px;
}

.logo-text span {
    color: var(--blue);
}

.nav-links {
    display: flex;
    gap: 32px;
    align-items: center;
}

.nav-links a {
    font-size: 12px;
    color: #B5B8C0;
    transition: .2s;
}

.nav-links a:hover {
    color: white;
}

.nav-cta {
    background: var(--blue);
    color: white !important;
    padding: 13px 19px;
    border-radius: 3px;
}

/* ============================================================
   HERO / PORTADA COMPACTA
============================================================ */

.hero {
    min-height: 75vh;
    display: flex;
    align-items: center;
    padding-top: 65px;
    padding-bottom: 85px;
    overflow: hidden;
    background:
        radial-gradient(circle at 80% 35%, rgba(8,123,255,.17), transparent 35%),
        linear-gradient(180deg, #08090B, #0B0D12);
}

.hero-content {
    max-width: 1000px;
    position: relative;
    z-index: 2;
}

.hero h1 span {
    display: block;
}

.hero-description {
    max-width: 520px;
    margin: 22px 0;
    font-size: 16px;
}

.hero-buttons {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    margin-top: 25px;
}

.hero-bottom {
    position: absolute;
    bottom: 22px;
    left: 8%;
    right: 8%;
    display: flex;
    justify-content: space-between;
    color: #6D727C;
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* ============================================================
   MARQUEE
============================================================ */

.marquee {
    overflow: hidden;
    padding: 20px 0;
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    background: #0B0D12;
}

.marquee-track {
    display: flex;
    width: max-content;
    animation: marquee 28s linear infinite;
}

.marquee span {
    font-family: 'Space Grotesk';
    font-size: 15px;
    font-weight: 600;
    margin: 0 40px;
    color: #858A94;
    letter-spacing: 2px;
}

@keyframes marquee {
    from { transform: translateX(0); }
    to { transform: translateX(-50%); }
}

/* ============================================================
   NOSOTROS
============================================================ */

.about-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 80px;
    align-items: start;
}

.about-copy p {
    margin-top: 25px;
    max-width: 550px;
}

.about-stat {
    margin-top: 40px;
    display: flex;
    gap: 50px;
}

.stat strong {
    display: block;
    font-size: 36px;
    font-family: 'Space Grotesk';
    color: white;
}

.stat small {
    color: var(--gray);
    font-size: 12px;
}

/* ============================================================
   SERVICIOS
============================================================ */

.services {
    background: #0B0D12;
}

.section-heading {
    max-width: 700px;
    margin-bottom: 60px;
}

.services-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
}

.service-card {
    border: 1px solid var(--border);
    padding: 35px;
    min-height: 250px;
    transition: .3s;
    background: rgba(255,255,255,.015);
}

.service-card:hover {
    border-color: var(--blue);
    transform: translateY(-5px);
}

.service-number {
    color: var(--blue);
    font-size: 12px;
    margin-bottom: 40px;
}

.service-card p {
    margin-top: 18px;
    font-size: 14px;
}

/* ============================================================
   EXPERIENCIA Y PROYECTOS
============================================================ */

.project-intro {
    display: flex;
    justify-content: space-between;
    align-items: end;
    gap: 30px;
    margin-bottom: 60px;
}

.project-intro p {
    max-width: 450px;
}

.project {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 65px;
    align-items: center;
    margin-bottom: 120px;
}

.project.reverse .project-visual {
    order: 2;
}

.project.reverse .project-copy {
    order: 1;
}

.project-copy p {
    margin: 22px 0;
}

.project-label {
    color: var(--blue);
    font-size: 12px;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 20px;
}

.project-visual {
    min-width: 0;
}

/* ============================================================
   CARRUSELES
============================================================ */

.carousel {
    position: relative;
    overflow: hidden;
    border-radius: 6px;
    background: #101319;
    border: 1px solid var(--border);
    aspect-ratio: 4 / 3;
}

.carousel-track {
    display: flex;
    height: 100%;
    transition: transform .65s cubic-bezier(.2,.8,.2,1);
}

.carousel-slide {
    flex: 0 0 100%;
    height: 100%;
    position: relative;
    overflow: hidden;
}

.carousel-slide img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 1s;
}

.carousel-slide:hover img {
    transform: scale(1.04);
}

.image-placeholder {
    width: 100%;
    height: 100%;
    min-height: 260px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background:
        radial-gradient(circle at center, rgba(8,123,255,.12), transparent 55%),
        #11141A;
    color: #626976;
    letter-spacing: 2px;
    font-size: 12px;
}

.image-placeholder small {
    margin-top: 10px;
    color: #414650;
    letter-spacing: 0;
}

.carousel-overlay {
    position: absolute;
    inset: 0;
    pointer-events: none;
    background: linear-gradient(180deg, transparent 60%, rgba(0,0,0,.45));
}

.carousel-controls {
    position: absolute;
    left: 20px;
    right: 20px;
    bottom: 18px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    z-index: 5;
}

.carousel-controls button {
    border: 1px solid rgba(255,255,255,.3);
    color: white;
    background: rgba(0,0,0,.3);
    width: 35px;
    height: 35px;
    border-radius: 50%;
    cursor: pointer;
    transition: .2s;
}

.carousel-controls button:hover {
    background: var(--blue);
    border-color: var(--blue);
}

.carousel-dots {
    display: flex;
    gap: 7px;
}

.carousel-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: rgba(255,255,255,.45);
    border: none;
    padding: 0;
    cursor: pointer;
}

.carousel-dot.active {
    background: var(--blue);
    transform: scale(1.4);
}

/* ============================================================
   LOGOS DE CLIENTES
============================================================ */

.client-logo {
    display: block;
    object-fit: contain;
    object-position: left center;
}

.amh-logo {
    width: 105px;
    max-height: 48px;
    margin-top: 18px;
}

.roothua-logo {
    width: 145px;
    max-height: 65px;
    margin-top: 18px;
}

.client-logo-text {
    color: white;
    font-family: 'Space Grotesk';
    font-weight: 700;
    letter-spacing: 2px;
    font-size: 22px;
    margin-top: 20px;
}

/* ============================================================
   PROCESO
============================================================ */

.process {
    background: #0B0D12;
}

.process-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    margin-top: 60px;
}

.process-item {
    border-top: 1px solid var(--border);
    padding-top: 25px;
}

.process-item span {
    color: var(--blue);
    font-size: 12px;
}

.process-item h3 {
    margin: 25px 0 15px;
}

.process-item p {
    font-size: 13px;
}

/* ============================================================
   CONTACTO
============================================================ */

.contact {
    background:
        radial-gradient(circle at 90% 50%, rgba(8,123,255,.15), transparent 40%),
        #08090B;
}

.contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 90px;
}

.contact-copy p {
    margin: 25px 0;
    max-width: 500px;
}

.contact-form {
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.contact-form input,
.contact-form textarea {
    width: 100%;
    background: #101319;
    border: 1px solid var(--border);
    color: white;
    padding: 17px;
    border-radius: 3px;
    outline: none;
    font-family: inherit;
    font-size: 13px;
}

.contact-form input:focus,
.contact-form textarea:focus {
    border-color: var(--blue);
}

.contact-form textarea {
    min-height: 130px;
    resize: vertical;
}

.contact-form button {
    justify-content: center;
}

/* ============================================================
   FOOTER
============================================================ */

footer {
    padding: 35px 8%;
    border-top: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #6D727C;
    font-size: 12px;
    gap: 20px;
}

.footer-logo {
    font-family: 'Space Grotesk';
    font-size: 22px;
    color: white;
    font-weight: 700;
}

.footer-logo span {
    color: var(--blue);
}

/* ============================================================
   CORTINA AZUL
============================================================ */

.curtain {
    position: fixed;
    inset: 0;
    z-index: 2000;
    pointer-events: none;
    transform: scaleY(0);
    transform-origin: bottom;
    background: var(--blue);
}

.curtain.active {
    animation: curtainMove .8s cubic-bezier(.77,0,.18,1);
}

@keyframes curtainMove {
    0% { transform: scaleY(0); transform-origin: bottom; }
    45% { transform: scaleY(1); transform-origin: bottom; }
    55% { transform: scaleY(1); transform-origin: top; }
    100% { transform: scaleY(0); transform-origin: top; }
}

/* ============================================================
   CURSOR
============================================================ */

.pointer-dot {
    position: fixed;
    width: 7px;
    height: 7px;
    background: var(--blue);
    border-radius: 50%;
    pointer-events: none;
    z-index: 3000;
    transform: translate(-50%,-50%);
    box-shadow: 0 0 15px var(--blue);
}

/* ============================================================
   RESPONSIVE
============================================================ */

@media(max-width: 900px) {
    :root {
        --nav-height: 74px;
    }

    section {
        padding: 85px 6%;
    }

    .nav {
        padding: 10px 6%;
    }

    .logo-img {
        width: 165px;
        max-height: 55px;
    }

    .nav-links {
        gap: 15px;
    }

    .nav-links a {
        font-size: 11px;
    }

    .about-grid,
    .project,
    .contact-grid {
        grid-template-columns: 1fr;
        gap: 40px;
    }

    .project.reverse .project-visual,
    .project.reverse .project-copy {
        order: initial;
    }

    .services-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .process-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .project {
        margin-bottom: 85px;
    }
}

@media(max-width: 600px) {
    :root {
        --nav-height: 68px;
    }

    .nav {
        padding: 8px 5%;
    }

    .logo-img {
        width: 145px;
        max-height: 48px;
    }

    .nav-links {
        gap: 10px;
    }

    .nav-links a:not(.nav-cta) {
        display: none;
    }

    .nav-cta {
        padding: 11px 14px;
    }

    .hero {
        min-height: 70vh;
        padding-top: 45px;
        padding-bottom: 75px;
    }

    .hero-description {
        font-size: 15px;
    }

    .hero-bottom {
        left: 6%;
        right: 6%;
        font-size: 9px;
    }

    .about-grid {
        gap: 30px;
    }

    .about-stat {
        gap: 25px;
    }

    .stat strong {
        font-size: 28px;
    }

    .services-grid {
        grid-template-columns: 1fr;
    }

    .service-card {
        min-height: auto;
    }

    .project-intro {
        display: block;
    }

    .project-intro p {
        margin-top: 20px;
    }

    .process-grid {
        grid-template-columns: 1fr;
    }

    .contact-grid {
        gap: 40px;
    }

    footer {
        flex-direction: column;
        align-items: start;
    }
}

</style>
</head>

<body>

<div class="curtain" id="curtain"></div>

<!-- CABECERA -->
<nav class="nav">
    <a href="#inicio" class="logo">__LOGO__</a>

    <div class="nav-links">
        <a href="#nosotros">Nosotros</a>
        <a href="#servicios">Servicios</a>
        <a href="#proyectos">Experiencia</a>
        <a href="#contacto" class="nav-cta">Hablemos ↗</a>
    </div>
</nav>

<!-- PORTADA -->
<section class="hero" id="inicio">
    <div class="container hero-content">
        <div class="eyebrow">Soluciones comerciales · Creatividad · Producción</div>

        <h1>
            Conectamos ideas.
            <span class="blue">Creamos soluciones.</span>
        </h1>

        <p class="hero-description">
            Diseñamos, producimos y ejecutamos proyectos que ayudan a las marcas
            a comunicar mejor, destacar y generar experiencias memorables.
        </p>

        <div class="hero-buttons">
            <a href="#proyectos" class="btn">Conoce nuestros proyectos ↗</a>
            <a href="#contacto" class="btn btn-outline">Cuéntanos tu proyecto</a>
        </div>
    </div>

    <div class="hero-bottom">
        <span>Nexo · Soluciones integrales</span>
        <span>Diseño / Producción / Ejecución</span>
    </div>
</section>

<!-- MARQUEE -->
<div class="marquee">
    <div class="marquee-track">
        <span>BRANDING</span><span>PRODUCCIÓN</span><span>DISEÑO</span>
        <span>EXPERIENCIAS</span><span>COMUNICACIÓN</span><span>PROYECTOS</span>
        <span>BRANDING</span><span>PRODUCCIÓN</span><span>DISEÑO</span>
        <span>EXPERIENCIAS</span><span>COMUNICACIÓN</span><span>PROYECTOS</span>
    </div>
</div>

<!-- NOSOTROS -->
<section id="nosotros">
    <div class="container about-grid">
        <div>
            <div class="eyebrow">01 / Quiénes somos</div>
            <h2>Una idea clara.<br><span class="blue">Una ejecución sólida.</span></h2>
        </div>

        <div class="about-copy">
            <p>
                Nexo es una iniciativa comercial enfocada en conectar necesidades
                con soluciones creativas, prácticas y bien ejecutadas.
            </p>
            <p>
                Trabajamos desde la conceptualización hasta la entrega,
                integrando diseño, proveedores, producción y coordinación
                para convertir ideas en proyectos reales.
            </p>

            <div class="about-stat">
                <div class="stat">
                    <strong>360°</strong>
                    <small>Visión integral</small>
                </div>
                <div class="stat">
                    <strong>1:1</strong>
                    <small>Atención personalizada</small>
                </div>
                <div class="stat">
                    <strong>+</strong>
                    <small>Soluciones a medida</small>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- SERVICIOS -->
<section class="services" id="servicios">
    <div class="container">
        <div class="section-heading">
            <div class="eyebrow">02 / Qué hacemos</div>
            <h2>Ideas que se convierten<br>en <span class="blue">proyectos.</span></h2>
            <p style="margin-top:25px">
                Un enfoque flexible para resolver necesidades de comunicación,
                promoción, producción y desarrollo comercial.
            </p>
        </div>

        <div class="services-grid">
            <div class="service-card">
                <div class="service-number">01 / DISEÑO</div>
                <h3>Diseño &amp; Branding</h3>
                <p>Identidad visual, conceptos creativos, diseño de materiales y aplicaciones de marca.</p>
            </div>

            <div class="service-card">
                <div class="service-number">02 / PRODUCCIÓN</div>
                <h3>Material promocional</h3>
                <p>Productos promocionales, impresos, artículos personalizados y materiales corporativos.</p>
            </div>

            <div class="service-card">
                <div class="service-number">03 / EVENTOS</div>
                <h3>Experiencias</h3>
                <p>Materiales para congresos, eventos, capacitaciones y activaciones comerciales.</p>
            </div>

            <div class="service-card">
                <div class="service-number">04 / DIGITAL</div>
                <h3>Contenido digital</h3>
                <p>Gestión de redes sociales, publicaciones, comunicación y contenido para marcas.</p>
            </div>

            <div class="service-card">
                <div class="service-number">05 / DESARROLLO</div>
                <h3>Proyectos a medida</h3>
                <p>Coordinación de proveedores, desarrollo de productos y soluciones específicas.</p>
            </div>

            <div class="service-card">
                <div class="service-number">06 / GESTIÓN</div>
                <h3>Coordinación integral</h3>
                <p>Planeación, seguimiento, producción y control de entregables de cada proyecto.</p>
            </div>
        </div>
    </div>
</section>

<!-- EXPERIENCIA -->
<section id="proyectos">
    <div class="container">

        <div class="project-intro">
            <div>
                <div class="eyebrow">03 / Experiencia</div>
                <h2>Proyectos que<br><span class="blue">hablan por sí mismos.</span></h2>
            </div>
            <p>
                Cada proyecto es una oportunidad para integrar creatividad,
                planeación y ejecución. Estas experiencias reflejan distintas
                formas de resolver necesidades reales.
            </p>
        </div>

        <!-- AMH -->
        <div class="project">
            <div class="project-visual">
                __AMH_CAROUSEL__
            </div>

            <div class="project-copy">
                <div class="project-label">01 / Producción &amp; Eventos</div>
                <h2>AMH</h2>
                <p>
                    Desarrollo de materiales promocionales y recursos para
                    actividades académicas, congresos y comunicación institucional.
                </p>

                <p>
                    Desde la planeación y diseño hasta la coordinación de producción
                    y entrega, integramos diferentes piezas en una solución coherente.
                </p>

                <div style="margin:25px 0">
                    <span class="tag">Planeación</span>
                    <span class="tag">Diseño</span>
                    <span class="tag">Promocionales</span>
                    <span class="tag">Producción</span>
                    <span class="tag">Eventos</span>
                </div>

                __AMH_LOGO__
            </div>
        </div>

        <!-- ROOTÚA -->
        <div class="project reverse">
            <div class="project-visual">
                __ROOT_CAROUSEL__
            </div>

            <div class="project-copy">
                <div class="project-label">02 / Comunicación &amp; Desarrollo</div>
                <h2>Roothúa</h2>
                <p>
                    Colaboración en proyectos de comunicación, contenido digital
                    y desarrollo de soluciones de mobiliario.
                </p>

                <p>
                    Una experiencia que integra creatividad, producción visual,
                    publicaciones y desarrollo de proyectos físicos.
                </p>

                <div style="margin:25px 0">
                    <span class="tag">Contenido</span>
                    <span class="tag">Redes sociales</span>
                    <span class="tag">Publicaciones</span>
                    <span class="tag">Mobiliario</span>
                    <span class="tag">Proyectos</span>
                </div>

                __ROOT_LOGO__
            </div>
        </div>

    </div>
</section>

<!-- PROCESO -->
<section class="process">
    <div class="container">
        <div class="eyebrow">04 / Cómo trabajamos</div>
        <h2>Del concepto<br>hasta la <span class="blue">entrega.</span></h2>

        <div class="process-grid">
            <div class="process-item">
                <span>01</span>
                <h3>Escuchamos</h3>
                <p>Entendemos el objetivo, las necesidades y el contexto de cada proyecto.</p>
            </div>

            <div class="process-item">
                <span>02</span>
                <h3>Proponemos</h3>
                <p>Desarrollamos una solución, concepto y propuesta de trabajo.</p>
            </div>

            <div class="process-item">
                <span>03</span>
                <h3>Coordinamos</h3>
                <p>Integramos diseño, proveedores, producción y seguimiento.</p>
            </div>

            <div class="process-item">
                <span>04</span>
                <h3>Entregamos</h3>
                <p>Verificamos los resultados y concretamos la solución acordada.</p>
            </div>
        </div>
    </div>
</section>

<!-- CONTACTO -->
<section class="contact" id="contacto">
    <div class="container contact-grid">
        <div class="contact-copy">
            <div class="eyebrow">05 / Contacto</div>
            <h2>¿Tienes una idea?<br><span class="blue">Hagámosla realidad.</span></h2>
            <p>
                Cuéntanos qué necesitas. Podemos ayudarte a desarrollar
                una propuesta, coordinar un proyecto o encontrar una solución.
            </p>

            <a href="mailto:__CORREO__" class="btn btn-outline">Enviar correo ↗</a>
        </div>

        <form class="contact-form" id="contactForm">
            <input type="text" id="nombre" placeholder="Nombre" required>
            <input type="text" id="empresa" placeholder="Empresa / Organización">
            <input type="email" id="email" placeholder="Correo electrónico" required>
            <input type="text" id="tipo" placeholder="¿Qué tipo de proyecto necesitas?">
            <textarea id="mensaje" placeholder="Cuéntanos sobre tu proyecto..." required></textarea>
            <button type="submit" class="btn">Enviar mensaje ↗</button>
        </form>
    </div>
</section>

<!-- FOOTER -->
<footer>
    <div class="footer-logo">NEXO<span>.</span></div>
    <div>Soluciones comerciales · Diseño · Producción</div>
    <div>© <span id="year"></span> Nexo</div>
</footer>

<script>
/* ============================================================
   NAVEGACIÓN Y CORTINA
============================================================ */

const curtain = document.getElementById('curtain');

document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', function(e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (!target) return;

        e.preventDefault();

        curtain.classList.remove('active');
        void curtain.offsetWidth;
        curtain.classList.add('active');

        setTimeout(() => {
            target.scrollIntoView({behavior: 'smooth', block: 'start'});
        }, 250);
    });
});

/* ============================================================
   CARRUSELES AUTOMÁTICOS
============================================================ */

document.querySelectorAll('[data-carousel]').forEach(carousel => {
    const track = carousel.querySelector('.carousel-track');
    const slides = Array.from(carousel.querySelectorAll('.carousel-slide'));
    const dotsContainer = carousel.querySelector('.carousel-dots');
    const prev = carousel.querySelector('.carousel-prev');
    const next = carousel.querySelector('.carousel-next');

    let index = 0;
    let timer;

    slides.forEach((slide, i) => {
        const dot = document.createElement('button');
        dot.className = 'carousel-dot' + (i === 0 ? ' active' : '');
        dot.setAttribute('aria-label', 'Imagen ' + (i + 1));

        dot.addEventListener('click', () => {
            goTo(i);
            restart();
        });

        dotsContainer.appendChild(dot);
    });

    const dots = Array.from(dotsContainer.children);

    function goTo(i) {
        index = (i + slides.length) % slides.length;
        track.style.transform = `translateX(-${index * 100}%)`;

        dots.forEach((dot, j) => {
            dot.classList.toggle('active', j === index);
        });
    }

    function restart() {
        clearInterval(timer);

        if (slides.length > 1) {
            timer = setInterval(() => goTo(index + 1), 4500);
        }
    }

    prev.addEventListener('click', () => {
        goTo(index - 1);
        restart();
    });

    next.addEventListener('click', () => {
        goTo(index + 1);
        restart();
    });

    carousel.addEventListener('mouseenter', () => clearInterval(timer));
    carousel.addEventListener('mouseleave', restart);

    if (slides.length <= 1) {
        prev.style.display = 'none';
        next.style.display = 'none';
    }

    restart();
});

/* ============================================================
   FORMULARIO
============================================================ */

document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const empresa = document.getElementById('empresa').value;
    const email = document.getElementById('email').value;
    const tipo = document.getElementById('tipo').value;
    const mensaje = document.getElementById('mensaje').value;

    const correo = '__CORREO__';

    const subject = encodeURIComponent('Nuevo proyecto Nexo - ' + nombre);

    const body = encodeURIComponent(
        'Nombre: ' + nombre + '\n' +
        'Empresa: ' + empresa + '\n' +
        'Correo: ' + email + '\n' +
        'Proyecto: ' + tipo + '\n\n' +
        'Mensaje:\n' + mensaje
    );

    if (!correo) {
        alert('Configura CORREO en app.py para recibir los mensajes.');
        return;
    }

    window.location.href = `mailto:${correo}?subject=${subject}&body=${body}`;
});

/* ============================================================
   EFECTO DE CURSOR
============================================================ */

if (window.matchMedia('(pointer:fine)').matches) {
    let lastTime = 0;

    document.addEventListener('mousemove', function(e) {
        const now = Date.now();

        if (now - lastTime < 40) return;
        lastTime = now;

        const dot = document.createElement('div');
        dot.className = 'pointer-dot';
        dot.style.left = e.clientX + 'px';
        dot.style.top = e.clientY + 'px';

        document.body.appendChild(dot);

        setTimeout(() => {
            dot.style.transition = 'opacity .5s, transform .5s';
            dot.style.opacity = '0';
            dot.style.transform = 'translate(-50%,-50%) scale(2)';
        }, 20);

        setTimeout(() => dot.remove(), 600);
    });
});

document.getElementById('year').textContent = new Date().getFullYear();
</script>

</body>
</html>
"""

# ============================================================
# SUSTITUCIÓN DE CONTENIDO
# ============================================================

pagina = pagina.replace("__LOGO__", logo_nexo)
pagina = pagina.replace("__AMH_LOGO__", logo_amh)
pagina = pagina.replace("__ROOT_LOGO__", logo_roothua)

pagina = pagina.replace(
    "__AMH_CAROUSEL__",
    carrusel_imagenes(amh_images, "Proyecto AMH")
)

pagina = pagina.replace(
    "__ROOT_CAROUSEL__",
    carrusel_imagenes(roothua_images, "Proyecto Roothúa")
)

pagina = pagina.replace("__CORREO__", CORREO)

# ============================================================
# RENDERIZADO
# ============================================================

components.html(
    pagina,
    height=7200,
    scrolling=True
)
