from gui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui
from scraper import sennheiser_response, jbl_response, skullcandy_response
import json


class Browser(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.search_brands = []

        self.sennheiser_checkbox.stateChanged.connect(lambda: self.toggle_search(self.sennheiser_checkbox, "Sennheiser"))
        self.jbl_checkbox.stateChanged.connect(lambda: self.toggle_search(self.jbl_checkbox, "JBL"))
        self.skullcandy_checkbox.stateChanged.connect(lambda: self.toggle_search(self.skullcandy_checkbox, "Skullcandy"))

        self.search_button.clicked.connect(self.display_results)

        self.search()

    def search(self):
        sennheiser_response()
        jbl_response()
        skullcandy_response()

    def toggle_search(self, checkbox, brand):
        if checkbox.isChecked():
            self.search_brands.append(brand)
            self.search_button.setEnabled(True)
        else:
            self.search_brands.remove(brand)

            if len(self.search_brands) == 0:
                self.search_button.setEnabled(False)

    def display_results(self):
        self.results_table.setRowCount(0)

        with open("products.json") as f:
            file_data = json.load(f)

            current_row = 0

            for brand in self.search_brands:
                for product in file_data[brand]:
                    self.results_table.insertRow(current_row)

                    item_name = QtWidgets.QTableWidgetItem(product.get("name"))
                    item_name.setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))

                    item_img = QtGui.QPixmap(product.get("image_url"))
                    img_label = QtWidgets.QLabel()
                    img_label.setPixmap(item_img)

                    item_price = QtWidgets.QTableWidgetItem("$" + product.get("price"))
                    item_price.setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))

                    item_brand = QtWidgets.QTableWidgetItem(brand)
                    item_brand.setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))

                    self.results_table.setItem(current_row, 0, item_name)
                    self.results_table.setCellWidget(current_row, 1, img_label)
                    self.results_table.setItem(current_row, 2, item_price)
                    self.results_table.setItem(current_row, 3, item_brand)

                    current_row += 1


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
