
import streamlit as st
from datetime import datetime
from urllib.parse import quote

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(
    page_title="Nexo Comercial | Soluciones para empresas",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded"
)

EMPRESA = "Nexo Comercial"
SUBTITULO = "Publicidad, productos promocionales y soluciones digitales"

# COMPLETAR CUANDO TENGAS LOS DATOS OFICIALES
CORREO = ""
TELEFONO = ""
WHATSAPP = ""  # Ejemplo México: 5215512345678

# =====================================================
# DISEÑO
# =====================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

.stApp {
    background-color: #F4F7FA;
    color: #1A2B3C;
    font-family: 'DM Sans', sans-serif;
}
h1, h2, h3 {
    font-family: 'Manrope', sans-serif;
    color: #10243A;
}
[data-testid="stSidebar"] {
    background: #10243A;
}
[data-testid="stSidebar"] * {
    color: white;
}
.hero {
    background: linear-gradient(130deg, #10243A, #214E70, #27798A);
    padding: 52px 42px;
    border-radius: 22px;
    color: white;
    margin-bottom: 28px;
}
.hero h1 {
    color: white;
    font-size: clamp(34px, 5vw, 56px);
    line-height: 1.12;
}
.hero p {
    color: #E4EDF5;
    font-size: 18px;
    line-height: 1.7;
    max-width: 780px;
}
.eyebrow {
    color: #8CE2E5;
    font-weight: 700;
    letter-spacing: 2px;
    font-size: 12px;
    text-transform: uppercase;
}
.card {
    background: white;
    border: 1px solid #E0E7EE;
    border-radius: 16px;
    padding: 23px;
    margin-bottom: 15px;
    min-height: 155px;
    box-shadow: 0 4px 15px rgba(16,36,58,0.04);
}
.card h3 {
    font-size: 19px;
}
.card p {
    color: #637384;
    line-height: 1.65;
    font-size: 14px;
}
.case {
    background: white;
    border: 1px solid #E0E7EE;
    border-radius: 16px;
    padding: 26px;
    margin: 15px 0;
}
.label {
    color: #27798A;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
}
.feature {
    background: #E7F2F6;
    border-left: 4px solid #4CB7C5;
    border-radius: 8px;
    padding: 18px;
    margin: 20px 0;
}
.stButton > button, .stDownloadButton > button {
    background: #10243A;
    color: white;
    border: 1px solid #10243A;
    border-radius: 9px;
    font-weight: 600;
    min-height: 42px;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    background: #234E70;
    color: white;
    border-color: #234E70;
}
.footer {
    border-top: 1px solid #DCE4EC;
    color: #637384;
    padding-top: 22px;
    margin-top: 45px;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)


# =====================================================
# FUNCIONES
# =====================================================

def titulo_seccion(titulo, descripcion=""):
    st.markdown(f"## {titulo}")
    if descripcion:
        st.markdown(
            f"<p style='color:#637384;font-size:16px'>{descripcion}</p>",
            unsafe_allow_html=True
        )


def tarjeta(icono, titulo, descripcion):
    st.markdown(f"""
    <div class="card">
        <div style="font-size:27px">{icono}</div>
        <h3>{titulo}</h3>
        <p>{descripcion}</p>
    </div>
    """, unsafe_allow_html=True)


def pie():
    st.markdown(f"""
    <div class="footer">
        <strong>{EMPRESA}</strong><br>
        {SUBTITULO}<br><br>
        Los productos, precios, cantidades y tiempos de entrega
        se confirman mediante cotización.
    </div>
    """, unsafe_allow_html=True)


def ir_a_cotizacion():
    st.session_state["pagina"] = "Solicitar cotización"


# =====================================================
# MENÚ LATERAL
# =====================================================

with st.sidebar:
    st.markdown("# ◆ NEXO")
    st.markdown("### COMERCIAL")
    st.caption("Un aliado para tus proyectos")
    st.divider()

    opciones = [
        "Inicio",
        "Nosotros",
        "Servicios",
        "Portafolio",
        "Solicitar cotización",
        "Contacto"
    ]

    pagina_actual = st.session_state.get("pagina", "Inicio")

    pagina = st.radio(
        "MENÚ PRINCIPAL",
        opciones,
        index=opciones.index(pagina_actual)
        if pagina_actual in opciones else 0
    )

    st.session_state["pagina"] = pagina

    st.divider()
    st.caption("Publicidad · Suministro · Comunicación")

# =====================================================
# INICIO
# =====================================================

if pagina == "Inicio":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">PUBLICIDAD · SUMINISTRO · COMUNICACIÓN</div>
        <h1>Tu proyecto necesita<br>un aliado comercial.</h1>
        <p>
            Integramos productos promocionales, impresión y soluciones
            digitales para empresas, asociaciones e instituciones.
            Simplificamos la coordinación de tus requerimientos
            con una propuesta comercial clara.
        </p>
    </div>
    """, unsafe_allow_html=True)

    titulo_seccion(
        "Soluciones integrales para tu organización",
        "Desde artículos promocionales hasta materiales para congresos, "
        "cursos, campañas y comunicación institucional."
    )

    columnas = st.columns(3)

    with columnas[0]:
        tarjeta(
            "🎁", "Productos promocionales",
            "Tazas, plumas, bolsas, pines, gafetes y artículos personalizados."
        )

    with columnas[1]:
        tarjeta(
            "🖨️", "Impresión y publicidad",
            "Lonas, roll-ups, muros gráficos, folletos, volantes y señalización."
        )

    with columnas[2]:
        tarjeta(
            "💻", "Soluciones digitales",
            "Páginas informativas, formularios, boletos con QR y apoyo a eventos."
        )

    st.markdown("""
    <div class="feature">
        <strong>Nuestra propuesta de valor</strong><br>
        Hacer más sencilla la gestión de pedidos y materiales,
        buscando calidad, coordinación y soluciones adecuadas
        a las necesidades de cada cliente.
    </div>
    """, unsafe_allow_html=True)

    if st.button("Conocer nuestros servicios", type="primary"):
        ir_a_cotizacion()
        st.rerun()

    pie()


# =====================================================
# NOSOTROS
# =====================================================

elif pagina == "Nosotros":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">QUIÉNES SOMOS</div>
        <h1>Conectamos necesidades<br>con soluciones.</h1>
        <p>
            Nexo Comercial integra productos promocionales, materiales
            publicitarios y herramientas digitales para apoyar a
            organizaciones en sus proyectos.
        </p>
    </div>
    """, unsafe_allow_html=True)

    titulo_seccion("Nuestra forma de trabajar")

    st.write("""
    Cada proyecto comienza por comprender qué necesita el cliente.
    A partir de ello, organizamos los requerimientos, revisamos
    alternativas y preparamos una propuesta con alcances definidos.
    """)

    a, b = st.columns(2)

    with a:
        st.markdown("### Nuestra misión")
        st.write("""
        Facilitar el acceso a productos y servicios que apoyen
        la comunicación, promoción y operación de empresas,
        asociaciones e instituciones.
        """)

    with b:
        st.markdown("### Nuestro compromiso")
        st.write("""
        Ofrecer atención clara, seguimiento comercial y alternativas
        acordes con los objetivos y el presupuesto de cada proyecto.
        """)

    titulo_seccion("Principios de servicio")

    principios = [
        ("Atención personalizada", "Comprender cada necesidad."),
        ("Coordinación", "Organizar productos y servicios en una propuesta."),
        ("Calidad", "Buscar materiales y acabados adecuados."),
        ("Claridad", "Definir precios, alcances y tiempos en la cotización.")
    ]

    for nombre, descripcion in principios:
        st.markdown(f"""
        <div class="case">
            <h3>{nombre}</h3>
            <p>{descripcion}</p>
        </div>
        """, unsafe_allow_html=True)

    st.caption(
        "Revisa estos textos y ajústalos a la identidad institucional "
        "definitiva antes de publicar."
    )

    pie()


