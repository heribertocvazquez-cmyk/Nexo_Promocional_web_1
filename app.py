
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64
import html
import json

# =====================================================
# CONFIGURACIÓN
# =====================================================
st.set_page_config(
    page_title="Nexo Promocional | Ideas que conectan",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"

# Completa estos datos para habilitar el contacto directo.
CORREO = ""
WHATSAPP = ""


# =====================================================
# FUNCIONES AUXILIARES
# =====================================================
def imagen_base64(nombre):
    ruta = ASSETS / nombre

    if not ruta.exists():
        return ""

    mime = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".svg": "image/svg+xml",
    }.get(ruta.suffix.lower(), "application/octet-stream")

    contenido = base64.b64encode(ruta.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{contenido}"


def bloque_imagen(nombre, clase, etiqueta):
    src = imagen_base64(nombre)

    if src:
        return (
            f'<div class="{clase}">'
            f'<img src="{src}" alt="{html.escape(etiqueta)}">'
            "</div>"
        )

    return (
        f'<div class="{clase} placeholder">'
        f"<span>{html.escape(etiqueta)}</span>"
        "</div>"
    )


def cargar_logo(nombre, alt, ancho=200):
    src = imagen_base64(nombre)

    if not src:
        return ""

    return (
        '<div class="client-logo-card">'
        f'<img class="client-logo-svg" src="{src}" '
        f'alt="{html.escape(alt)}" style="max-width:{ancho}px">'
        "</div>"
    )


def logo_cliente_amh():
    logo = cargar_logo(
        "logo-hepatologia.svg",
        "Asociación Mexicana de Hepatología",
    )

    if logo:
        return logo

    return """
    <div class="client-logo-card">
        <span class="client-logo-mark">AMH</span>
        <small>Asociación Mexicana de Hepatología</small>
    </div>
    """


# =====================================================
# LOGOTIPOS E IMÁGENES
# =====================================================
logo_path = ASSETS / "nexo-horizontal.svg"

if logo_path.exists():
    logo_html = logo_path.read_text(encoding="utf-8")
    logo_html = logo_html.replace(
        "<svg ",
        '<svg class="logo-img" ',
        1,
    )
else:
    logo_html = """
    <span class="logo-mark">N</span>
    <span>NEXO<span class="logo-dot">.</span></span>
    """

amh_imagen = bloque_imagen(
    "amh-entrega-01.jpg",
    "project-image",
    "Materiales promocionales para AMH",
)

productos_imagen = bloque_imagen(
    "productos-promocionales.jpg",
    "project-image",
    "Productos promocionales",
)

roothua_imagen = bloque_imagen(
    "roothua-proyecto.jpg",
    "project-image",
    "Proyecto Roothúa",
)

clientes_logos = (
    logo_cliente_amh()
    + cargar_logo("roothua_logo.svg", "Roothúa")
)


# =====================================================
# DOCUMENTO HTML
# =====================================================
pagina = r"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport"
      content="width=device-width, initial-scale=1, maximum-scale=5">

<style>
:root {
    --bg: #F5F8FC;
    --panel: #FFFFFF;
    --blue: #087BFF;
    --blue2: #075EAD;
    --ink: #14263D;
    --muted: #596B80;
    --border: #DCE4EE;
}

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: auto;
    width: 100%;
    overflow-x: clip;
}

body {
    margin: 0;
    width: 100%;
    max-width: 100%;
    background: var(--bg);
    color: var(--ink);
    font-family: Arial, Helvetica, sans-serif;
    overflow-x: clip;
    -webkit-text-size-adjust: 100%;
}

img {
    max-width: 100%;
}

a {
    color: inherit;
    text-decoration: none;
}

button,
input,
select,
textarea {
    font: inherit;
}

.wrap {
    width: min(1180px, 90%);
    margin: auto;
}

section {
    scroll-margin-top: 22px;
}

/* =====================================================
   NAVEGACIÓN
   ===================================================== */
nav {
    position: relative;
    z-index: 20;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 22px;
    padding: 20px 0;
    border-bottom: 1px solid var(--border);
}

.brand {
    display: inline-flex;
    align-items: center;
    gap: 9px;
    flex-shrink: 0;
    font-weight: 800;
    font-size: 24px;
    letter-spacing: 4px;
}

.logo-mark {
    color: var(--blue2);
    font-size: 34px;
    font-weight: 900;
}

.logo-dot {
    color: var(--blue2);
}

.logo-img {
    display: block;
    width: 165px;
    max-width: 100%;
    height: auto;
    max-height: 60px;
}

.nav-toggle {
    display: none;
    align-items: center;
    justify-content: center;
    width: 46px;
    height: 44px;
    border: 1px solid var(--border);
    border-radius: 7px;
    background: #FFFFFF;
    color: var(--ink);
    font-size: 25px;
    cursor: pointer;
}

.navlinks {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    flex-wrap: wrap;
    gap: 22px;
    font-size: 14px;
    color: #4B5D72;
}

.navlinks a {
    transition: color .2s ease;
}

.navlinks a:hover {
    color: var(--blue2);
}

.navlinks .nav-cta {
    padding: 12px 16px;
    border-radius: 6px;
    background: var(--blue);
    color: #FFFFFF;
}

