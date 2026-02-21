import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt, QTimer, QPropertyAnimation

class MusicNotification(QWidget):
    def __init__(self, image_path, title, artist, description, parent=None):
        super().__init__(parent)
        
        # 1. Configurações da Janela
        # Frameless (sem borda), Tool (não aparece na barra de tarefas), StaysOnTop (sempre à frente)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint | 
            Qt.WindowType.Tool
        )
        # Permite bordas arredondadas e fundo transparente na janela base
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # 2. Container Principal (Estilização CSS-like)
        self.container = QWidget(self)
        self.container.setStyleSheet("""
            QWidget {
                background-color: #282c34; /* Fundo escuro elegante */
                border-radius: 12px;
                color: #ffffff;
            }
        """)
        
        # 3. Criando os Layouts
        main_layout = QHBoxLayout(self.container)
        main_layout.setContentsMargins(15, 15, 15, 15) # Margens internas
        text_layout = QVBoxLayout()
        text_layout.setSpacing(2) # Espaçamento entre os textos

        # 4. Configurando a Foto/Capa do Álbum
        self.image_label = QLabel()
        # Carrega a imagem e redimensiona mantendo a proporção com suavidade
        pixmap = QPixmap(image_path).scaled(
            70, 70, 
            Qt.AspectRatioMode.KeepAspectRatioByExpanding, 
            Qt.TransformationMode.SmoothTransformation
        )
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(70, 70)
        self.image_label.setStyleSheet("border-radius: 8px;")

        # 5. Configurando os Textos (Música, Artista e Descrição)
        self.title_label = QLabel(title)
        self.title_label.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        
        self.artist_label = QLabel(artist)
        self.artist_label.setFont(QFont("Segoe UI", 10))
        self.artist_label.setStyleSheet("color: #abb2bf;") # Cinza claro
        
        self.desc_label = QLabel(description)
        self.desc_label.setFont(QFont("Segoe UI", 9))
        self.desc_label.setStyleSheet("color: #7f848e;") # Cinza mais escuro

        # 6. Montando a Estrutura
        text_layout.addWidget(self.title_label)
        text_layout.addWidget(self.artist_label)
        text_layout.addWidget(self.desc_label)
        text_layout.addStretch() # Empurra os textos para o topo

        main_layout.addWidget(self.image_label)
        main_layout.addSpacing(10) # Espaço entre a imagem e o texto
        main_layout.addLayout(text_layout)
        
        # Define o tamanho final da notificação
        self.container.setFixedSize(360, 100)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.container)
        self.setFixedSize(360, 100)

        # 7. Posicionamento e Animação
        self.position_on_screen()
        self.animate_show()

        # Fecha a notificação automaticamente após 5000 milissegundos (5 segundos)
        QTimer.singleShot(5000, self.animate_close)

    def position_on_screen(self):
        """Posiciona a janela no canto inferior direito da tela primária."""
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        x = screen_geometry.width() - self.width() - 20  # 20px de margem da direita
        y = screen_geometry.height() - self.height() - 20 # 20px de margem de baixo
        self.move(x, y)

    def animate_show(self):
        """Cria um efeito de Fade In (Surgimento suave)."""
        self.setWindowOpacity(0.0)
        self.show()
        
        self.anim_in = QPropertyAnimation(self, b"windowOpacity")
        self.anim_in.setDuration(400) # Duração em ms
        self.anim_in.setStartValue(0.0)
        self.anim_in.setEndValue(1.0)
        self.anim_in.start()

    def animate_close(self):
        """Cria um efeito de Fade Out antes de destruir a janela."""
        self.anim_out = QPropertyAnimation(self, b"windowOpacity")
        self.anim_out.setDuration(400)
        self.anim_out.setStartValue(1.0)
        self.anim_out.setEndValue(0.0)
        # Quando a animação acabar, fecha a janela definitivamente
        self.anim_out.finished.connect(self.close) 
        self.anim_out.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Substitua "capa.jpg" por uma imagem que exista no seu computador
    notificacao = MusicNotification(
        image_path="capa.jpg", 
        title="Bohemian Rhapsody", 
        artist="Queen", 
        description="A Night at the Opera • 1975"
    )
    
    # Impede que o app feche imediatamente se não houver janela principal
    sys.exit(app.exec())