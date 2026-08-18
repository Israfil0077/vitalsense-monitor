import random
import textwrap
import time
from datetime import datetime

import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="VitalSense Monitor",
    page_icon="♥",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# CUSTOM CSS
# ============================================================
st.markdown(
    """
<style>

    /* =========================
       STREAMLIT UI
       ========================= */

    header[data-testid="stHeader"] {
        display: none !important;
    }

    [data-testid="stToolbar"] {
        display: none !important;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 12% 18%,
                rgba(99, 72, 180, 0.16),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 82%,
                rgba(0, 180, 220, 0.08),
                transparent 28%
            ),
            #080d1d;
    }

    .block-container {
        max-width: 1050px;
        padding-top: 2.5rem;
        padding-bottom: 1.5rem;
    }


    /* =========================
       HEADER
       ========================= */

    .brand-wrap {
        text-align: center;
        margin-bottom: 10px;
    }

    .brand {
        display: inline-flex;
        align-items: center;
        gap: 16px;
    }

    .brand-icon {
        width: 54px;
        height: 54px;
        border-radius: 16px;

        display: flex;
        align-items: center;
        justify-content: center;

        background: linear-gradient(
            145deg,
            #ff596f,
            #e9368c
        );

        color: white;
        font-size: 28px;

        box-shadow:
            0 10px 30px
            rgba(239, 62, 117, 0.30);
    }

    .brand-title {
        font-size: 32px;
        font-weight: 800;
        letter-spacing: -1px;
        color: #f8fafc;
        text-align: left;
    }

    .brand-title .accent {
        color: #ff6374;
    }

    .brand-subtitle {
        margin-top: 3px;
        color: #9ba9c1;
        font-size: 14px;
        text-align: left;
    }


    /* =========================
       SENSOR STATUS
       ========================= */

    .sensor-pill {
        width: fit-content;

        margin: 20px auto 30px auto;

        padding: 8px 16px;

        border-radius: 999px;

        border: 1px solid
            rgba(16, 185, 129, 0.35);

        background:
            rgba(16, 185, 129, 0.07);

        color: #34e6a0;

        font-size: 13px;
        font-weight: 700;
    }

    .sensor-dot {
        display: inline-block;

        width: 8px;
        height: 8px;

        margin-right: 8px;

        border-radius: 50%;

        background: #34e6a0;

        box-shadow:
            0 0 12px
            rgba(52, 230, 160, 0.85);
    }


    /* =========================
       READING CARDS
       ========================= */

    .reading-card {
        position: relative;
        overflow: hidden;

        height: 350px;

        padding: 28px 24px;

        border-radius: 22px;

        border: 1px solid
            rgba(148, 163, 184, 0.16);

        background:
            linear-gradient(
                145deg,
                rgba(28, 39, 62, 0.96),
                rgba(12, 20, 39, 0.98)
            );

        box-shadow:
            0 18px 45px
            rgba(0, 0, 0, 0.28);

        text-align: center;
    }


    .reading-card::before {
        content: "";

        position: absolute;

        top: 0;
        left: 0;
        right: 0;

        height: 3px;
    }


    .heart-card::before {
        background: #ff4f61;
    }

    .spo2-card::before {
        background: #26b9f4;
    }


    /* =========================
       CARD GLOW
       ========================= */

    .card-glow {
        position: absolute;

        width: 140px;
        height: 140px;

        right: -70px;
        top: -70px;

        border-radius: 50%;

        opacity: 0.10;
    }

    .heart-glow {
        background: #ff4f61;
    }

    .spo2-glow {
        background: #26b9f4;
    }


    /* =========================
       CARD ICON
       ========================= */

    .card-icon {
        position: relative;

        width: 68px;
        height: 68px;

        margin: 0 auto 20px auto;

        border-radius: 50%;

        display: flex;
        align-items: center;
        justify-content: center;

        font-size: 30px;
        font-weight: 700;

        background:
            rgba(5, 12, 27, 0.72);
    }


    .heart-icon {
        color: #ff6371;

        border: 1px solid
            rgba(255, 79, 97, 0.75);

        box-shadow:
            0 0 20px
            rgba(255, 79, 97, 0.15);
    }


    .spo2-icon {
        color: #37c7ff;

        border: 1px solid
            rgba(38, 185, 244, 0.75);

        box-shadow:
            0 0 20px
            rgba(38, 185, 244, 0.15);
    }


    /* =========================
       LABEL
       ========================= */

    .card-label {
        position: relative;

        display: flex;

        align-items: center;
        justify-content: center;

        gap: 12px;

        margin-bottom: 14px;

        font-size: 14px;

        font-weight: 800;

        letter-spacing: 0.3px;
    }


    .card-label::before,
    .card-label::after {
        content: "";

        width: 28px;
        height: 1px;

        opacity: 0.75;
    }


    .heart-label {
        color: #ff6673;
    }

    .heart-label::before,
    .heart-label::after {
        background: #ff4f61;
    }


    .spo2-label {
        color: #35c4ff;
    }

    .spo2-label::before,
    .spo2-label::after {
        background: #26b9f4;
    }


    /* =========================
       BIG VALUE
       ========================= */

    .reading-number {
        position: relative;

        color: #f8fafc;

        font-size: 72px;

        font-weight: 850;

        line-height: 1;

        letter-spacing: -3px;
    }


    .reading-unit {
        position: relative;

        margin-top: 8px;

        font-size: 17px;

        font-weight: 800;
    }


    .heart-unit {
        color: #ff6574;
    }

    .spo2-unit {
        color: #35c4ff;
    }


    /* =========================
       READING STATUS
       ========================= */

    .reading-status {
        position: relative;

        width: fit-content;

        margin: 26px auto 0 auto;

        padding: 7px 14px;

        border-radius: 999px;

        border: 1px solid
            rgba(148, 163, 184, 0.18);

        color: #e2e8f0;

        background:
            rgba(9, 17, 35, 0.55);

        font-size: 12px;

        font-weight: 650;
    }


    .status-check {
        color: #19e89a;

        margin-right: 6px;

        font-size: 14px;
    }


    /* =========================
       INFORMATION PANEL
       ========================= */

    .info-panel {
        display: flex;

        align-items: center;

        max-width: 850px;

        margin: 24px auto 0 auto;

        padding: 18px 24px;

        border: 1px solid
            rgba(148, 163, 184, 0.13);

        border-radius: 17px;

        background:
            rgba(12, 20, 39, 0.70);
    }


    .info-block {
        flex: 1;
    }


    .info-divider {
        width: 1px;

        height: 42px;

        background:
            rgba(148, 163, 184, 0.16);

        margin: 0 28px;
    }


    .info-label {
        color: #8e9bb2;

        font-size: 11px;

        font-weight: 700;

        letter-spacing: 0.5px;
    }


    .info-value {
        margin-top: 4px;

        color: #e8edf5;

        font-size: 14px;

        font-weight: 750;
    }


    .info-sub {
        margin-top: 2px;

        color: #64748b;

        font-size: 11px;
    }


    .connected {
        color: #20e6a0;
    }


    /* =========================
       FOOTER
       ========================= */

    .footer {
        margin-top: 20px;

        text-align: center;

        color: #65738a;

        font-size: 11px;
    }


    /* =========================
       MOBILE
       ========================= */

    @media (max-width: 750px) {

        .block-container {
            padding-top: 1.5rem;
        }

        .brand-title {
            font-size: 26px;
        }

        .brand-icon {
            width: 48px;
            height: 48px;
        }

        .reading-card {
            height: 330px;
            margin-bottom: 18px;
        }

        .reading-number {
            font-size: 62px;
        }

        .info-panel {
            display: block;
        }

        .info-divider {
            width: 100%;
            height: 1px;
            margin: 16px 0;
        }
    }

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# SENSOR DATA
# ============================================================
def get_sensor_data():

    # DEMO DATA
    # Replace this section later with ESP32 communication.

    random.seed(int(time.time()) // 2)

    heart_rate = random.randint(72, 84)

    spo2 = random.randint(96, 99)

    return heart_rate, spo2


heart_rate, spo2 = get_sensor_data()

updated = datetime.now().strftime("%I:%M:%S %p")


# ============================================================
# HEADER
# ============================================================
st.markdown(
    """
<div class="brand-wrap">
<div class="brand">
<div class="brand-icon">♥</div>
<div>
<div class="brand-title"><span class="accent">VitalSense</span> Monitor</div>
<div class="brand-subtitle">Live heart rate &amp; oxygen saturation monitor</div>
</div>
</div>
</div>

<div class="sensor-pill">
<span class="sensor-dot"></span>
Sensor Dashboard
</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# READING CARDS
# ============================================================
left, right = st.columns(
    2,
    gap="medium"
)


# ============================================================
# HEART RATE
# ============================================================
with left:

    st.markdown(
        textwrap.dedent(f"""\
        <div class="reading-card heart-card">
            <div class="card-glow heart-glow"></div>
            <div class="card-icon heart-icon">♥</div>
            <div class="card-label heart-label">HEART RATE</div>
            <div class="reading-number">{heart_rate}</div>
            <div class="reading-unit heart-unit">BPM</div>
            <div class="reading-status">
                <span class="status-check">✓</span>
                Reading received
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )


# ============================================================
# SPO2
# ============================================================
with right:

    st.markdown(
        textwrap.dedent(f"""\
        <div class="reading-card spo2-card">
            <div class="card-glow spo2-glow"></div>
            <div class="card-icon spo2-icon">O₂</div>
            <div class="card-label spo2-label">BLOOD OXYGEN (SpO₂)</div>
            <div class="reading-number">{spo2}</div>
            <div class="reading-unit spo2-unit">%</div>
            <div class="reading-status">
                <span class="status-check">✓</span>
                Reading received
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )


# ============================================================
# DEVICE INFORMATION
# ============================================================
st.markdown(
    f"""
<div class="info-panel">
<div class="info-block">
<div class="info-label">LAST READING RECEIVED</div>
<div class="info-value">{updated}</div>
<div class="info-sub">Live sensor update</div>
</div>
<div class="info-divider"></div>
<div class="info-block">
<div class="info-label">DATA SOURCE</div>
<div class="info-value">ESP32 Sensor</div>
<div class="info-sub connected">● Connected</div>
</div>
</div>

<div class="footer">This interface displays sensor readings and is not a diagnostic tool.</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# AUTO REFRESH
# ============================================================
time.sleep(2)
st.rerun()