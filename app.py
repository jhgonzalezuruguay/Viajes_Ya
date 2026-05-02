import streamlit as st

st.set_page_config(page_title="Turismo Salto", layout="centered")

st.title("🇺🇾 Turismo Salto")
st.write("Explorá hoteles en Termas de Daymán y Arapey")

# -------------------------
# DATA (cargá 6–10 por zona)
# -------------------------
dayman = [
    {
        "nombre": "Hotel Aguasol",
        "precio": "Desde $3500",
        "desc": "Hotel termal cerca del complejo Daymán.",
        "whatsapp": "59812345678",
        "img": "https://via.placeholder.com/400x250"
    },
    {
        "nombre": "Hotel El Mirador",
        "precio": "Desde $4200",
        "desc": "Vistas al río y acceso a termas.",
        "whatsapp": "59812345678",
        "img": "https://via.placeholder.com/400x250"
    },
]

arapey = [
    {
        "nombre": "Altos del Arapey",
        "precio": "Desde $9000",
        "desc": "Resort all inclusive con spa.",
        "whatsapp": "59812345678",
        "img": "https://via.placeholder.com/400x250"
    },
    {
        "nombre": "Arapey Thermal Resort",
        "precio": "Desde $8500",
        "desc": "Ideal para grupos y relax.",
        "whatsapp": "59812345678",
        "img": "https://via.placeholder.com/400x250"
    },
]

# -------------------------
# UI
# -------------------------
zona = st.selectbox("Elegí zona", ["Daymán", "Arapey"])

data = dayman if zona == "Daymán" else arapey

for hotel in data:
    st.image(hotel["img"])
    st.subheader(hotel["nombre"])
    st.write(hotel["precio"])
    st.write(hotel["desc"])

    mensaje = f"Hola, vi {hotel['nombre']} en la app y me interesa"
    link = f"https://wa.me/{hotel['whatsapp']}?text={mensaje.replace(' ', '%20')}"

    st.link_button("📞 Contactar por WhatsApp", link)
    st.markdown("---")
