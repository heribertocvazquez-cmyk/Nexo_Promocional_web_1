
import streamlit as st
from pathlib import Path
import html

st.set_page_config(
    page_title="Nexo Promocional | Ideas que conectan",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------
BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"

CORREO = ""       # Agrega aquí el correo comercial
TELEFONO = ""     # Agrega aquí el teléfono
WHATSAPP = ""     # Agrega aquí el número con código de país, solo dígitos

def asset(nombre):
    ruta = ASSETS / nombre
    return str(ruta) if ruta.exists() else None

def seccion(titulo, texto=None, etiqueta=None):
    tag = f'<div class="eyebrow">{html.escape(etiqueta)}</div>' if etiqueta else ""
    desc = f'<p class="section-desc">{html.escape(texto)}</p>' if texto else ""
    st.markdown(
        f'<div class="section-heading">{tag}'
        f'<h2>{html.escape(titulo)}</h2>{desc}</div>',
        unsafe_allow_html=True,
    )

def tarjeta(numero, titulo, descripcion):
    st.markdown(
        f"""
        <div class="service-card">
            <div class="service-number">{numero}</div>
            <h3>{html.escape(titulo)}</h3>
            <p>{html.escape(descripcion)}</p>
            <div class="card-line"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --------------------------------------------------
# ESTILO VISUAL
# --------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #09223D;
    --navy2: #103858;
    --cyan: #16C1C8;
    --cyan-light: #DDF9F8;
    --ink: #14283D;
    --muted: #64758A;
    --paper: #F5F8FB;
    --white: #FFFFFF;
}

html { scroll-behavior: smooth; }
.stApp {
    background: var(--white);
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
}
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stSidebar"] { display: none; }
.block-container {
    max-width: 1320px;
    padding: 1rem 4.2rem 3rem;
}
h1, h2, h3, h4 {
    font-family: 'Manrope', sans-serif !important;
    letter-spacing: -0.045em;
}
p { line-height: 1.7; }
a { text-decoration: none; }

/* Navegación */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    padding: 12px 0 24px;
    border-bottom: 1px solid #E7EDF3;
    margin-bottom: 28px;
}
.brand {
    font-family: 'Manrope', sans-serif;
    font-size: 1.4rem;
    font-weight: 800;
    letter-spacing: -1px;
    color: var(--navy);
}
.brand span { color: var(--cyan); }
.navlinks {
    display: flex;
    gap: 23px;
    flex-wrap: wrap;
    align-items: center;
}
.navlinks a {
    color: var(--navy);
    font-size: .87rem;
    font-weight: 600;
}
.navlinks a:hover { color: #009DA8; }
.nav-cta {
    background: var(--navy);
    color: white !important;
    padding: 11px 17px;
    border-radius: 6px;
}

/* Hero */
.hero {
    position: relative;
    overflow: hidden;
    background:
      radial-gradient(circle at 87% 22%, rgba(22,193,200,.30), transparent 29%),
      radial-gradient(circle at 10% 100%, rgba(25,111,164,.35), transparent 36%),
      linear-gradient(120deg, #071D34, #103858 70%, #0B334C);
    color: white;
    border-radius: 18px;
    padding: clamp(36px, 6vw, 82px);
    min-height: 450px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    animation: rise .8s ease both;
}
.hero:after {
    content: "";
    position: absolute;
    width: 290px;
    height: 290px;
    right: -85px;
    bottom: -140px;
    border: 1px solid rgba(255,255,255,.22);
    border-radius: 50%;
    box-shadow: 0 0 0 32px rgba(255,255,255,.035),
                0 0 0 65px rgba(255,255,255,.025);
}
.eyebrow {
    text-transform: uppercase;
    letter-spacing: .16em;
    font-size: .76rem;
    font-weight: 800;
    color: #009DA8;
    margin-bottom: 14px;
}
.hero .eyebrow { color: #66F0ED; }
.hero h1 {
    color: white;
    font-size: clamp(2.8rem, 6.2vw, 5.5rem);
    line-height: .99;
    max-width: 850px;
    margin: 0 0 24px;
    font-weight: 800;
}
.hero h1 span { color: #5CE4E1; }
.hero p {
    color: #D9E9F4;
    max-width: 650px;
    font-size: 1.12rem;
    margin: 0 0 28px;
}
.hero-actions { display:flex; flex-wrap:wrap; gap:12px; }
.hero-button {
    display:inline-block;
    background:var(--cyan);
    color:var(--navy) !important;
    font-weight:800;
    padding:14px 22px;
    border-radius:6px;
    transition:transform .2s, background .2s;
}
.hero-button:hover { transform:translateY(-3px); background:#6CE6E4; }
.hero-button.secondary {
    background:transparent;
    color:white !important;
    border:1px solid rgba(255,255,255,.45);
}
.hero-foot {
    display:flex;
    gap:26px;
    flex-wrap:wrap;
    margin-top:38px;
    color:#D5E7F2;
    font-size:.85rem;
}
.hero-foot b { color:#66F0ED; }

/* Secciones */
.section-heading { padding: 66px 0 26px; }
.section-heading h2 {
    font-size: clamp(2rem, 4.4vw, 3.7rem);
    line-height: 1.06;
    color: var(--navy);
    max-width: 850px;
    margin: 0 0 14px;
}
.section-desc {
    color: var(--muted);
    font-size: 1.04rem;
    max-width: 760px;
    margin: 0;
}
.service-card {
    height: 100%;
    min-height: 225px;
    box-sizing: border-box;
    background: #F5F8FB;
    border: 1px solid #E6EDF3;
    border-radius: 12px;
    padding: 25px;
    transition: transform .25s, box-shadow .25s, border .25s;
}
.service-card:hover {
    transform: translateY(-7px);
    border-color: #8BE5E4;
    box-shadow: 0 16px 36px rgba(9,34,61,.09);
}
.service-number {
    color: #009DA8;
    font-weight: 800;
    font-size: .82rem;
    margin-bottom: 26px;
}
.service-card h3 {
    color: var(--navy);
    font-size: 1.25rem;
    margin: 0 0 10px;
}
.service-card p { color: var(--muted); font-size: .94rem; }
.card-line {
    width: 42px; height: 3px;
    background: var(--cyan);
    margin-top: 20px;
    border-radius: 5px;
}
.pill {
    display:inline-block;
    padding:7px 11px;
    border-radius:5px;
    background:rgba(22,193,200,.13);
    color:#007C87;
    font-size:.8rem;
    font-weight:700;
    margin:0 5px 8px 0;
}

/* Banda y casos */
.trust-band {
    margin-top: 50px;
    background: var(--cyan-light);
    border-radius: 12px;
    padding: 25px 30px;
    color: var(--navy);
}
.trust-band strong { font-size:1.1rem; }
.case-card {
    background: var(--navy);
    color: white;
    border-radius: 12px;
    overflow: hidden;
    height: 100%;
}
.case-copy { padding: 24px; }
.case-card h3 { color:white; font-size:1.45rem; margin:0 0 10px; }
.case-card p { color:#D2E2EE; font-size:.94rem; }
.case-label {
    font-size:.73rem; text-transform:uppercase; letter-spacing:.12em;
    color:#64E4E1; font-weight:800; margin-bottom:12px;
}
.case-placeholder {
    height: 185px;
    display:flex;
    align-items:center;
    justify-content:center;
    text-align:center;
    padding:20px;
    color:#6CE6E4;
    font-size:1.4rem;
    font-family:'Manrope', sans-serif;
    font-weight:800;
    background:radial-gradient(circle at 80% 20%, #1A6680, transparent 40%),
               linear-gradient(135deg,#0A2039,#16425D);
}

/* CTA y pie */
.cta-panel {
    background: linear-gradient(120deg, #0A2039, #10415B);
    color:white;
    border-radius:16px;
    padding:clamp(30px,5vw,60px);
    margin-top:68px;
}
.cta-panel h2 {
    color:white;
    font-size:clamp(2rem,4vw,3.5rem);
    margin:0 0 15px;
    line-height:1.08;
}
.cta-panel p { color:#D5E7F2; max-width:690px; }
.footer {
    border-top:1px solid #E6EDF3;
    padding:24px 0 10px;
    margin-top:45px;
    display:flex;
    flex-wrap:wrap;
    justify-content:space-between;
    gap:16px;
    color:#718196;
    font-size:.83rem;
}
.footer strong { color:var(--navy); }
div[data-testid="stForm"] {
    border:1px solid #E1EAF1;
    border-radius:12px;
    padding:22px;
    background:#F8FAFC;
}
div.stButton > button, div[data-testid="stFormSubmitButton"] button {
    background:var(--cyan);
    color:var(--navy);
    border:0;
    border-radius:6px;
    font-weight:800;
    min-height:44px;
}
div.stButton > button:hover, div[data-testid="stFormSubmitButton"] button:hover {
    background:#62E1DF;
    color:var(--navy);
    border:0;
}
div[data-testid="stImage"] img { border-radius:10px; }
@keyframes rise {
    from { opacity:0; transform:translateY(16px); }
    to { opacity:1; transform:translateY(0); }
}
@media (max-width: 800px) {
    .block-container { padding: .7rem 1rem 2rem; }
    .navbar { align-items:flex-start; flex-direction:column; }
    .navlinks { gap:12px; }
    .hero { min-height:0; padding:34px 24px; }
    .hero h1 { font-size:2.8rem; }
    .section-heading { padding-top:45px; }
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# BARRA DE NAVEGACIÓN
# --------------------------------------------------
st.markdown("""
<div class="navbar">
  <a class="brand" href="#inicio">NEXO<span>✦</span></a>
  <div class="navlinks">
    <a href="#servicios">Servicios</a>
    <a href="#experiencia">Experiencia</a>
    <a href="#proyectos">Proyectos</a>
    <a href="#roothua">Soluciones integrales</a>
    <a class="nav-cta" href="#contacto">Hablemos ↗</a>
  </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HERO
# --------------------------------------------------
st.markdown("""
<div id="inicio" class="hero">
  <div class="eyebrow">Nexo Promocional · Soluciones para empresas</div>
  <h1>Tu proyecto.<br>Muchas ideas.<br><span>Un solo Nexo.</span></h1>
  <p>
    Integramos productos promocionales, impresión, diseño y soluciones
    digitales para que tu marca llegue más lejos, con menos complicaciones.
  </p>
  <div class="hero-actions">
    <a class="hero-button" href="#contacto">Cuéntanos tu proyecto ↗</a>
    <a class="hero-button secondary" href="#servicios">Explorar servicios ↓</a>
  </div>
  <div class="hero-foot">
    <span><b>01</b> · Atención cercana</span>
    <span><b>02</b> · Soluciones integrales</span>
    <span><b>03</b> · De la idea a la entrega</span>
  </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# PROPUESTA DE VALOR
# --------------------------------------------------
seccion(
    "Todo conectado. Todo más fácil.",
    "Un solo punto de contacto para coordinar materiales, comunicación "
    "y recursos que tu empresa necesita para destacar.",
    "Una solución integral"
)

c1, c2, c3 = st.columns(3, gap="medium")
with c1:
    tarjeta("01 / PLANEA", "Escuchamos tu necesidad",
            "Entendemos tu objetivo, el público y los materiales que necesitas.")
with c2:
    tarjeta("02 / INTEGRAMOS", "Coordinamos las soluciones",
            "Conectamos diseño, producción e impresión para resolver el proyecto.")
with c3:
    tarjeta("03 / ENTREGAMOS", "Acompañamos el proceso",
            "Damos seguimiento a los detalles para ayudarte a llegar a tiempo.")

st.markdown("""
<div class="trust-band">
  <strong>Menos proveedores que coordinar. Más claridad en cada proyecto.</strong>
  <div style="margin-top:7px;color:#49657B">
    Desde una pieza promocional hasta los materiales para un evento o una campaña.
  </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SERVICIOS
# --------------------------------------------------
st.markdown('<div id="servicios"></div>', unsafe_allow_html=True)
seccion(
    "Todo lo que tu marca necesita para hacerse notar.",
    "Una oferta flexible para empresas, asociaciones, instituciones, eventos y comercios.",
    "Qué hacemos"
)

servicios = [
    ("01", "Productos promocionales",
     "Tazas, plumas, bolsas, pines, gafetes y artículos personalizados."),
    ("02", "Impresión y gran formato",
     "Lonas, banners, roll-ups, muros gráficos, viniles, carteles y señalización."),
    ("03", "Papelería y comunicación",
     "Folletos, volantes, dípticos, trípticos, carpetas, invitaciones y materiales institucionales."),
    ("04", "Diseño gráfico",
     "Diseño de materiales para eventos, campañas, presentaciones y comunicación de marca."),
    ("05", "Eventos y acreditaciones",
     "Boletos digitales, gafetes, códigos QR y materiales de apoyo para registro."),
    ("06", "Soluciones digitales",
     "Páginas informativas, formularios y herramientas sencillas para compartir información.")
]
for inicio in range(0, len(servicios), 3):
    columnas = st.columns(3, gap="medium")
    for columna, servicio in zip(columnas, servicios[inicio:inicio+3]):
        with columna:
            tarjeta(*servicio)

# --------------------------------------------------
# EXPERIENCIA / PORTAFOLIO
# --------------------------------------------------
st.markdown('<div id="experiencia"></div>', unsafe_allow_html=True)
seccion(
    "Ideas que pasan del diseño a la realidad.",
    "Trabajamos para convertir necesidades concretas en materiales útiles, "
    "bien coordinados y alineados con cada proyecto.",
    "Nuestra experiencia"
)

amh_img = asset("amh-entrega-01.jpg")
prod_img = asset("productos-promocionales.jpg")
logo_amh = asset("logo-amh.png")

c1, c2 = st.columns([1.05, 1], gap="large")
with c1:
    if amh_img:
        st.image(amh_img, use_container_width=True)
    else:
        st.markdown("""
        <div class="case-placeholder">
          AMH<br>Productos y materiales para eventos
        </div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div style="padding:8px 0 18px">
      <div class="eyebrow">Caso de trabajo · AMH</div>
      <h2 style="font-size:2.25rem;color:#09223D;line-height:1.1">
        Materiales que trabajan en conjunto.
      </h2>
      <p style="color:#64758A">
        Para la Asociación Mexicana de Hepatología se coordinaron materiales
        promocionales y gráficos para actividades y eventos.
      </p>
      <span class="pill">Tazas y plumas</span>
      <span class="pill">Gafetes</span>
      <span class="pill">Roll-up</span>
      <span class="pill">Muro gráfico 3×3</span>
      <span class="pill">Material digital</span>
    </div>
    """, unsafe_allow_html=True)

st.divider()

c1, c2 = st.columns([1, 1.05], gap="large")
with c1:
    st.markdown("""
    <div style="padding:8px 0 18px">
      <div class="eyebrow">De la idea a la entrega</div>
      <h2 style="font-size:2.25rem;color:#09223D;line-height:1.1">
        Una marca consistente en cada detalle.
      </h2>
      <p style="color:#64758A">
        Integramos diferentes piezas para que los materiales de comunicación
        mantengan una presentación coherente con el propósito de cada cliente.
      </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="padding:17px 0;border-top:1px solid #E6EDF3">
      <strong style="color:#09223D">01 / Planeación</strong>
      <div style="color:#64758A;margin-top:5px">Definimos qué necesita el proyecto.</div>
    </div>
    <div style="padding:17px 0;border-top:1px solid #E6EDF3">
      <strong style="color:#09223D">02 / Producción</strong>
      <div style="color:#64758A;margin-top:5px">Coordinamos materiales y acabados.</div>
    </div>
    <div style="padding:17px 0;border-top:1px solid #E6EDF3">
      <strong style="color:#09223D">03 / Entrega</strong>
      <div style="color:#64758A;margin-top:5px">Damos seguimiento a los productos acordados.</div>
    </div>
    """, unsafe_allow_html=True)
with c2:
    if prod_img:
        st.image(prod_img, use_container_width=True)
    else:
        st.markdown("""
        <div class="case-placeholder" style="height:330px">
          NEXO PROMOCIONAL<br>Productos · Impresión · Diseño
        </div>""", unsafe_allow_html=True)

# --------------------------------------------------
# SOLUCIONES INTEGRALES / ROOTHÚA
# --------------------------------------------------
st.markdown('<div id="roothua"></div>', unsafe_allow_html=True)
seccion(
    "Más capacidades. Más posibilidades.",
    "Además de los materiales promocionales, podemos conectar proyectos con "
    "soluciones complementarias de diseño, fabricación y renovación.",
    "Ecosistema de soluciones"
)

roothua_img = asset("roothua-proyecto.jpg")
c1, c2 = st.columns([1, 1.1], gap="large")
with c1:
    if roothua_img:
        st.image(roothua_img, use_container_width=True)
    else:
        st.markdown("""
        <div class="case-placeholder" style="height:260px">
          ROOTHÚA<br>Mobiliario · Diseño · Renovación
        </div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div style="padding:10px 0">
      <div class="eyebrow">Roothúa · Mobiliario y proyectos</div>
      <h2 style="font-size:2.2rem;color:#09223D;line-height:1.1">
        Soluciones que van más allá de lo promocional.
      </h2>
      <p style="color:#64758A">
        La experiencia vinculada con Roothúa complementa las capacidades
        del proyecto con mobiliario, fabricación sobre medida, tapicería
        y renovación de espacios.
      </p>
      <span class="pill">Mobiliario</span>
      <span class="pill">Fabricación sobre medida</span>
      <span class="pill">Tapicería</span>
      <span class="pill">Renovación</span>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# FORMA DE TRABAJO
# --------------------------------------------------
seccion(
    "Un proceso claro, de principio a fin.",
    "Queremos que pedir tus materiales sea más sencillo.",
    "Cómo trabajamos"
)
c1, c2, c3, c4 = st.columns(4, gap="medium")
pasos = [
    ("01", "Nos contactas", "Cuéntanos qué necesitas."),
    ("02", "Preparamos", "Definimos materiales y alcance."),
    ("03", "Cotizamos", "Revisamos opciones y tiempos."),
    ("04", "Coordinamos", "Damos seguimiento al pedido.")
]
for col, paso in zip([c1, c2, c3, c4], pasos):
    with col:
        tarjeta(*paso)

# --------------------------------------------------
# CONTACTO
# --------------------------------------------------
st.markdown('<div id="contacto"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="cta-panel">
  <div class="eyebrow">Hagamos equipo</div>
  <h2>¿Qué necesitas<br>resolver hoy?</h2>
  <p>
    Cuéntanos tu idea. Te ayudaremos a identificar los materiales y servicios
    que pueden hacer realidad tu proyecto.
  </p>
</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns([1, 1.2], gap="large")
with c1:
    st.markdown("""
    <div style="padding-top:18px">
      <h3 style="color:#09223D;font-size:1.5rem">Hablemos de tu proyecto.</h3>
      <p style="color:#64758A">
        Comparte tus datos y una breve descripción de lo que buscas.
        Podrás revisar la información antes de enviarla por el medio de contacto disponible.
      </p>
    </div>
    """, unsafe_allow_html=True)
    if CORREO:
        st.markdown(f"✉️ **Correo:** [{html.escape(CORREO)}](mailto:{html.escape(CORREO)})")
    if TELEFONO:
        st.markdown(f"☎️ **Teléfono:** {html.escape(TELEFONO)}")
    if WHATSAPP:
        st.link_button("Escribir por WhatsApp", f"https://wa.me/{WHATSAPP}")

with c2:
    with st.form("contacto_nexo"):
        nombre = st.text_input("Nombre")
        empresa = st.text_input("Empresa u organización")
        correo_cliente = st.text_input("Correo electrónico")
        tipo = st.selectbox(
            "¿Qué necesitas?",
            [
                "Productos promocionales",
                "Impresión y gran formato",
                "Diseño y comunicación",
                "Materiales para eventos",
                "Soluciones digitales",
                "Mobiliario o renovación",
                "Proyecto integral",
                "Otro"
            ]
        )
        mensaje = st.text_area("Cuéntanos sobre tu proyecto")
        enviar = st.form_submit_button("Preparar solicitud")

    if enviar:
        if not nombre.strip() or not correo_cliente.strip() or not mensaje.strip():
            st.warning("Completa tu nombre, correo y descripción del proyecto.")
        else:
            asunto = f"Cotización Nexo Promocional - {tipo}"
            cuerpo = (
                f"Nombre: {nombre}\n"
                f"Empresa: {empresa}\n"
                f"Correo: {correo_cliente}\n"
                f"Servicio: {tipo}\n\n"
                f"Proyecto:\n{mensaje}"
            )
            st.success("Solicitud preparada. Puedes copiarla y enviarla al correo comercial.")
            st.code(f"ASUNTO: {asunto}\n\n{cuerpo}", language="text")
            st.caption(
                "Este formulario no envía ni almacena automáticamente los datos. "
                "Para recibir solicitudes directamente, hay que conectar un servicio de envío."
            )

# --------------------------------------------------
# PIE
# --------------------------------------------------
st.markdown("""
<div class="footer">
  <div><strong>NEXO PROMOCIONAL</strong><br>Ideas que conectan. Soluciones que avanzan.</div>
  <div>Productos · Impresión · Diseño · Soluciones digitales</div>
  <div>© Nexo Promocional</div>
</div>
""", unsafe_allow_html=True)
