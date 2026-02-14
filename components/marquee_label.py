from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPainter


class MarqueeLabel(QLabel):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self._text = text
        self._offset = 0
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._update_offset)
        self._speed = 2  # velocidade do scroll

        self.setAlignment(Qt.AlignVCenter)
        self.setMinimumWidth(0)

    def setText(self, text):
        self._text = text
        self._offset = 0
        super().setText(text)

    def enterEvent(self, event):
        if self.fontMetrics().horizontalAdvance(self._text) > self.width():
            self._timer.start(30)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._timer.stop()
        self._offset = 0
        self.update()
        super().leaveEvent(event)

    def _update_offset(self):
        self._offset += self._speed
        text_width = self.fontMetrics().horizontalAdvance(self._text)
        if self._offset > text_width:
            self._offset = 0
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        text_width = self.fontMetrics().horizontalAdvance(self._text)

        if text_width <= self.width():
            painter.drawText(self.rect(), Qt.AlignVCenter, self._text)
        else:
            painter.drawText(-self._offset, 0, text_width, self.height(),
                             Qt.AlignVCenter, self._text)
            painter.drawText(text_width - self._offset + 50, 0,
                             text_width, self.height(),
                             Qt.AlignVCenter, self._text)