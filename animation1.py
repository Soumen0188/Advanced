import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Create figure and axis
fig = make_subplots(rows=1, cols=1)
x = np.linspace(0, 2 * np.pi, 100)
trace = go.Scatter(x=x, y=np.sin(x))
fig.add_trace(trace)

# Update function for animation
frames = [go.Frame(data=[go.Scatter(x=x, y=np.sin(x + frame * 0.1))]) for frame in range(100)]
for frame in frames:
    fig.add_frame(frame)

# Set animation options
animation_opts = dict(frame=dict(duration=50, redraw=True), fromcurrent=True)
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                            method='animate', args=[None, animation_opts])])])

# Show the animation
fig.show()

