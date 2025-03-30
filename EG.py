import numpy as np
import plotly.graph_objects as go
import streamlit as st

def ellipse_foci(a, b):
    c = np.sqrt(a**2 - b**2)
    return (-c, 0), (c, 0)

def plot_ellipse(a, b, num_rays=10):
    theta = np.linspace(0, 2*np.pi, 500)
    x = a * np.cos(theta)
    y = b * np.sin(theta)
    
    f1, f2 = ellipse_foci(a, b)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Ellipse Boundary'))
    
    
    fig.add_trace(go.Scatter(x=[f1[0], f2[0]], y=[f1[1], f2[1]],
                             mode='markers', marker=dict(size=10, color='red'), name='Foci'))
    
    
    angles = np.linspace(0, np.pi, num_rays)
    for angle in angles:
        ray_x = [f1[0], a * np.cos(angle)]
        ray_y = [f1[1], b * np.sin(angle)]
        fig.add_trace(go.Scatter(x=ray_x, y=ray_y, mode='lines', name='Sound Ray'))
        
        
        fig.add_trace(go.Scatter(x=[a * np.cos(angle), f2[0]], y=[b * np.sin(angle), f2[1]],
                                 mode='lines', line=dict(dash='dash'), name='Reflected Ray'))
    
    fig.update_layout(title='Elliptical Stadium Acoustics', xaxis=dict(scaleanchor='y'))
    return fig


st.title('Elliptical Stadium Sound Simulation')
a = st.slider('Major Axis (a)', 1.0, 10.0, 5.0)
b = st.slider('Minor Axis (b)', 1.0, 10.0, 3.0)
num_rays = st.slider('Number of Sound Rays', 5, 20, 10)

fig = plot_ellipse(a, b, num_rays)
st.plotly_chart(fig)
