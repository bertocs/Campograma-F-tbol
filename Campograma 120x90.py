import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Rectangle, Circle

def create_pitch(length=120, width=90):
    # Dimensiones reglamentarias
    goal_width = 7.32
    pen_depth = 16.5
    pen_width = 40.32
    goal_area_depth = 5.5
    goal_area_width = 18.32
    pen_spot_dist = 11
    centre_circle_r = 9.15
    pen_arc_r = 9.15

    mid_x = length / 2
    mid_y = width / 2
    goal_half = goal_width / 2
    pen_half = pen_width / 2
    goal_area_half = goal_area_width / 2

    fig, ax = plt.subplots(figsize=(12, 9))
    ax.set_facecolor("white")

    # Campo exterior
    outer = Rectangle((0, 0), length, width, linewidth=1.2, edgecolor="black", facecolor="none")
    ax.add_patch(outer)

    # Línea central
    ax.plot([mid_x, mid_x], [0, width], color="black")

    # Círculo central y punto central
    ax.add_patch(Circle((mid_x, mid_y), centre_circle_r, edgecolor="black", facecolor="none"))
    ax.add_patch(Circle((mid_x, mid_y), 0.2, edgecolor="black", facecolor="black"))

    # Áreas de penal
    ax.add_patch(Rectangle((0, mid_y - pen_half), pen_depth, pen_width, edgecolor="black", facecolor="none"))
    ax.add_patch(Rectangle((length - pen_depth, mid_y - pen_half), pen_depth, pen_width, edgecolor="black", facecolor="none"))

    # Áreas de meta
    ax.add_patch(Rectangle((0, mid_y - goal_area_half), goal_area_depth, goal_area_width, edgecolor="black", facecolor="none"))
    ax.add_patch(Rectangle((length - goal_area_depth, mid_y - goal_area_half), goal_area_depth, goal_area_width, edgecolor="black", facecolor="none"))

    # Puntos de penalti pequeño
    ax.add_patch(Circle((pen_spot_dist, mid_y), 0.2, edgecolor="black", facecolor="black"))
    ax.add_patch(Circle((length - pen_spot_dist, mid_y), 0.2, edgecolor="black", facecolor="black"))

    # Arcos de penalti
    ax.add_patch(Arc((pen_spot_dist, mid_y), pen_arc_r * 2, pen_arc_r * 2,
                     angle=0, theta1=310, theta2=50, color="black"))
    ax.add_patch(Arc((length - pen_spot_dist, mid_y), pen_arc_r * 2, pen_arc_r * 2,
                     angle=0, theta1=130, theta2=230, color="black"))

    # Configuración de ejes
    ax.set_xlim(0, length)
    ax.set_ylim(0, width)
    ax.set_aspect('equal')
    ax.invert_yaxis()
    ax.axis('off')

    # Evento de clic para mostrar coordenadas
    def onclick(event):
        if event.inaxes:
            print(f"Coordenadas: ({event.xdata:.2f}, {event.ydata:.2f})")

    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

create_pitch()
