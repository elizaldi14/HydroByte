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
        chart_frame.setFrameShape(QFrame.StyledPanel)
        chart_frame.setStyleSheet("""
            QFrame#chartFrame {
                background: transparent;
                border-radius: 14px;
            }
        """)
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
        plot_widget.setMinimumHeight(200)  # Set minimum height for better visibility

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
        
        # Update frame style
        self.findChild(QFrame, "chartFrame").setStyleSheet(f"""
            QFrame#chartFrame {{
                background: {colors.get('card', '#FFFFFF')};
                border: 1px solid {colors.get('border', '#E2E8F0')};
                border-radius: 14px;
            }}
        """)
        
        # Update title style
        self.title_label.setStyleSheet(f"""
            QLabel {{
                color: {colors.get('text', '#1E293B')};
                background-color: transparent;
                padding: 5px;
            }}
        """)
        
        # Update chart colors
        for plot in self.plot_widgets:
            plot.setBackground(None)
            
            # Set axis colors
            for axis in ['left', 'bottom']:
                ax = plot.getAxis(axis)
                if ax:
                    ax.setPen(colors.get('text', '#1E293B'))
                    ax.setTextPen(colors.get('text', '#1E293B'))
            
            # Update grid
            plot.showGrid(x=True, y=True, alpha=0.3)
            
            # Update legend
            if hasattr(self, 'legend'):
                self.legend.setBrush(colors.get('card', '#FFFFFF'))
                self.legend.setPen(colors.get('border', '#E2E8F0'))
                self.legend.setLabelTextColor(colors.get('text', '#1E293B'))
                self.legend.setOffset((10, 10))

            plot.showGrid(x=True, y=True)
            plot.getPlotItem().getViewBox().setBackgroundColor(colors['card'])

            if hasattr(plot, 'legend') and plot.legend is not None:
                for sample, label in plot.legend.items:
                    label.setAttr('color', colors['text'])