/* =====================================================
   CORTINAS AZULES
   ===================================================== */
#curtain-transition {
    position: fixed;
    inset: 0;
    z-index: 100000;
    display: block;
    overflow: hidden;
    pointer-events: none;
    visibility: hidden;
}

#curtain-transition.active {
    visibility: visible;
}

.curtain-panel {
    position: absolute;
    top: -1%;
    width: 52%;
    height: 102%;
    overflow: hidden;

    background:
        repeating-linear-gradient(
            90deg,
            rgba(2, 20, 49, .56) 0px,
            rgba(2, 20, 49, .32) 8px,
            rgba(78, 148, 221, .34) 18px,
            rgba(14, 56, 108, .25) 28px,
            rgba(2, 20, 49, .52) 42px
        ),
        linear-gradient(
            180deg,
            #174B82 0%,
            #0D3A70 52%,
            #082952 100%
        );

    box-shadow:
        inset 0 0 25px rgba(0, 0, 0, .18),
        inset 10px 0 16px rgba(255, 255, 255, .06);

    will-change: transform;
    transition: transform 1450ms cubic-bezier(.72, 0, .24, 1);
}

.curtain-panel::before {
    content: "";
    position: absolute;
    inset: 0;

    background: repeating-linear-gradient(
        90deg,
        rgba(0, 0, 0, .24) 0px,
        rgba(0, 0, 0, .10) 8px,
        rgba(255, 255, 255, .20) 18px,
        rgba(255, 255, 255, .04) 27px,
        rgba(0, 0, 0, .14) 39px
    );

    opacity: .9;
    mix-blend-mode: soft-light;
}

.curtain-panel::after {
    content: "";
    position: absolute;
    inset: 0;

    background: repeating-linear-gradient(
        0deg,
        rgba(255, 255, 255, .025) 0px,
        rgba(255, 255, 255, .025) 1px,
        transparent 1px,
        transparent 4px
    );
}

.curtain-panel.left {
    left: 0;
    transform: translateX(-102%);
    border-right: 3px solid rgba(132, 190, 245, .6);
}

.curtain-panel.right {
    right: 0;
    transform: translateX(102%);
    border-left: 3px solid rgba(132, 190, 245, .6);
}

#curtain-transition.closing .curtain-panel.left,
#curtain-transition.closing .curtain-panel.right {
    transform: translateX(0);
}

#curtain-transition.opening .curtain-panel.left {
    transform: translateX(-102%);
}

#curtain-transition.opening .curtain-panel.right {
    transform: translateX(102%);
}

.curtain-brand {
    position: absolute;
    z-index: 2;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(.92);

    color: #FFFFFF;
    font-size: clamp(25px, 4vw, 44px);
    font-weight: 900;
    letter-spacing: 7px;
    white-space: nowrap;
    opacity: 0;

    text-shadow: 0 4px 22px rgba(0, 0, 0, .28);

    transition:
        opacity 450ms ease,
        transform 450ms ease;
}

#curtain-transition.closing .curtain-brand {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1);
    transition-delay: 350ms;
}

#curtain-transition.opening .curtain-brand {
    opacity: 0;
    transform: translate(-50%, -50%) scale(1.06);
}

/* =====================================================
   PORTADA
   ===================================================== */
.hero {
    position: relative;
    display: flex;
    align-items: center;
    min-height: 580px;
    padding: 78px 0;
    overflow: hidden;
}

.hero-glow {
    position: absolute;
    top: 5px;
    right: -170px;
    width: 600px;
    height: 500px;
    background: radial-gradient(
        ellipse,
        rgba(0, 91, 255, .10),
        transparent 68%
    );
    pointer-events: none;
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 780px;
}

.eyebrow {
    margin-bottom: 20px;
    color: var(--blue2);
    font-size: 12px;
    font-weight: 800;
    line-height: 1.6;
    letter-spacing: 3px;
    text-transform: uppercase;
}

h1, h2, h3, p {
    margin-top: 0;
}

h1 {
    margin-bottom: 25px;
    font-size: clamp(45px, 7.3vw, 86px);
    font-weight: 800;
    line-height: 1;
    letter-spacing: -4px;
    overflow-wrap: anywhere;
}

h1 span,
.blue {
    color: var(--blue2);
}

.hero p {
    max-width: 590px;
    color: #52657B;
    font-size: 18px;
    line-height: 1.8;
}

.actions {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 30px;
}

.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 46px;
    padding: 13px 20px;
    border: 1px solid var(--blue);
    border-radius: 7px;
    background: var(--blue);
    color: #FFFFFF;
    font-weight: 700;
    text-align: center;
    cursor: pointer;
    transition: transform .2s ease, background .2s ease;
}

.btn:hover {
    transform: translateY(-2px);
    background: #218CFF;
}

.btn.outline {
    border-color: #AAB9C9;
    background: transparent;
    color: var(--ink);
}

.btn.outline:hover {
    border-color: var(--blue2);
}

.hero-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 23px;
    margin-top: 42px;
    color: #596B80;
    font-size: 12px;
}

.hero-meta b {
    color: var(--blue2);
}