# =====================================================
# SERVICIOS
# =====================================================

elif pagina == "Servicios":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">CATÁLOGO DE SERVICIOS</div>
        <h1>Todo lo que tu proyecto<br>necesita comunicar.</h1>
        <p>
            Soluciones promocionales, gráficas y digitales para
            empresas, asociaciones, congresos y campañas comerciales.
        </p>
    </div>
    """, unsafe_allow_html=True)

    categorias = [
        (
            "Productos promocionales",
            "Artículos personalizados para eventos, marcas y campañas.",
            [
                ("☕", "Tazas y termos", "Artículos personalizados para regalos y campañas."),
                ("🖊️", "Plumas", "Plumas promocionales y artículos de escritura."),
                ("🪪", "Gafetes", "Credenciales y elementos de identificación."),
                ("📌", "Pines", "Distintivos personalizados para instituciones."),
                ("👜", "Bolsas", "Bolsas textiles y materiales promocionales."),
                ("🎁", "Regalos corporativos", "Artículos seleccionados según el proyecto.")
            ]
        ),
        (
            "Impresión y publicidad",
            "Materiales para difusión, identidad visual y eventos.",
            [
                ("🪧", "Lonas", "Lonas institucionales y comerciales."),
                ("📐", "Roll-ups", "Displays portátiles para exposiciones."),
                ("🧱", "Muros gráficos", "Fondos y estructuras para eventos."),
                ("📄", "Folletos y volantes", "Material impreso para campañas."),
                ("📚", "Papelería corporativa", "Tarjetas, carpetas y formatos."),
                ("🧭", "Señalización", "Gráficos de orientación e identificación."),
                ("🖼️", "Diseño gráfico", "Diseño y adaptación de archivos."),
                ("📣", "Comunicación visual", "Piezas gráficas para empresas.")
            ]
        ),
        (
            "Soluciones digitales",
            "Herramientas digitales para cursos, eventos y comunicación.",
            [
                ("🔳", "Boletos con QR", "Boletos electrónicos y códigos de acceso."),
                ("📝", "Formularios", "Captura de datos y registro de asistentes."),
                ("📊", "Control de registros", "Organización de datos y hojas de seguimiento."),
                ("🌐", "Páginas informativas", "Páginas para cursos, servicios y eventos."),
                ("🎟️", "Apoyo a eventos", "Herramientas digitales para asistentes."),
                ("🎨", "Diseño digital", "Piezas para comunicación en línea.")
            ]
        ),
        (
            "Suministro comercial e institucional",
            "Apoyo en la integración y coordinación de requerimientos.",
            [
                ("📋", "Integración de pedidos", "Consolidación de distintos productos."),
                ("🤝", "Coordinación comercial", "Seguimiento de requerimientos y proveedores."),
                ("📦", "Suministro institucional", "Productos para asociaciones y empresas."),
                ("🗓️", "Planeación", "Organización de cantidades y entregas.")
            ]
        )
    ]

    for categoria, descripcion, productos in categorias:
        titulo_seccion(categoria, descripcion)
        columnas = st.columns(3)

        for i, producto in enumerate(productos):
            with columnas[i % 3]:
                tarjeta(*producto)

        st.write("")

    st.info(
        "La disponibilidad, especificaciones, precios y tiempos "
        "de entrega se confirman para cada cotización."
    )

    if st.button("Solicitar una cotización", type="primary"):
        ir_a_cotizacion()
        st.rerun()

    pie()


# =====================================================
# PORTAFOLIO
# =====================================================

elif pagina == "Portafolio":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">PROYECTOS Y EXPERIENCIA</div>
        <h1>Soluciones que se integran<br>en un mismo proyecto.</h1>
        <p>
            Ejemplos de trabajo en materiales promocionales,
            comunicación visual y apoyo digital.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.caption(
        "Esta primera versión utiliza descripciones. Después "
        "podremos integrar fotografías reales y autorizadas."
    )

    st.markdown("""
    <div class="case">
        <div class="label">CASO INSTITUCIONAL</div>
        <h2>Asociación Mexicana de Hepatología (AMH)</h2>
        <p>
            Suministro de materiales promocionales y gráficos para
            actividades institucionales y eventos.
        </p>
        <ul>
            <li>Tazas y plumas promocionales.</li>
            <li>Gafetes para identificación.</li>
            <li>Roll-up y muro gráfico.</li>
            <li>Apoyo digital para cursos y materiales de acceso.</li>
        </ul>
        <p><strong>Enfoque:</strong> coordinar distintos requerimientos
        mediante una propuesta comercial integrada.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="case">
        <div class="label">CASO DE MOBILIARIO Y COMUNICACIÓN</div>
        <h2>Roothúa</h2>
        <p>
            Proyectos de mobiliario, renovación y comunicación
            comercial para mostrar productos, procesos y resultados.
        </p>
        <ul>
            <li>Contenido comercial de productos.</li>
            <li>Comunicación de procesos de renovación de muebles.</li>
            <li>Material visual para presentar acabados y soluciones.</li>
        </ul>
        <p><strong>Enfoque:</strong> comunicar el valor del trabajo
        realizado mediante contenido comercial.</p>
    </div>
    """, unsafe_allow_html=True)

    st.warning(
        "Antes de publicar, incorpora fotografías autorizadas y "
        "verifica que las descripciones representen los trabajos "
        "realizados. No se incluyen métricas no verificadas."
    )

    pie()


# =====================================================
# SOLICITAR COTIZACIÓN
# =====================================================

elif pagina == "Solicitar cotización":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">INICIAR UN PROYECTO</div>
        <h1>Cuéntanos qué necesitas.</h1>
        <p>
            Completa los datos básicos para preparar un resumen
            de tu solicitud de cotización.
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("formulario_cotizacion"):
        st.subheader("Datos de contacto")

        nombre = st.text_input("Nombre de contacto *")
        organizacion = st.text_input("Empresa u organización")
        correo_cliente = st.text_input("Correo electrónico")
        telefono_cliente = st.text_input("Teléfono")

        st.subheader("Información del proyecto")

        tipo = st.selectbox(
            "Servicio solicitado *",
            [
                "Productos promocionales",
                "Impresión y publicidad",
                "Gafetes y credenciales",
                "Materiales para eventos",
                "Soluciones digitales",
                "Suministro institucional",
                "Varios servicios",
                "Otro"
            ]
        )

        descripcion = st.text_area(
            "Describe lo que necesitas *",
            placeholder=(
                "Ejemplo: 100 tazas personalizadas, 100 plumas, "
                "un roll-up y materiales para un evento."
            ),
            height=140
        )

        cantidad = st.text_input(
            "Cantidad aproximada",
            placeholder="Ejemplo: 100 piezas"
        )

        fecha = st.date_input(
            "Fecha deseada de entrega",
            value=None,
            format="DD/MM/YYYY"
        )

        presupuesto = st.selectbox(
            "Presupuesto estimado",
            [
                "Por definir",
                "Menos de $5,000 MXN",
                "$5,000 a $15,000 MXN",
                "$15,000 a $30,000 MXN",
                "$30,000 a $60,000 MXN",
                "Más de $60,000 MXN"
            ]
        )

        enviar = st.form_submit_button(
            "Preparar solicitud",
            type="primary",
            use_container_width=True
        )

    if enviar:
        if not nombre.strip() or not descripcion.strip():
            st.error(
                "Escribe tu nombre y describe el proyecto "
                "para poder preparar la solicitud."
            )
        else:
            fecha_texto = (
                fecha.strftime("%d/%m/%Y")
                if fecha else "Por definir"
            )

            folio = datetime.now().strftime("NX-%Y%m%d-%H%M%S")

            resumen = f"""
