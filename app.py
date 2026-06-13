import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Page configuration and styling
st.set_page_config(page_title="1D Heat Equation Pro", layout="wide")
plt.style.use('dark_background')

# App header and collapsible description
st.title("🔥 1D Heat Equation: Dynamic Simulation")

with st.expander("📖 Show Description & Mathematical Formula", expanded=False):
    st.markdown(
        "An interactive simulator for the 1D Heat Equation. Customize the initial heat distribution, adjust physical parameters, and observe how heat diffuses over time.")
    st.latex(r"u(x,t) = \sum_{n=1}^{N} B_n \sin\left(\frac{n\pi x}{L}\right) e^{-c \left(\frac{n\pi}{L}\right)^2 t}")

# Physical parameters
L = np.pi
x = np.linspace(0, L, 500)

# Sidebar UI controls
st.sidebar.header("🎛️ Control Panel")

func_str = st.sidebar.text_input(
    "Initial Equation f(x) =",
    value="100 * ((x > np.pi/4) & (x < 3*np.pi/4))",
    help="Supports Python/NumPy syntax, e.g., 100 * np.sin(x)"
)

c = st.sidebar.slider(
    "Diffusion Coefficient (c)",
    min_value=0.01, max_value=2.0, value=0.10, step=0.01,
    help="Higher values represent faster heat transfer."
)

st.sidebar.markdown("---")
t = st.sidebar.slider("Time (t)", 0.0, 3.0, 0.0, step=0.01)
n = st.sidebar.slider("Fourier Terms (N)", 1, 100, 50, step=1)

st.sidebar.markdown("---")
auto_scale = st.sidebar.checkbox("Auto-scale Y-axis", value=False,
                                 help="Check this to dynamically adjust the Y-axis as temperature drops.")

st.sidebar.markdown("---")
st.sidebar.subheader("🎬 Auto Play Animation")
play_target = st.sidebar.radio("Select Play Target:", ("Time", "Terms"))
play_btn = st.sidebar.button("▶ Play Animation", use_container_width=True)


# Mathematical computations (Fourier coefficients and heat profile)
@st.cache_data
def get_fourier_coefficients(equation_str, max_terms=100):
    Bn = np.zeros(max_terms + 1)
    try:
        f_x = eval(equation_str)
        if isinstance(f_x, (int, float)):
            f_x = np.full_like(x, f_x)

        trapz_func = getattr(np, 'trapezoid', getattr(np, 'trapz', None))
        for i in range(1, max_terms + 1):
            integrand = f_x * np.sin(i * x)
            Bn[i] = (2 / L) * trapz_func(integrand, x)
        return Bn
    except Exception as e:
        st.sidebar.error(f"Equation parsing error: {e}")
        return None


cached_Bn = get_fourier_coefficients(func_str)


def get_heat_profile(t_val, terms_val, c_val):
    u = np.zeros_like(x)
    if cached_Bn is None:
        return u
    for i in range(1, terms_val + 1):
        if cached_Bn[i] != 0:
            u += cached_Bn[i] * np.sin(i * x) * np.exp(-c_val * (i ** 2) * t_val)
    return u


# Visualization setup (Temperature curve and heatmap)
def draw_plot(current_t, current_n):
    fig = plt.figure(figsize=(12, 4.5))
    gs = fig.add_gridspec(2, 1, height_ratios=[3.5, 1], hspace=0.35)

    ax_main = fig.add_subplot(gs[0])
    ax_bar = fig.add_subplot(gs[1])

    u_current = get_heat_profile(current_t, current_n, c)

    ax_main.plot(x, u_current, color='#ff3366', lw=7, alpha=0.3)
    ax_main.plot(x, u_current, color='#ff9933', lw=2, label='Temperature Curve')
    ax_main.set_xlim(0, L)

    if not auto_scale:
        ax_main.set_ylim(-20, 130)

    ax_main.set_ylabel("Temperature (°C)", fontsize=10, color='lightgray')
    ax_main.grid(True, color='#333333', linestyle='--')
    ax_main.legend(loc='upper right', facecolor='#222222', edgecolor='none', labelcolor='white')

    vmax_val = np.max(u_current) if auto_scale and np.max(u_current) > 0 else 100
    ax_bar.imshow(u_current.reshape(1, -1), cmap='inferno', aspect='auto', extent=[0, L, 0, 1], vmin=0, vmax=vmax_val)
    ax_bar.set_yticks([])
    ax_bar.set_xlabel("Position on Metal Bar (x)", fontsize=10, color='lightgray')

    return fig


# Main rendering and animation loop
status_text = st.empty()
plot_placeholder = st.empty()

if play_btn:
    if play_target == "Time":
        for val in np.arange(0.0, 3.05, 0.05):
            status_text.markdown(f"### ⏳ Playing Time ($t$): `{val:.2f}` | Terms ($N$): `{n}`")
            fig = draw_plot(val, n)
            plot_placeholder.pyplot(fig)
            plt.close(fig)
            time.sleep(0.05)
    elif play_target == "Terms":
        for val in range(1, 101, 2):
            status_text.markdown(f"### ⏳ Playing Terms ($N$): `{val}` | Time ($t$): `{t:.2f}`")
            fig = draw_plot(t, val)
            plot_placeholder.pyplot(fig)
            plt.close(fig)
            time.sleep(0.05)

    status_text.success(f"✅ Animation Finished! Reverted to slider state (t={t}, N={n}).")
    fig = draw_plot(t, n)
    plot_placeholder.pyplot(fig)
    plt.close(fig)
else:
    status_text.markdown(f"### 📍 Current State - Time ($t$): `{t:.2f}` | Terms ($N$): `{n}`")
    fig = draw_plot(t, n)
    plot_placeholder.pyplot(fig)
    plt.close(fig)