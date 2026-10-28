import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64
import html

# ==================================================
# CONFIGURACIÓN
# ==================================================
st.set_page_config(
    page_title="Nexo Promocional | Ideas que conectan",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"

# Personaliza estos datos cuando estés listo
CORREO = ""       # Ejemplo: ventas@tudominio.com
WHATSAPP = ""     # Ejemplo: 525512345678, solo dígitos


def imagen_base64(nombre):
    """Carga una imagen local de assets y la convierte en una imagen incrustada."""
    ruta = ASSETS / nombre
    if not ruta.exists():
        return ""
    extension = ruta.suffix.lower()
    mime = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".svg": "image/svg+xml",
    }.get(extension, "application/octet-stream")
    contenido = base64.b64encode(ruta.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{contenido}"


def bloque_imagen(nombre, clase, etiqueta):
    src = imagen_base64(nombre)
    if src:
        return (
            f'<div class="{clase}">'
            f'<img src="{src}" alt="{html.escape(etiqueta)}">'
            '</div>'
        )
    return (
        f'<div class="{clase} placeholder">'
        f'<span>{html.escape(etiqueta)}</span>'
        '</div>'
    )


logo_path = ASSETS / "nexo-horizontal.svg"
logo_html = (
    logo_path.read_text(encoding="utf-8").replace(
        "<svg ", '<svg class="logo-img" ', 1
    )
    if logo_path.is_file()
    else '<span class="logo-mark">N</span><span>NEXO<span class="logo-dot">.</span></span>'
)

amh_imagen = bloque_imagen(
    "amh-entrega-01.jpg", "project-image", "AMH · Materiales para eventos"
)
productos_imagen = bloque_imagen(
    "productos-promocionales.jpg", "project-image", "Productos promocionales"
)
roothua_imagen = bloque_imagen(
  "roothua-proyecto.jpg", "project-image", "Roothúa · Publicidad y contenido digital"
)


def logo_amh_asset():
    """Muestra un logo visible de AMH, en formato SVG y no como PDF embebido."""
    return """
    <div class="client-logo-card client-logo-feature">
      <div class="client-logo-svg-wrap">
        <svg class="client-logo-svg" viewBox="0 0 700 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Asociación Mexicana de Hepatología">
          <defs>
            <path id="amh-ring-top" d="M 120,130 a 116,116 0 1,1 0,0.0001"/>
            <path id="amh-ring-bottom" d="M 580,130 a 116,116 0 1,1 0,0.0001"/>
          </defs>
          <circle cx="350" cy="130" r="115" fill="none" stroke="#2aa061" stroke-width="3"/>
          <circle cx="350" cy="130" r="97" fill="none" stroke="#2aa061" stroke-width="2.5" opacity="0.8"/>
          <circle cx="350" cy="130" r="79" fill="none" stroke="#2aa061" stroke-width="2" opacity="0.8"/>

          <text font-size="21" font-weight="700" letter-spacing="2.5" fill="#2aa061" font-family="Arial, Helvetica, sans-serif" textLength="520">
            <textPath href="#amh-ring-top" startOffset="12%">ASOCIACIÓN MEXICANA DE HEPATOLOGÍA</textPath>
          </text>
          <text font-size="21" font-weight="700" letter-spacing="2.5" fill="#2aa061" font-family="Arial, Helvetica, sans-serif" textLength="520">
            <textPath href="#amh-ring-bottom" startOffset="-12%">ASOCIACIÓN MEXICANA DE HEPATOLOGÍA</textPath>
          </text>

          <g transform="translate(350 130)">
            <path d="M -58 24 C -30 2, -8 -8, 0 -18 C 12 -8, 28 -2, 48 0 C 69 2, 84 10, 96 26 C 108 40, 110 59, 101 71 C 87 86, 62 82, 44 76 C 28 70, 16 63, 6 55 C 3 53, -5 51, -12 53 L -12 80 C -32 88, -51 85, -66 72 C -82 59, -85 38, -58 24 Z" fill="#2aa061"/>
            <path d="M 30 96 C 53 105, 68 142, 65 176 C 63 204, 38 220, 8 219 C -24 219, -42 197, -47 165 C -50 135, -32 109, 0 102 C 9 100, 20 96, 30 96 Z" fill="#2aa061" opacity="0.97"/>
            <path d="M 15 104 C 27 118, 31 145, 26 170" fill="none" stroke="#ffffff" stroke-width="10" stroke-linecap="round"/>
            <path d="M -6 104 C 14 121, 18 142, 11 170" fill="none" stroke="#ffffff" stroke-width="8" stroke-linecap="round"/>
            <path d="M -31 24 C -54 35, -68 48, -86 66" fill="none" stroke="#2aa061" stroke-width="12" stroke-linecap="round"/>
            <path d="M 95 24 C 119 14, 132 16, 147 23" fill="none" stroke="#2aa061" stroke-width="12" stroke-linecap="round"/>
          </g>
        </svg>
      </div>
    </div>
    """


amh_cliente_logo = logo_amh_asset()

# ==================================================
# PÁGINA COMPLETA
# ==================================================
pagina = r"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
:root {
  --bg: #F5F8FC;
  --bg2: #FFFFFF;
  --panel: #FFFFFF;
    --blue: #087BFF;
  --blue2: #075EAD;
  --cyan: #007F9E;
  --white: #14263D;
  --muted: #596B80;
  --border: #DCE4EE;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
    margin: 0;
    background: var(--bg);
    color: var(--white);
    font-family: Arial, Helvetica, sans-serif;
    overflow-x: hidden;
}
a { color: inherit; text-decoration: none; }
button, input, textarea, select { font: inherit; }
.wrap { width: min(1180px, 90%); margin: auto; }
section { scroll-margin-top: 28px; }
nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 24px 0;
    border-bottom: 1px solid var(--border);
    gap: 20px;
}
.brand {
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 800;
    font-size: 25px;
    letter-spacing: 5px;
}
.logo-mark {
    color: var(--blue2);
    font-size: 34px;
    font-weight: 900;
    letter-spacing: -4px;
    margin-right: 5px;
}
.logo-dot { color: var(--blue2); }
.logo-img { display: block; width: 170px; height: 60px; flex: 0 0 auto; }
.navlinks {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 25px;
    font-size: 14px;
    color: #4B5D72;
}
.navlinks a:hover { color: var(--blue2); }
.nav-cta {
    background: var(--blue);
    border-radius: 6px;
    padding: 12px 17px;
    color: white !important;
}
.hero {
    min-height: 610px;
    position: relative;
    display: flex;
    align-items: center;
    overflow: hidden;
    padding: 80px 0;
}
.hero-glow {
    position: absolute;
    right: -170px;
    top: 5px;
    width: 600px;
    height: 500px;
    background: radial-gradient(ellipse, rgba(0,91,255,.10), transparent 68%);
    pointer-events: none;
}
.hero-content { position: relative; z-index: 2; max-width: 780px; }
.eyebrow {
    color: var(--blue2);
    text-transform: uppercase;
    letter-spacing: 4px;
    font-size: 12px;
    font-weight: 800;
    margin-bottom: 23px;
}
h1, h2, h3, p { margin-top: 0; }
h1 {
    font-size: clamp(46px, 7.3vw, 88px);
    line-height: .99;
    letter-spacing: -5px;
    margin-bottom: 26px;
    font-weight: 800;
}
h1 span, .blue { color: var(--blue2); }
.hero p {
    font-size: 18px;
    line-height: 1.8;
    max-width: 590px;
    color: #52657B;
}
.actions { display: flex; flex-wrap: wrap; gap: 13px; margin-top: 32px; }
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 15px 22px;
    border-radius: 7px;
    background: var(--blue);
    color: white;
    font-weight: 700;
    border: 1px solid var(--blue);
    transition: .2s ease;
}
.btn:hover { transform: translateY(-3px); background: #218CFF; }
.btn.outline { background: transparent; border-color: #AAB9C9; color: var(--white); }
.btn.outline:hover { border-color: var(--blue2); }
.hero-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 24px;
    margin-top: 46px;
    font-size: 12px;
    letter-spacing: .5px;
    color: #596B80;
}
.hero-meta b { color: var(--blue2); }
.section { padding: 78px 0; border-top: 1px solid #E2E8F0; }
.section-head { max-width: 760px; margin-bottom: 35px; }
.section-head h2 {
    font-size: clamp(32px, 4.5vw, 54px);
    line-height: 1.08;
    letter-spacing: -2px;
    margin-bottom: 16px;
}
.section-head p, .body-copy {
    color: var(--muted);
    font-size: 16px;
    line-height: 1.85;
}
.grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }
.grid2 { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 34px; align-items: center; }
.card {
    border: 1px solid var(--border);
    background: linear-gradient(145deg, #FFFFFF, #F8FAFC);
    padding: 27px;
    min-height: 220px;
    border-radius: 10px;
    transition: transform .25s, border-color .25s, box-shadow .25s;
}
.card:hover {
    transform: translateY(-6px);
    border-color: #1269C5;
    box-shadow: 0 12px 38px #17365D12;
}
.num { color: var(--blue2); font-size: 12px; font-weight: 800; margin-bottom: 26px; }
.card h3 { font-size: 21px; letter-spacing: -.5px; margin-bottom: 12px; }
.card p { color: var(--muted); line-height: 1.75; font-size: 14px; margin-bottom: 0; }
.band {
    border: 1px solid #D5E2F0;
    background: linear-gradient(100deg, #F1F7FE, #FFFFFF);
    border-radius: 10px;
    padding: 26px 30px;
    margin-top: 25px;
    line-height: 1.7;
}
.band strong { color: var(--white); }
.band span { color: var(--muted); }
.project-image {
    width: 100%;
    height: 350px;
    border: 1px solid #D8E2ED;
    border-radius: 11px;
    overflow: hidden;
    background:
      radial-gradient(ellipse at 80% 10%, #E1F0FF, transparent 45%),
      linear-gradient(145deg, #F3F8FD, #EAF1F8);
    display: flex;
    align-items: center;
    justify-content: center;
}
.project-image img { width: 100%; height: 100%; object-fit: cover; }
.project-image.placeholder span {
    padding: 25px;
    text-align: center;
    color: #075EAD;
    font-size: 21px;
    font-weight: 800;
    letter-spacing: 1px;
}
.project-copy h2 { font-size: 38px; line-height: 1.12; letter-spacing: -1.5px; }
.project-copy p { color: var(--muted); line-height: 1.8; }
.tags { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 18px; }
.tag {
    border: 1px solid #C9DDF1;
    background: #F0F6FC;
    color: #075EAD;
    padding: 7px 10px;
    border-radius: 4px;
    font-size: 12px;
}
.steps { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }
.step {
    border-top: 2px solid var(--blue);
    padding-top: 20px;
}
.step b { display: block; color: var(--blue2); font-size: 13px; margin-bottom: 12px; }
.step h3 { font-size: 18px; margin-bottom: 9px; }
.step p { color: var(--muted); font-size: 14px; line-height: 1.7; }
.cta {
    padding: 45px;
    border: 1px solid #C9DDF1;
    border-radius: 12px;
    background:
      radial-gradient(ellipse at 95% 5%, #E5F2FF, transparent 40%),
      linear-gradient(125deg, #F3F8FD, #FFFFFF);
}
.cta h2 { font-size: clamp(35px, 5vw, 57px); line-height: 1.06; letter-spacing: -2px; margin-bottom: 18px; }
.cta p { color: var(--muted); line-height: 1.8; max-width: 640px; }
.contact-form {
    margin-top: 28px;
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
}
.contact-form label { display: block; font-size: 12px; color: #43566D; margin-bottom: 7px; }
.contact-form input, .contact-form select, .contact-form textarea {
    display: block;
    width: 100%;
    background: #FFFFFF;
    color: #14263D;
    border: 1px solid #CBD6E2;
    border-radius: 5px;
    padding: 13px;
    outline: none;
}
.contact-form input:focus, .contact-form textarea:focus, .contact-form select:focus {
    border-color: var(--blue);
}
.contact-form textarea { min-height: 110px; resize: vertical; }
.full { grid-column: 1 / -1; }
.contact-form button { cursor: pointer; }
.client-strip {
    margin-top: 22px;
    padding: 0;
    background: transparent;
    border: none;
    border-radius: 0;
    box-shadow: none;
}
.client-strip .eyebrow {
    margin-bottom: 10px;
    text-align: center;
}
.client-logo-row {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    min-height: 86px;
    padding: 0;
    background: transparent;
}
.client-logo-card {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 260px;
    min-height: 120px;
    padding: 16px 24px;
    border: 1px solid #D4E4F5;
    border-radius: 12px;
    background: linear-gradient(135deg, #F7FBFF, #FFFFFF);
    box-shadow: 0 12px 28px rgba(10, 40, 80, 0.06);
}
.client-logo-feature {
    width: min(100%, 520px);
    min-width: 0;
    min-height: 190px;
    padding: 18px 20px;
    background: linear-gradient(135deg, #ffffff, #f4faf7);
    border-color: #cfe4d8;
}
.client-logo-svg-wrap {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    min-height: 150px;
}
.client-logo-svg {
    display: block;
    width: 100%;
    max-width: 500px;
    height: auto;
}
.client-logo-link {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 6px;
    text-align: center;
    text-decoration: none;
    color: #0D4C8C;
}
.client-logo-mark {
    font-size: clamp(26px, 4vw, 42px);
    font-weight: 900;
    letter-spacing: -2px;
}
.client-logo-link small {
    font-size: 12px;
    color: #4A6079;
    letter-spacing: 0.6px;
}
footer {
    border-top: 1px solid var(--border);
    padding: 28px 0 35px;
    display: flex;
    justify-content: space-between;
    gap: 15px;
    flex-wrap: wrap;
    color: #65768A;
    font-size: 12px;
}
footer b { color: var(--white); letter-spacing: 2px; }
.upcoming {
  border-left: 3px solid var(--blue);
  padding: 5px 0 5px 22px;
  max-width: 760px;
}
.upcoming p { color: var(--muted); line-height: 1.8; margin-bottom: 20px; }

/* Rastro del cursor: N azul con brillo */
#trail-layer {
    position: fixed;
    inset: 0;
    z-index: 9999;
    pointer-events: none;
    overflow: hidden;
}
.trail-n {
    position: absolute;
    width: 23px;
    height: 27px;
    color: #087BFF;
    font-family: Arial, sans-serif;
    font-weight: 900;
    font-size: 25px;
    line-height: 27px;
    text-align: center;
    text-shadow: 0 0 7px #087BFF, 0 0 17px #005BFF, 0 0 30px #005BFF;
    transform: translate(-50%, -50%) scale(.8) rotate(-8deg);
    opacity: 0;
    will-change: transform, opacity;
}
@media (hover: none), (pointer: coarse) {
    #trail-layer { display: none; }
}
@media (max-width: 760px) {
    .wrap { width: 91%; }
    nav { align-items: flex-start; flex-direction: column; }
    .navlinks { gap: 15px; }
    .hero { min-height: auto; padding: 75px 0; }
    h1 { letter-spacing: -2.5px; }
    .grid3, .grid2, .steps { grid-template-columns: 1fr; }
    .project-image { height: 260px; }
    .project-copy h2 { font-size: 31px; }
    .section { padding: 55px 0; }
    .cta { padding: 25px; }
    .contact-form { grid-template-columns: 1fr; }
    .full { grid-column: auto; }
}
</style>
</head>
<body>

<div id="trail-layer" aria-hidden="true"></div>

<div class="wrap">
  <nav>
    <a class="brand" href="#inicio">__LOGO__</a>
    <div class="navlinks">
      <a href="#inicio">Inicio</a>
      <a href="#servicios">Servicios</a>
      <a href="#proyectos">Proyectos</a>
      <a href="#proximos">Próximos proyectos</a>
      <a class="nav-cta" href="#contacto">Hablemos ↗</a>
    </div>
  </nav>

  <section class="hero" id="inicio">
    <div class="hero-glow"></div>
    <div class="hero-content">
      <div class="eyebrow">Nexo Promocional · Soluciones para empresas</div>
      <h1>Tu proyecto.<br>Muchas ideas.<br><span>Un solo Nexo.</span></h1>
      <p>Integramos productos promocionales, impresión, diseño y soluciones digitales para que tu marca llegue más lejos, con menos complicaciones.</p>
      <div class="actions">
        <a class="btn" href="#contacto">Cuéntanos tu proyecto ↗</a>
        <a class="btn outline" href="#servicios">Explorar servicios ↓</a>
      </div>
      <div class="hero-meta">
        <span><b>01</b> · Atención cercana</span>
        <span><b>02</b> · Soluciones integrales</span>
        <span><b>03</b> · De la idea a la entrega</span>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="section-head">
      <div class="eyebrow">Una solución integral</div>
      <h2>Todo conectado.<br><span class="blue">Todo más fácil.</span></h2>
      <p>Un solo punto de contacto para coordinar materiales, comunicación y recursos que tu empresa necesita para destacar.</p>
    </div>
    <div class="grid3">
      <article class="card"><div class="num">01 / PLANEA</div><h3>Escuchamos tu necesidad</h3><p>Entendemos tu objetivo, tu público y los materiales que necesitas.</p></article>
      <article class="card"><div class="num">02 / INTEGRAMOS</div><h3>Coordinamos soluciones</h3><p>Conectamos diseño, producción e impresión para resolver el proyecto.</p></article>
      <article class="card"><div class="num">03 / ENTREGAMOS</div><h3>Acompañamos el proceso</h3><p>Damos seguimiento a los detalles de los productos y servicios acordados.</p></article>
    </div>
    <div class="band"><strong>Menos proveedores que coordinar. Más claridad en cada proyecto.</strong><br><span>Desde una pieza promocional hasta los materiales para un evento o una campaña.</span></div>
  </section>

  <section class="section" id="servicios">
    <div class="section-head">
      <div class="eyebrow">Qué hacemos</div>
      <h2>Todo lo que tu marca necesita para <span class="blue">hacerse notar.</span></h2>
      <p>Una oferta flexible para empresas, asociaciones, instituciones, eventos y comercios.</p>
    </div>
    <div class="grid3">
      <article class="card"><div class="num">01</div><h3>Productos promocionales</h3><p>Tazas, plumas, bolsas, pines, gafetes y artículos personalizados.</p></article>
      <article class="card"><div class="num">02</div><h3>Impresión y gran formato</h3><p>Lonas, banners, roll-ups, muros gráficos, viniles, carteles y señalización.</p></article>
      <article class="card"><div class="num">03</div><h3>Papelería y comunicación</h3><p>Folletos, volantes, dípticos, trípticos, carpetas, invitaciones y materiales institucionales.</p></article>
      <article class="card"><div class="num">04</div><h3>Diseño gráfico</h3><p>Materiales para eventos, campañas, presentaciones y comunicación de marca.</p></article>
      <article class="card"><div class="num">05</div><h3>Eventos y acreditaciones</h3><p>Boletos digitales, gafetes, códigos QR y materiales de apoyo para registro.</p></article>
      <article class="card"><div class="num">06</div><h3>Soluciones digitales</h3><p>Páginas informativas, formularios y herramientas sencillas para compartir información.</p></article>
    </div>
  </section>

  <section class="section" id="proyectos">
    <div class="section-head">
      <div class="eyebrow">Nuestra experiencia</div>
      <h2>Ideas que pasan del diseño <span class="blue">a la realidad.</span></h2>
      <p>Convertimos necesidades concretas en materiales útiles, coordinados y alineados con cada proyecto.</p>
    </div>
    <div class="grid2">
      __AMH_IMAGE__
      <div class="project-copy">
        <div class="eyebrow">Caso de éxito · AMH</div>
        <h2>Materiales que trabajan en conjunto.</h2>
        <p>Para la Asociación Mexicana de Hepatología se coordinaron materiales promocionales y gráficos para actividades y eventos.</p>
        <div class="tags"><span class="tag">Tazas y plumas</span><span class="tag">Gafetes</span><span class="tag">Roll-up</span><span class="tag">Muro gráfico 3×3</span><span class="tag">Material del evento</span></div>
      </div>
    </div>
    <div style="height:45px"></div>
    <div class="grid2">
      <div class="project-copy">
        <div class="eyebrow">Producción y comunicación</div>
        <h2>Una marca consistente en cada detalle.</h2>
        <p>Integramos distintas piezas para que los materiales de comunicación mantengan una presentación coherente con el propósito de cada cliente.</p>
        <div class="tags"><span class="tag">Planeación</span><span class="tag">Producción</span><span class="tag">Impresión</span><span class="tag">Entrega</span></div>
      </div>
      __PRODUCTS_IMAGE__
    </div>
  </section>

  <section class="section" id="proximos">
    <div class="section-head">
      <div class="eyebrow">Lo que viene</div>
      <h2>Próximos <span class="blue">proyectos.</span></h2>
    </div>
    <div class="upcoming">
      <p>Estamos preparando nuevas colaboraciones y soluciones. Muy pronto compartiremos más detalles; mientras tanto, cuéntanos qué proyecto te gustaría hacer realidad.</p>
      <a class="btn" href="#contacto">Platiquemos de tu proyecto ↗</a>
    </div>
  </section>

  <section class="section" id="roothua">
    <div class="grid2">
      __ROOTHUA_IMAGE__
      <div class="project-copy">
        <div class="eyebrow">Caso de éxito · Roothúa</div>
        <h2>Publicidad y contenido para conectar con su audiencia.</h2>
        <p>Desarrollamos publicidad, manejo de redes sociales, creación de contenido y edición de imágenes para fortalecer la comunicación de Roothúa.</p>
        <div class="tags"><span class="tag">Publicidad</span><span class="tag">Manejo de redes sociales</span><span class="tag">Creación de contenido</span><span class="tag">Edición de imágenes</span></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="section-head">
      <div class="eyebrow">Cómo trabajamos</div>
      <h2>Un proceso claro,<br><span class="blue">de principio a fin.</span></h2>
      <p>Queremos que solicitar tus materiales sea más sencillo.</p>
    </div>
    <div class="steps">
      <div class="step"><b>01 / CONTACTO</b><h3>Nos contactas</h3><p>Cuéntanos qué necesitas.</p></div>
      <div class="step"><b>02 / PLANEACIÓN</b><h3>Preparamos</h3><p>Definimos materiales y alcance.</p></div>
      <div class="step"><b>03 / PROPUESTA</b><h3>Cotizamos</h3><p>Revisamos opciones y tiempos.</p></div>
      <div class="step"><b>04 / SEGUIMIENTO</b><h3>Coordinamos</h3><p>Damos seguimiento al pedido.</p></div>
    </div>
  </section>

  <section class="section" id="contacto">
    <div class="cta">
      <div class="eyebrow">Hagamos equipo</div>
      <h2>¿Qué necesitas<br><span class="blue">resolver hoy?</span></h2>
      <p>Cuéntanos tu idea. Te ayudaremos a identificar los materiales y servicios que pueden hacer realidad tu proyecto.</p>

      <form class="contact-form" id="contact-form">
        <div><label for="nombre">Nombre *</label><input id="nombre" name="nombre" required placeholder="Tu nombre"></div>
        <div><label for="empresa">Empresa u organización</label><input id="empresa" name="empresa" placeholder="Nombre de tu organización"></div>
        <div><label for="correo">Correo electrónico *</label><input id="correo" name="correo" type="email" required placeholder="tu@correo.com"></div>
        <div><label for="tipo">Servicio que necesitas</label>
          <select id="tipo" name="tipo">
            <option>Productos promocionales</option>
            <option>Impresión y gran formato</option>
            <option>Diseño y comunicación</option>
            <option>Materiales para eventos</option>
            <option>Soluciones digitales</option>
            <option>Mobiliario o renovación</option>
            <option>Proyecto integral</option>
            <option>Otro</option>
          </select>
        </div>
        <div class="full"><label for="mensaje">Cuéntanos sobre tu proyecto *</label><textarea id="mensaje" name="mensaje" required placeholder="¿Qué necesitas, para cuándo y en qué cantidad?"></textarea></div>
        <div class="full"><button class="btn" type="submit">Preparar solicitud ↗</button></div>
      </form>
      <p id="form-result" aria-live="polite" style="margin-top:16px"></p>
      <div id="contact-links" style="margin-top:16px"></div>
    </div>

    <div class="client-strip">
      <div class="eyebrow">Clientes</div>
      <div class="client-logo-row">
        __CLIENT_LOGO__
      </div>
    </div>
  </section>

  <footer>
    <div><b>NEXO PROMOCIONAL</b><br>Ideas que conectan. Soluciones que avanzan.</div>
    <div>Productos · Impresión · Diseño · Soluciones digitales</div>
    <div>© Nexo Promocional</div>
  </footer>
</div>

<script>
/* Los anclajes están dentro del iframe; desplaza el contenedor de Streamlit. */
document.addEventListener("click", function (event) {
    const link = event.target instanceof Element
        ? event.target.closest('a[href^="#"]')
        : null;
    if (!link) return;

    const target = document.getElementById(link.getAttribute("href").slice(1));
    const frame = window.frameElement;
    if (!target) return;
    event.preventDefault();

    if (!frame) {
        target.scrollIntoView({behavior: "smooth", block: "start"});
        return;
    }

    const parentWindow = window.parent;
    const parentDocument = frame.ownerDocument;
    const targetTop =
        frame.getBoundingClientRect().top +
        target.getBoundingClientRect().top;
    let container = frame.parentElement;

    while (container && container !== parentDocument.body) {
        const overflowY = parentWindow.getComputedStyle(container).overflowY;
        if (
            ["auto", "scroll", "overlay"].includes(overflowY) &&
            container.scrollHeight > container.clientHeight
        ) {
            break;
        }
        container = container.parentElement;
    }

    if (container && container !== parentDocument.body) {
        container.scrollTo({
            top: container.scrollTop + targetTop - container.getBoundingClientRect().top - 24,
            behavior: "smooth",
        });
    } else {
        const scrollRoot = parentDocument.scrollingElement || parentDocument.documentElement;
        parentWindow.scrollTo({
            top: scrollRoot.scrollTop + targetTop - 24,
            behavior: "smooth",
        });
    }
}, true);

/* =================================================
   ESTELA INTERACTIVA DE LA N DE NEXO
   ================================================= */
(function () {
    const layer = document.getElementById("trail-layer");
    if (!layer || !window.matchMedia("(hover: hover) and (pointer: fine)").matches) return;

    const total = 11;
    const items = [];
    for (let i = 0; i < total; i++) {
        const el = document.createElement("span");
        el.className = "trail-n";
        el.textContent = "N";
        layer.appendChild(el);
        items.push({el: el, x: -100, y: -100});
    }

    let mouseX = -100, mouseY = -100;
    let visible = false;
    let lastX = -100, lastY = -100;

    window.addEventListener("mousemove", function (e) {
        mouseX = e.clientX;
        mouseY = e.clientY;
        visible = true;
    }, {passive: true});

    window.addEventListener("mouseout", function (e) {
        if (!e.relatedTarget) visible = false;
    });

    window.addEventListener("blur", function () { visible = false; });
    window.addEventListener("focus", function () { visible = true; });

    function animate() {
        let targetX = mouseX;
        let targetY = mouseY;

        items.forEach(function (item, i) {
            const lag = 0.29 - i * 0.014;
            item.x += (targetX - item.x) * lag;
            item.y += (targetY - item.y) * lag;

            const progress = 1 - i / total;
            const scale = 0.45 + progress * 0.55;
            const opacity = visible ? Math.pow(progress, 1.45) * 0.9 : 0;

            item.el.style.left = item.x + "px";
            item.el.style.top = item.y + "px";
            item.el.style.opacity = opacity;
            item.el.style.transform =
                "translate(-50%,-50%) scale(" + scale + ") rotate(-8deg)";
            item.el.style.filter = "blur(" + (1 - progress) * 1.3 + "px)";

            targetX = item.x + (mouseX - item.x) * 0.12;
            targetY = item.y + (mouseY - item.y) * 0.12;
        });

        lastX = mouseX;
        lastY = mouseY;
        requestAnimationFrame(animate);
    }
    animate();
})();

/* =================================================
   CONTACTO
   ================================================= */
(function () {
    const form = document.getElementById("contact-form");
    const result = document.getElementById("form-result");
    const links = document.getElementById("contact-links");

    const emailDestino = "__EMAIL__";
    const whatsappDestino = "__WHATSAPP__";

    if (whatsappDestino) {
        const a = document.createElement("a");
        a.className = "btn outline";
        a.target = "_blank";
        a.rel = "noopener";
        a.href = "https://wa.me/" + whatsappDestino;
        a.textContent = "También puedes escribirnos por WhatsApp";
        links.appendChild(a);
    }

    form.addEventListener("submit", function (e) {
        e.preventDefault();
        const data = new FormData(form);
        const nombre = data.get("nombre").trim();
        const correo = data.get("correo").trim();
        const empresa = data.get("empresa").trim();
        const tipo = data.get("tipo");
        const mensaje = data.get("mensaje").trim();

        const asunto = "Solicitud de cotización Nexo Promocional: " + tipo;
        const cuerpo =
            "Nombre: " + nombre + "\n" +
            "Empresa: " + empresa + "\n" +
            "Correo: " + correo + "\n" +
            "Servicio: " + tipo + "\n\n" +
            "Proyecto:\n" + mensaje;

        if (emailDestino) {
            window.location.href =
                "mailto:" + emailDestino +
                "?subject=" + encodeURIComponent(asunto) +
                "&body=" + encodeURIComponent(cuerpo);
            result.textContent = "Se abrirá tu aplicación de correo para que puedas revisar y enviar la solicitud.";
        } else {
            const blob = new Blob([asunto + "\n\n" + cuerpo], {type: "text/plain;charset=utf-8"});
            const url = URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;
            a.download = "solicitud-nexo.txt";
            a.click();
            URL.revokeObjectURL(url);
            result.textContent = "Descargamos tu solicitud. Configura el correo comercial para habilitar el envío directo.";
        }
    });
})();
</script>
</body>
</html>
"""

# Sustituir los espacios reservados por contenido seguro
pagina = pagina.replace("__LOGO__", logo_html)
pagina = pagina.replace("__AMH_IMAGE__", amh_imagen)
pagina = pagina.replace("__PRODUCTS_IMAGE__", productos_imagen)
pagina = pagina.replace("__ROOTHUA_IMAGE__", roothua_imagen)
pagina = pagina.replace("__EMAIL__", CORREO.strip())
pagina = pagina.replace("__WHATSAPP__", "".join(c for c in WHATSAPP if c.isdigit()))
pagina = pagina.replace("__CLIENT_LOGO__", amh_cliente_logo)

# El contenido completo se encuentra dentro del mismo marco para que
# el cursor y su estela compartan el mismo contexto del navegador.
components.html(
    pagina,
  height=7200,
  scrolling=True,
)