SOLICITUD DE COTIZACIÓN - {EMPRESA}
Folio: {folio}
Fecha de preparación: {datetime.now().strftime("%d/%m/%Y %H:%M")}

DATOS DE CONTACTO
Nombre: {nombre}
Empresa u organización: {organizacion}
Correo electrónico: {correo_cliente}
Teléfono: {telefono_cliente}

INFORMACIÓN DEL PROYECTO
Servicio: {tipo}
Descripción: {descripcion}
Cantidad aproximada: {cantidad}
Fecha deseada de entrega: {fecha_texto}
Presupuesto estimado: {presupuesto}

Esta solicitud es un resumen de requerimientos.
No representa una cotización definitiva ni confirma un pedido.
            """.strip()

            st.session_state["resumen_cotizacion"] = resumen
            st.session_state["folio_cotizacion"] = folio

            st.success(f"Solicitud preparada. Folio: {folio}")

    if st.session_state.get("resumen_cotizacion"):
        st.subheader("Resumen de la solicitud")

        st.text_area(
            "Revisa los datos antes de descargar",
            value=st.session_state["resumen_cotizacion"],
            height=300
        )

        st.download_button(
            "Descargar solicitud en TXT",
            data=st.session_state["resumen_cotizacion"],
            file_name="solicitud_nexo.txt",
            mime="text/plain",
            use_container_width=True
        )

        st.warning(
            "Este formulario todavía no envía correos ni almacena "
            "solicitudes en una base de datos. El archivo se descarga "
            "para que puedas enviarlo manualmente. Antes de recibir "
            "datos reales, configura almacenamiento seguro y aviso "
            "de privacidad."
        )

    pie()


# =====================================================
# CONTACTO
# =====================================================

elif pagina == "Contacto":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">CONTACTO COMERCIAL</div>
        <h1>Hablemos de tu próximo proyecto.</h1>
        <p>
            Cuéntanos qué materiales, productos o servicios necesitas
            y revisaremos las alternativas disponibles.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Canales de atención")

    if CORREO.strip():
        st.markdown(f"**Correo:** [{CORREO}](mailto:{CORREO})")
    else:
        st.info("Correo comercial pendiente de configurar.")

    if TELEFONO.strip():
        st.markdown(f"**Teléfono:** {TELEFONO}")
    else:
        st.info("Teléfono comercial pendiente de configurar.")

    if WHATSAPP.strip():
        st.link_button(
            "Contactar por WhatsApp",
            f"https://wa.me/{WHATSAPP.strip()}"
        )
    else:
        st.caption("WhatsApp comercial pendiente de configurar.")

    st.markdown("""
    <div class="feature">
        <strong>¿Tienes un proyecto en desarrollo?</strong><br>
        Puedes comenzar con una lista de productos, cantidades,
        fecha requerida y presupuesto aproximado.
    </div>
    """, unsafe_allow_html=True)

    if st.button("Preparar una solicitud"):
        ir_a_cotizacion()
        st.rerun()

    pie()
