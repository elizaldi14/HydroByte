import pyqtgraph as pg
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from time import time, strftime, localtime


class TimeAxisItem(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        return [strftime('%H:%M:%S', localtime(value)) for value in values]


class ChartWidget(QWidget):
    def __init__(self, title, series_data, theme_manager, parent=None):
        super().__init__(parent)
        self.title = title
        self.series_data = series_data
        self.theme_manager = theme_manager
        self.max_points = 10

        self.setup_ui()
        self.apply_theme()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        chart_frame = QFrame()
        chart_frame.setObjectName("chartFrame")
        chart_layout = QVBoxLayout(chart_frame)
        chart_layout.setContentsMargins(15, 15, 15, 15)

        title_label = QLabel(self.title)
        title_label.setFont(QFont("Segoe UI", 14, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        self.title_label = title_label
        self.title_label.setStyleSheet("background-color: transparent;")

        self.plot_widgets = []
        self.data_lines = []
        self.x_data = []
        self.y_data = []

        current_time = time()
        for series in self.series_data:
            x_series = [current_time - (self.max_points - i) for i in range(len(series["data"]))]
            self.x_data.append(x_series)
            self.y_data.append(series["data"].copy())

        plot_widget = pg.PlotWidget(axisItems={'bottom': TimeAxisItem(orientation='bottom')})
        plot_widget.setBackground(None)
        plot_widget.showGrid(x=True, y=True, alpha=0.3)

        view_box = plot_widget.getViewBox()
        view_box.setMouseEnabled(x=False, y=False)
        view_box.setMenuEnabled(False)

        for i, series_info in enumerate(self.series_data):
            pen = pg.mkPen(color=series_info["color"], width=3)
            data_line = plot_widget.plot(
                self.x_data[i],
                self.y_data[i],
                name=series_info["name"],
                pen=pen,
                symbol='o',
                symbolSize=8,
                symbolBrush=series_info["color"]
            )
            self.data_lines.append(data_line)

        legend = plot_widget.addLegend()
        legend.setOffset((10, 10))
        self.legend = legend

        all_y_values = [item for sublist in self.y_data for item in sublist]
        if all_y_values:
            min_y = min(all_y_values) - 1
            max_y = max(all_y_values) + 1
            plot_widget.setYRange(min_y, max_y)

        self.plot_widget = plot_widget
        self.plot_widgets.append(plot_widget)

        chart_layout.addWidget(title_label)
        chart_layout.addWidget(plot_widget)
        layout.addWidget(chart_frame)

    def update_data(self, new_data):
        current_time = time()
        for i, series_info in enumerate(new_data):
            if i < len(self.data_lines):
                self.y_data[i] = series_info["data"].copy()
                self.x_data[i] = [current_time - (len(series_info["data"]) - j) for j in range(len(series_info["data"]))]
                self.data_lines[i].setData(self.x_data[i], self.y_data[i])

        all_y_values = [item for sublist in self.y_data for item in sublist]
        if all_y_values:
            min_y = min(all_y_values) - 1
            max_y = max(all_y_values) + 1
            self.plot_widget.setYRange(min_y, max_y)

    def apply_theme(self):
        colors = self.theme_manager.get_colors()

        self.setStyleSheet(f"""
            #chartFrame {{
                background-color: {colors['card']};
                border: 1px solid {colors['border']};
                border-radius: 12px;
            }}
        """)

        self.title_label.setStyleSheet(f"color: {colors['text']};")

        for plot_widget in self.plot_widgets:
            plot_widget.setBackground(colors['card'])

            axis_pen = pg.mkPen(color=colors['text'], width=1.5)
            grid_pen = pg.mkPen(color=colors['border'], width=1, style=Qt.DotLine)

            for orientation in ['bottom', 'left']:
                axis = plot_widget.getAxis(orientation)
                axis.setPen(axis_pen)
                axis.setTextPen(colors['text'])
                axis.setStyle(tickTextOffset=10)

            plot_widget.showGrid(x=True, y=True)
            plot_widget.getPlotItem().getViewBox().setBackgroundColor(colors['card'])

            if hasattr(plot_widget, 'legend') and plot_widget.legend is not None:
                for sample, label in plot_widget.legend.items:
                    label.setAttr('color', colors['text'])