/* =====================================================
   SECCIONES
   ===================================================== */
.section {
    padding: 75px 0;
    border-top: 1px solid #E2E8F0;
}

.section-head {
    max-width: 760px;
    margin-bottom: 34px;
}

.section-head h2 {
    margin-bottom: 15px;
    font-size: clamp(31px, 4.5vw, 52px);
    line-height: 1.1;
    letter-spacing: -2px;
}

.section-head p,
.body-copy {
    color: var(--muted);
    font-size: 16px;
    line-height: 1.8;
}

.grid3 {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 18px;
}

.grid2 {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    align-items: center;
    gap: 32px;
}

.card {
    min-width: 0;
    min-height: 215px;
    padding: 25px;
    border: 1px solid var(--border);
    border-radius: 10px;
    background: linear-gradient(145deg, #FFFFFF, #F8FAFC);
    transition: transform .25s ease, border-color .25s ease;
}

.card:hover {
    transform: translateY(-4px);
    border-color: #1269C5;
}

.num {
    margin-bottom: 22px;
    color: var(--blue2);
    font-size: 12px;
    font-weight: 800;
}

.card h3 {
    margin-bottom: 11px;
    font-size: 20px;
}

.card p {
    margin-bottom: 0;
    color: var(--muted);
    font-size: 14px;
    line-height: 1.75;
}

.band {
    margin-top: 24px;
    padding: 23px;
    border: 1px solid #D5E2F0;
    border-radius: 9px;
    background: linear-gradient(100deg, #F1F7FE, #FFFFFF);
    line-height: 1.7;
}

.band span {
    color: var(--muted);
}

/* =====================================================
   IMÁGENES DE PROYECTOS
   ===================================================== */
.project-image {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    min-width: 0;
    aspect-ratio: 4 / 3;
    overflow: hidden;
    border: 1px solid #D8E2ED;
    border-radius: 11px;
    background:
        radial-gradient(ellipse at 80% 10%, #E1F0FF, transparent 45%),
        linear-gradient(145deg, #F3F8FD, #EAF1F8);
}

.project-image img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.project-image.placeholder span {
    padding: 20px;
    color: #075EAD;
    font-size: 20px;
    font-weight: 800;
    text-align: center;
}

.project-copy {
    min-width: 0;
}

.project-copy h2 {
    margin-bottom: 17px;
    font-size: clamp(29px, 3.5vw, 39px);
    line-height: 1.15;
    letter-spacing: -1px;
    overflow-wrap: anywhere;
}

.project-copy p {
    color: var(--muted);
    line-height: 1.8;
}

.tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 17px;
}

.tag {
    padding: 7px 10px;
    border: 1px solid #C9DDF1;
    border-radius: 4px;
    background: #F0F6FC;
    color: #075EAD;
    font-size: 12px;
    line-height: 1.5;
}

/* =====================================================
   PROCESO
   ===================================================== */
.steps {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 15px;
}

.step {
    min-width: 0;
    padding-top: 18px;
    border-top: 2px solid var(--blue);
}

.step b {
    display: block;
    margin-bottom: 12px;
    color: var(--blue2);
    font-size: 12px;
}

.step h3 {
    font-size: 18px;
}

.step p {
    color: var(--muted);
    font-size: 14px;
    line-height: 1.7;
}

/* =====================================================
   PRÓXIMOS PROYECTOS
   ===================================================== */
.upcoming {
    max-width: 760px;
    padding: 5px 0 5px 22px;
    border-left: 3px solid var(--blue);
}

.upcoming p {
    color: var(--muted);
    line-height: 1.8;
}

/* =====================================================
   CONTACTO
   ===================================================== */
.cta {
    padding: 40px;
    border: 1px solid #C9DDF1;
    border-radius: 12px;
    background:
        radial-gradient(ellipse at 95% 5%, #E5F2FF, transparent 40%),
        linear-gradient(125deg, #F3F8FD, #FFFFFF);
}

.cta h2 {
    margin-bottom: 17px;
    font-size: clamp(34px, 5vw, 56px);
    line-height: 1.08;
    letter-spacing: -2px;
    overflow-wrap: anywhere;
}

.cta > p {
    max-width: 640px;
    color: var(--muted);
    line-height: 1.8;
}

.contact-form {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
    margin-top: 27px;
}

.contact-form label {
    display: block;
    margin-bottom: 7px;
    color: #43566D;
    font-size: 12px;
}

.contact-form input,
.contact-form select,
.contact-form textarea {
    display: block;
    width: 100%;
    min-width: 0;
    min-height: 45px;
    padding: 12px;
    border: 1px solid #CBD6E2;
    border-radius: 5px;
    background: #FFFFFF;
    color: #14263D;
    font-size: 16px;
}

.contact-form textarea {
    min-height: 110px;
    resize: vertical;
}

.contact-form input:focus,
.contact-form textarea:focus,
.contact-form select:focus {
    outline: 2px solid #B7D9FF;
    border-color: var(--blue);
}

.full {
    grid-column: 1 / -1;
}

/* =====================================================
   LOGOTIPOS
   ===================================================== */
.client-strip {
    margin-top: 35px;
}

.client-strip > .eyebrow {
    margin-bottom: 12px;
    text-align: center;
}

.client-logo-row {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 25px;
    width: 100%;
    padding: 10px 0;
}

.client-logo-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 220px;
    max-width: 100%;
    padding: 10px;
}

.client-logo-svg {
    display: block;
    width: 100%;
    max-width: 200px;
    max-height: 90px;
    height: auto;
    object-fit: contain;
}

.client-logo-mark {
    color: var(--blue2);
    font-size: 35px;
    font-weight: 900;
}

.client-logo-card small {
    margin-top: 5px;
    color: var(--muted);
    font-size: 11px;
    text-align: center;
}

/* =====================================================
   RASTRO DE LA N
   ===================================================== */
#trail-layer {
    position: fixed;
    inset: 0;
    z-index: 9999;
    overflow: hidden;
    pointer-events: none;
}

.trail-n {
    position: absolute;
    width: 23px;
    height: 27px;
    color: #087BFF;
    font-family: Arial, sans-serif;
    font-size: 25px;
    font-weight: 900;
    line-height: 27px;
    text-align: center;
    text-shadow: 0 0 7px #087BFF, 0 0 17px #005BFF;
    transform: translate(-50%, -50%);
    opacity: 0;
    will-change: transform, opacity;
}

/* =====================================================
   PIE
   ===================================================== */
footer {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 18px;
    padding: 28px 0 35px;
    border-top: 1px solid var(--border);
    color: #65768A;
    font-size: 12px;
    line-height: 1.7;
}

footer b {
    color: var(--ink);
    letter-spacing: 2px;
}

/* =====================================================
   TABLETAS
   ===================================================== */
@media (min-width: 761px) and (max-width: 1050px) {
    .wrap {
        width: 92%;
    }

    .navlinks {
        gap: 13px;
        font-size: 13px;
    }

    .grid3 {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .steps {
        grid-template-columns: repeat(2, minmax(0, 1fr));
        row-gap: 24px;
    }
}

/* =====================================================
   CELULARES
   ===================================================== */
@media (max-width: 760px) {
    .wrap {
        width: auto;
        max-width: 100%;
        margin: 0;
        padding-right: 18px;
        padding-left: 18px;
    }

    nav {
        flex-wrap: wrap;
        justify-content: space-between;
        gap: 12px;
        padding: 14px 0;
    }

    .brand {
        max-width: calc(100% - 58px);
        font-size: 21px;
        letter-spacing: 2px;
    }

    .logo-img {
        width: 145px;
        max-height: 48px;
    }

    .nav-toggle {
        display: inline-flex;
        flex-shrink: 0;
    }

    .navlinks {
        display: none;
        width: 100%;
        flex-direction: column;
        align-items: stretch;
        gap: 7px;
        padding: 8px 0 5px;
        font-size: 15px;
    }

    .navlinks.menu-open {
        display: flex;
    }

    .navlinks a {
        display: block;
        width: 100%;
        padding: 12px 13px;
        border: 1px solid #E1E8F0;
        border-radius: 6px;
        background: #FFFFFF;
    }

    .navlinks .nav-cta {
        border-color: var(--blue);
        background: var(--blue);
    }

    .hero {
        min-height: auto;
        padding: 55px 0 44px;
    }

    .hero-glow {
        top: 0;
        right: -150px;
        width: 300px;
        height: 300px;
    }

    .eyebrow {
        margin-bottom: 15px;
        font-size: 10px;
        letter-spacing: 2px;
    }

    h1 {
        font-size: clamp(38px, 10.5vw, 58px);
        line-height: 1.04;
        letter-spacing: -2px;
    }

    .hero p {
        font-size: 16px;
        line-height: 1.7;
    }

    .actions {
        flex-direction: column;
        align-items: stretch;
        gap: 10px;
    }

    .actions .btn {
        width: 100%;
    }

    .hero-meta {
        display: grid;
        grid-template-columns: 1fr;
        gap: 10px;
        margin-top: 27px;
    }

    .section {
        padding: 46px 0;
    }

    .section-head {
        margin-bottom: 23px;
    }

    .section-head h2 {
        font-size: clamp(29px, 7.8vw, 39px);
        line-height: 1.13;
        letter-spacing: -1px;
    }

    .section-head p,
    .body-copy {
        font-size: 15px;
        line-height: 1.75;
    }

    .grid3,
    .grid2,
    .steps {
        grid-template-columns: minmax(0, 1fr);
        gap: 17px;
    }

    .card {
        min-height: auto;
        padding: 21px;
    }

    .num {
        margin-bottom: 15px;
    }

    .band {
        padding: 19px;
    }

    .project-image {
        aspect-ratio: 4 / 3;
        height: auto;
        min-height: 0;
    }

    .project-copy h2 {
        font-size: 30px;
        line-height: 1.15;
        letter-spacing: -1px;
    }

    .tag {
        font-size: 12px;
    }

    .cta {
        padding: 22px 17px;
    }

    .cta h2 {
        font-size: clamp(31px, 8.5vw, 43px);
        line-height: 1.12;
        letter-spacing: -1px;
    }

    .contact-form {
        grid-template-columns: minmax(0, 1fr);
        gap: 15px;
    }

    .contact-form > div,
    .contact-form .full {
        width: 100%;
        min-width: 0;
        grid-column: 1 / -1;
    }

    .contact-form input,
    .contact-form select,
    .contact-form textarea {
        font-size: 16px;
        min-height: 47px;
    }

    .contact-form button {
        width: 100%;
        min-height: 48px;
    }

    .client-logo-row {
        gap: 10px;
    }

    .client-logo-card {
        width: min(100%, 220px);
    }

    footer {
        flex-direction: column;
        gap: 14px;
    }

    .curtain-panel {
        transition-duration: 950ms;
    }

    .curtain-brand {
        font-size: 24px;
        letter-spacing: 5px;
    }
}

/* Teléfonos pequeños */
@media (max-width: 380px) {
    .wrap {
        padding-right: 14px;
        padding-left: 14px;
    }

    h1 {
        font-size: 37px;
    }

    .navlinks a {
        font-size: 14px;
        padding: 11px;
    }

    .card {
        padding: 18px;
    }

    .cta {
        padding: 18px 14px;
    }
}

/* Menos movimiento si el dispositivo lo solicita */
@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        scroll-behavior: auto !important;
        animation-duration: .01ms !important;
        transition-duration: .01ms !important;
    }
}
</style>
</head>

<body>

<div id="trail-layer" aria-hidden="true"></div>

<div id="curtain-transition" aria-hidden="true">
    <div class="curtain-panel left"></div>
    <div class="curtain-panel right"></div>
    <div class="curtain-brand">
        NEXO<span style="color:#8FD8FF">.</span>
    </div>
</div>

<div class="wrap">

    <!-- NAVEGACIÓN -->
    <nav>
        <a class="brand" href="#inicio" aria-label="Nexo Promocional, inicio">
            __LOGO__
        </a>

        <button
            class="nav-toggle"
            id="nav-toggle"
            type="button"
            aria-label="Abrir menú"
            aria-expanded="false"
            aria-controls="navlinks"
        >☰</button>

        <div class="navlinks" id="navlinks">
            <a href="#inicio">Inicio</a>
            <a href="#servicios">Servicios</a>
            <a href="#proyectos">Proyectos</a>
            <a href="#proximos">Próximos proyectos</a>
            <a class="nav-cta" href="#contacto">Hablemos ↗</a>
        </div>
    </nav>

    <!-- INICIO -->
    <section class="hero" id="inicio">
        <div class="hero-glow"></div>

        <div class="hero-content">
            <div class="eyebrow">
                Nexo Promocional · Soluciones para empresas
            </div>

            <h1>
                Tu proyecto.<br>
                Muchas ideas.<br>
                <span>Un solo Nexo.</span>
            </h1>

            <p>
                Integramos productos promocionales, impresión, diseño y
                soluciones digitales para que tu marca llegue más lejos,
                con menos complicaciones.
            </p>

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

    <!-- PROPUESTA DE VALOR -->
    <section class="section" id="enfoque">
        <div class="section-head">
            <div class="eyebrow">Una solución integral</div>

            <h2>
                Todo conectado.<br>
                <span class="blue">Todo más fácil.</span>
            </h2>

            <p>
                Un solo punto de contacto para coordinar materiales,
                comunicación y recursos que tu empresa necesita para destacar.
            </p>
        </div>

        <div class="grid3">
            <article class="card">
                <div class="num">01 / PLANEA</div>
                <h3>Escuchamos tu necesidad</h3>
                <p>Entendemos tu objetivo, tu público y los materiales que necesitas.</p>
            </article>

            <article class="card">
                <div class="num">02 / INTEGRAMOS</div>
                <h3>Coordinamos soluciones</h3>
                <p>Conectamos diseño, producción e impresión para resolver el proyecto.</p>
            </article>

            <article class="card">
                <div class="num">03 / ENTREGAMOS</div>
                <h3>Acompañamos el proceso</h3>
                <p>Damos seguimiento a los detalles de los productos y servicios acordados.</p>
            </article>
        </div>

        <div class="band">
            <strong>Menos proveedores que coordinar. Más claridad en cada proyecto.</strong>
            <br>
            <span>Desde una pieza promocional hasta los materiales para un evento o una campaña.</span>
        </div>
    </section>

    <!-- SERVICIOS -->
    <section class="section" id="servicios">
        <div class="section-head">
            <div class="eyebrow">Qué hacemos</div>

            <h2>
                Todo lo que tu marca necesita para
                <span class="blue">hacerse notar.</span>
            </h2>

            <p>
                Una oferta flexible para empresas, asociaciones,
                instituciones, eventos y comercios.
            </p>
        </div>

        <div class="grid3">
            <article class="card">
                <div class="num">01</div>
                <h3>Productos promocionales</h3>
                <p>Tazas, plumas, bolsas, pines, gafetes y artículos personalizados.</p>
            </article>

            <article class="card">
                <div class="num">02</div>
                <h3>Impresión y gran formato</h3>
                <p>Lonas, banners, roll-ups, muros gráficos, viniles, carteles y señalización.</p>
            </article>

            <article class="card">
                <div class="num">03</div>
                <h3>Papelería y comunicación</h3>
                <p>Folletos, volantes, dípticos, trípticos, carpetas, invitaciones y materiales institucionales.</p>
            </article>

            <article class="card">
                <div class="num">04</div>
                <h3>Diseño gráfico</h3>
                <p>Materiales para eventos, campañas, presentaciones y comunicación de marca.</p>
            </article>

            <article class="card">
                <div class="num">05</div>
                <h3>Eventos y acreditaciones</h3>
                <p>Boletos digitales, gafetes, códigos QR y materiales de apoyo para registro.</p>
            </article>

            <article class="card">
                <div class="num">06</div>
                <h3>Soluciones digitales</h3>
                <p>Páginas informativas, formularios y herramientas sencillas para compartir información.</p>
            </article>
        </div>
    </section>

    <!-- PROYECTOS -->
    <section class="section" id="proyectos">
        <div class="section-head">
            <div class="eyebrow">Nuestra experiencia</div>

            <h2>
                Ideas que pasan del diseño
                <span class="blue">a la realidad.</span>
            </h2>

            <p>
                Convertimos necesidades concretas en materiales útiles,
                coordinados y alineados con cada proyecto.
            </p>
        </div>

        <div class="grid2">
            __AMH_IMAGE__

            <div class="project-copy">
                <div class="eyebrow">Caso de éxito · AMH</div>
                <h2>Materiales que trabajan en conjunto.</h2>

                <p>
                    Para la Asociación Mexicana de Hepatología se coordinaron
                    materiales promocionales y gráficos para actividades y eventos.
                </p>

                <div class="tags">
                    <span class="tag">Tazas y plumas</span>
                    <span class="tag">Gafetes</span>
                    <span class="tag">Roll-up</span>
                    <span class="tag">Muro gráfico 3×3</span>
                    <span class="tag">Material del evento</span>
                </div>
            </div>
        </div>

        <div style="height:42px"></div>

        <div class="grid2">
            <div class="project-copy">
                <div class="eyebrow">Producción y comunicación</div>
                <h2>Una marca consistente en cada detalle.</h2>

                <p>
                    Integramos distintas piezas para que los materiales de
                    comunicación mantengan una presentación coherente con
                    el propósito de cada cliente.
                </p>

                <div class="tags">
                    <span class="tag">Planeación</span>
                    <span class="tag">Producción</span>
                    <span class="tag">Impresión</span>
                    <span class="tag">Entrega</span>
                </div>
            </div>

            __PRODUCTS_IMAGE__
        </div>
    </section>

    <!-- PRÓXIMOS PROYECTOS -->
    <section class="section" id="proximos">
        <div class="section-head">
            <div class="eyebrow">Lo que viene</div>
            <h2>Próximos <span class="blue">proyectos.</span></h2>
        </div>

        <div class="upcoming">
            <p>
                Estamos preparando nuevas colaboraciones y soluciones.
                Cuéntanos qué proyecto te gustaría hacer realidad.
            </p>

            <a class="btn" href="#contacto">Platiquemos de tu proyecto ↗</a>
        </div>
    </section>

    <!-- ROOTHÚA -->
    <section class="section" id="roothua">
        <div class="grid2">
            __ROOTHUA_IMAGE__

            <div class="project-copy">
                <div class="eyebrow">Caso de éxito · Roothúa</div>

                <h2>Publicidad y contenido para conectar con su audiencia.</h2>

                <p>
                    Desarrollamos publicidad, manejo de redes sociales,
                    creación de contenido y edición de imágenes para
                    fortalecer la comunicación de Roothúa.
                </p>

                <div class="tags">
                    <span class="tag">Publicidad</span>
                    <span class="tag">Manejo de redes sociales</span>
                    <span class="tag">Creación de contenido</span>
                    <span class="tag">Edición de imágenes</span>
                </div>
            </div>
        </div>
    </section>

    <!-- PROCESO -->
    <section class="section" id="proceso">
        <div class="section-head">
            <div class="eyebrow">Cómo trabajamos</div>

            <h2>
                Un proceso claro,<br>
                <span class="blue">de principio a fin.</span>
            </h2>

            <p>Queremos que solicitar tus materiales sea más sencillo.</p>
        </div>

        <div class="steps">
            <div class="step">
                <b>01 / CONTACTO</b>
                <h3>Nos contactas</h3>
                <p>Cuéntanos qué necesitas.</p>
            </div>

            <div class="step">
                <b>02 / PLANEACIÓN</b>
                <h3>Preparamos</h3>
                <p>Definimos materiales y alcance.</p>
            </div>

            <div class="step">
                <b>03 / PROPUESTA</b>
                <h3>Cotizamos</h3>
                <p>Revisamos opciones y tiempos.</p>
            </div>

            <div class="step">
                <b>04 / SEGUIMIENTO</b>
                <h3>Coordinamos</h3>
                <p>Damos seguimiento al pedido.</p>
            </div>
        </div>
    </section>

    <!-- CONTACTO -->
    <section class="section" id="contacto">
        <div class="cta">
            <div class="eyebrow">Hagamos equipo</div>

            <h2>
                ¿Qué necesitas<br>
                <span class="blue">resolver hoy?</span>
            </h2>

            <p>
                Cuéntanos tu idea. Te ayudaremos a identificar los materiales
                y servicios que pueden hacer realidad tu proyecto.
            </p>

            <form class="contact-form" id="contact-form">
                <div>
                    <label for="nombre">Nombre *</label>
                    <input id="nombre" name="nombre" required
                           autocomplete="name" placeholder="Tu nombre">
                </div>

                <div>
                    <label for="empresa">Empresa u organización</label>
                    <input id="empresa" name="empresa"
                           autocomplete="organization"
                           placeholder="Nombre de tu organización">
                </div>

                <div>
                    <label for="correo">Correo electrónico *</label>
                    <input id="correo" name="correo" type="email" required
                           autocomplete="email" placeholder="tu@correo.com">
                </div>

                <div>
                    <label for="tipo">Servicio que necesitas</label>
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

                <div class="full">
                    <label for="mensaje">Cuéntanos sobre tu proyecto *</label>
                    <textarea id="mensaje" name="mensaje" required
                              placeholder="¿Qué necesitas, para cuándo y en qué cantidad?"></textarea>
                </div>

                <div class="full">
                    <button class="btn" type="submit">Preparar solicitud ↗</button>
                </div>
            </form>

            <p id="form-result" aria-live="polite"
               style="margin-top:16px"></p>

            <div id="contact-links" style="margin-top:16px"></div>
        </div>

        <div class="client-strip">
            <div class="eyebrow">Clientes y proyectos</div>
            <div class="client-logo-row">__CLIENT_LOGOS__</div>
        </div>
    </section>

    <!-- PIE -->
    <footer>
        <div>
            <b>NEXO PROMOCIONAL</b><br>
            Ideas que conectan. Soluciones que avanzan.
        </div>

        <div>Productos · Impresión · Diseño · Soluciones digitales</div>

        <div>© Nexo Promocional</div>
    </footer>

</div>

<script>
/* =====================================================
   MENÚ HAMBURGUESA PARA MÓVILES
   ===================================================== */
(function () {
    const toggle = document.getElementById("nav-toggle");
    const menu = document.getElementById("navlinks");

    if (!toggle || !menu) return;

    function closeMenu() {
        menu.classList.remove("menu-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.setAttribute("aria-label", "Abrir menú");
        toggle.textContent = "☰";
    }

    toggle.addEventListener("click", function () {
        const isOpen = menu.classList.toggle("menu-open");

        toggle.setAttribute("aria-expanded", String(isOpen));
        toggle.setAttribute(
            "aria-label",
            isOpen ? "Cerrar menú" : "Abrir menú"
        );
        toggle.textContent = isOpen ? "×" : "☰";
    });

    menu.querySelectorAll('a[href^="#"]').forEach(function (link) {
        link.addEventListener("click", closeMenu);
    });

    window.addEventListener("resize", function () {
        if (window.innerWidth > 760) closeMenu();
    });
})();


/* =====================================================
   NAVEGACIÓN CON CORTINAS
   ===================================================== */
(function () {
    const curtain = document.getElementById("curtain-transition");

    if (!curtain) return;

    let transitioning = false;
    const reduceMotion = window.matchMedia(
        "(prefers-reduced-motion: reduce)"
    ).matches;

    const closeDuration = reduceMotion ? 200 : 1450;
    const openDuration = reduceMotion ? 200 : 1450;
    const holdDuration = reduceMotion ? 80 : 300;

    function scrollToTarget(target) {
        const frame = window.frameElement;

        if (!frame) {
            target.scrollIntoView({
                behavior: "auto",
                block: "start"
            });
            return;
        }

        try {
            const parentWindow = window.parent;
            const parentDocument = frame.ownerDocument;

            const targetTop =
                frame.getBoundingClientRect().top +
                target.getBoundingClientRect().top;

            let container = frame.parentElement;

            while (
                container &&
                container !== parentDocument.body
            ) {
                const overflowY =
                    parentWindow.getComputedStyle(container).overflowY;

                if (
                    ["auto", "scroll", "overlay"].includes(overflowY) &&
                    container.scrollHeight > container.clientHeight
                ) {
                    break;
                }

                container = container.parentElement;
            }

            if (
                container &&
                container !== parentDocument.body
            ) {
                container.scrollTo({
                    top:
                        container.scrollTop +
                        targetTop -
                        container.getBoundingClientRect().top -
                        24,
                    behavior: "auto"
                });
            } else {
                const scrollRoot =
                    parentDocument.scrollingElement ||
                    parentDocument.documentElement;

                parentWindow.scrollTo({
                    top: scrollRoot.scrollTop + targetTop - 24,
                    behavior: "auto"
                });
            }
        } catch (error) {
            target.scrollIntoView({
                behavior: "auto",
                block: "start"
            });
        }
    }

    document.addEventListener("click", function (event) {
        const link = event.target instanceof Element
            ? event.target.closest('a[href^="#"]')
            : null;

        if (!link) return;

        const id = link.getAttribute("href").slice(1);
        const target = document.getElementById(id);

        if (!target) return;

        event.preventDefault();

        if (transitioning) return;

        transitioning = true;

        curtain.classList.remove("opening");
        curtain.classList.add("active", "closing");

        window.setTimeout(function () {
            scrollToTarget(target);

            window.setTimeout(function () {
                curtain.classList.remove("closing");
                curtain.classList.add("opening");

                window.setTimeout(function () {
                    curtain.classList.remove("active", "opening");
                    transitioning = false;
                }, openDuration);

            }, holdDuration);

        }, closeDuration);
    }, true);
})();


/* =====================================================
   RASTRO DE LA N EN ESCRITORIO
   ===================================================== */
(function () {
    const layer = document.getElementById("trail-layer");

    if (
        !layer ||
        !window.matchMedia("(hover: hover) and (pointer: fine)").matches
    ) {
        return;
    }

    const total = 11;
    const items = [];

    for (let i = 0; i < total; i++) {
        const el = document.createElement("span");
        el.className = "trail-n";
        el.textContent = "N";
        layer.appendChild(el);

        items.push({
            el: el,
            x: -100,
            y: -100
        });
    }

    let mouseX = -100;
    let mouseY = -100;
    let visible = false;

    window.addEventListener("mousemove", function (event) {
        mouseX = event.clientX;
        mouseY = event.clientY;
        visible = true;
    }, { passive: true });

    window.addEventListener("mouseout", function (event) {
        if (!event.relatedTarget) visible = false;
    });

    window.addEventListener("blur", function () {
        visible = false;
    });

    function animate() {
        let targetX = mouseX;
        let targetY = mouseY;

        items.forEach(function (item, index) {
            const lag = 0.29 - index * 0.014;

            item.x += (targetX - item.x) * lag;
            item.y += (targetY - item.y) * lag;

            const progress = 1 - index / total;
            const scale = 0.45 + progress * 0.55;
            const opacity = visible
                ? Math.pow(progress, 1.45) * 0.9
                : 0;

            item.el.style.left = item.x + "px";
            item.el.style.top = item.y + "px";
            item.el.style.opacity = opacity;

            item.el.style.transform =
                "translate(-50%,-50%) scale(" +
                scale +
                ") rotate(-8deg)";

            item.el.style.filter =
                "blur(" + (1 - progress) * 1.3 + "px)";

            targetX = item.x + (mouseX - item.x) * 0.12;
            targetY = item.y + (mouseY - item.y) * 0.12;
        });

        requestAnimationFrame(animate);
    }

    animate();
})();


/* =====================================================
   FORMULARIO DE CONTACTO
   ===================================================== */
(function () {
    const form = document.getElementById("contact-form");
    const result = document.getElementById("form-result");
    const links = document.getElementById("contact-links");

    const emailDestino = __EMAIL_JSON__;
    const whatsappDestino = __WHATSAPP_JSON__;

    if (whatsappDestino) {
        const a = document.createElement("a");

        a.className = "btn outline";
        a.target = "_blank";
        a.rel = "noopener noreferrer";
        a.href = "https://wa.me/" + whatsappDestino;
        a.textContent = "También puedes escribirnos por WhatsApp";

        links.appendChild(a);
    }

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const data = new FormData(form);

        const nombre = String(data.get("nombre") || "").trim();
        const correo = String(data.get("correo") || "").trim();
        const empresa = String(data.get("empresa") || "").trim();
        const tipo = String(data.get("tipo") || "");
        const mensaje = String(data.get("mensaje") || "").trim();

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

            result.textContent =
                "Se abrirá tu aplicación de correo para revisar y enviar la solicitud.";
        } else {
            const contenido = asunto + "\n\n" + cuerpo;
            const blob = new Blob(
                [contenido],
                { type: "text/plain;charset=utf-8" }
            );

            const url = URL.createObjectURL(blob);
            const a = document.createElement("a");

            a.href = url;
            a.download = "solicitud-nexo.txt";
            document.body.appendChild(a);
            a.click();
            a.remove();

            window.setTimeout(function () {
                URL.revokeObjectURL(url);
            }, 1000);

            result.textContent =
                "La solicitud se descargó como archivo de texto. "
                + "Configura CORREO en app.py para habilitar el envío por correo.";
        }
    });
})();
</script>

</body>
</html>
"""


# =====================================================
# REEMPLAZAR CONTENIDO DINÁMICO
# =====================================================
pagina = pagina.replace("__LOGO__", logo_html)
pagina = pagina.replace("__AMH_IMAGE__", amh_imagen)
pagina = pagina.replace("__PRODUCTS_IMAGE__", productos_imagen)
pagina = pagina.replace("__ROOTHUA_IMAGE__", roothua_imagen)
pagina = pagina.replace("__CLIENT_LOGOS__", clientes_logos)

pagina = pagina.replace(
    "__EMAIL_JSON__",
    json.dumps(CORREO.strip()),
)

pagina = pagina.replace(
    "__WHATSAPP_JSON__",
    json.dumps("".join(c for c in WHATSAPP if c.isdigit())),
)


# =====================================================
# RENDERIZAR
# =====================================================
components.html(
    pagina,
    height=7200,
    scrolling=True,
)
