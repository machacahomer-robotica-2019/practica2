from RobotDrawer_python3 import plot_log, plot_log_with_map


def main():
    """
    Plot log file
    """
    plot_log("./out/trayectoria_trabajo_2.csv")
    # plot_log_with_map('./out/trayectoria_trabajo.csv', './maps/mapa3.txt')


if __name__ == "__main__":
    main()
