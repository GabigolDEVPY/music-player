# Arquitetura do Projeto - Music Player (Simplificada)

## 🎯 Filosofia: Simples, Prático e Escalável

- ✅ Sem banco de dados (apenas JSON)
- ✅ 3 camadas principais (não 5)
- ✅ Fácil de entender e implementar
- ✅ Preparado para testes
- ✅ Separa responsabilidades

---

## 📊 Estrutura Visual

```
COMPONENTES (UI)
       ↕ (sinais/slots)
CONTROLLERS (Orquestração)
       ↕
SERVICES (Lógica + Persistência)
       ↕
MODELS (Tipos de dados)
```

---

## 📁 Estrutura de Pastas - Simples

```
Player_music/
│
├── 📄 app.py                        # Entry point
├── 📄 main_window.py                # Main Controller
├── 📄 pytest.ini                    # Config pytest
├── 📄 requirements.txt
│
├── 📁 config/
│   ├── __init__.py
│   └── constants.py                 # Constantes globais
│
├── 📁 models/
│   ├── __init__.py
│   ├── music.py                     # @dataclass Music
│   ├── playlist.py                  # @dataclass Playlist  
│   └── enums.py                     # RepeatMode, ShuffleMode
│
├── 📁 services/
│   ├── __init__.py
│   ├── music_service.py             # Busca/parse de .mp3
│   ├── player_service.py            # Play/pause/next/prev
│   └── storage_service.py           # Salva/carrega JSON
│
├── 📁 controllers/
│   ├── __init__.py
│   ├── player_controller.py         # Orquestra player
│   ├── library_controller.py        # Orquestra biblioteca
│   └── panel_controller.py          # Troca painéis
│
├── 📁 components/
│   ├── __init__.py
│   ├── interface.py                 # Main window
│   ├── player_control.py            # Botões
│   ├── search_bar.py                # Busca
│   ├── side_panel.py                # Painel lateral
│   ├── music_card.py                # Card música
│   ├── marquee_label.py
│   └── youtube_panel.py
│
├── 📁 utils/
│   ├── __init__.py
│   ├── validators.py                # Validações
│   └── formatters.py                # Formatar dados
│
├── 📁 data/
│   ├── save.json                    # Config persistida
│   └── cache/                       # (opcional)
│
├── 📁 musicas/                      # Biblioteca do usuário
│
└── 📁 tests/                        # Testes
    ├── __init__.py
    ├── conftest.py
    ├── test_models.py
    ├── test_services.py
    └── test_controllers.py
```

---

## 🔄 Fluxo Simples

```
1. Usuário clica botão (Components)
2. Signal vai para Controller
3. Controller chama Service
4. Service executa lógica
5. Service persiste em JSON (se necessário)
```

**Exemplo Visual:**

```
[Button Play] → PlayerController → PlayerService → storage_service.py
(UI)              (orquestra)         (lógica)         (JSON)
```

---

## 💾 Models (Tipos de Dados)

### models/music.py
```python
from dataclasses import dataclass
from pathlib import Path
from PySide6.QtGui import QPixmap

@dataclass
class Music:
    """Representa uma música"""
    title: str
    artist: str
    duration: str      # "MM:SS"
    path: Path
    icon: QPixmap = None
    
    def __str__(self) -> str:
        return f"{self.artist} - {self.title}"
```

### models/enums.py
```python
from enum import Enum

class RepeatMode(Enum):
    OFF = 0
    ONE = 1
    ALL = 2

class ShuffleMode(Enum):
    OFF = False
    ON = True
```

---

## 🔧 Services (Lógica de Negócio + Persistência)

### services/music_service.py
```python
from pathlib import Path
from models.music import Music

class MusicService:
    @staticmethod
    def get_musics_from_path(path: str) -> list[Music]:
        """Busca todas as músicas de um caminho"""
        musics = []
        for file in Path(path).glob("*.mp3"):
            music = Music(
                title="Song",
                artist="Artist",
                duration="3:45",
                path=file
            )
            musics.append(music)
        return musics
```

### services/player_service.py
```python
from models.music import Music
from models.enums import RepeatMode

class PlayerService:
    def __init__(self, qmedia_player):
        self.player = qmedia_player
        self.playlist: list[Music] = []
        self.current_index = 0
        self.repeat_mode = RepeatMode.OFF
        self.is_shuffle = False
    
    def play(self, music: Music) -> bool:
        """Toca uma música"""
        try:
            self.player.setSource(QUrl.fromLocalFile(music.path))
            self.player.play()
            return True
        except Exception as e:
            print(f"Erro ao tocar: {e}")
            return False
    
    def pause(self) -> bool:
        """Pausa a reprodução"""
        self.player.pause()
        return True
    
    def next(self) -> Music | None:
        """Próxima música da playlist"""
        if not self.playlist:
            return None
        self.current_index = (self.current_index + 1) % len(self.playlist)
        return self.playlist[self.current_index]
```

### services/storage_service.py
```python
import json
from pathlib import Path
from models.music import Music

class StorageService:
    def __init__(self, save_path: str = "data/save.json"):
        self.save_path = Path(save_path)
    
    def save_config(self, volume: int, current_music: Music = None) -> bool:
        """Salva configurações em JSON"""
        try:
            data = {
                "volume": volume,
                "current_music": str(current_music.path) if current_music else None
            }
            self.save_path.write_text(json.dumps(data, indent=2))
            return True
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False
    
    def load_config(self) -> dict:
        """Carrega configurações do JSON"""
        try:
            if self.save_path.exists():
                return json.loads(self.save_path.read_text())
        except Exception as e:
            print(f"Erro ao carregar: {e}")
        return {"volume": 70, "current_music": None}
```

---

## 🎮 Controllers (Orquestração)

### controllers/player_controller.py
```python
from services.player_service import PlayerService
from models.music import Music

class PlayerController:
    def __init__(self, player_service: PlayerService):
        self.service = player_service
    
    def handle_play_music(self, music: Music) -> bool:
        """Handler para selecionar música"""
        return self.service.play(music)
    
    def handle_pause(self) -> bool:
        """Handler para pausar"""
        return self.service.pause()
    
    def handle_next(self) -> Music | None:
        """Handler para próxima"""
        return self.service.next()
    
    def handle_set_shuffle(self, enabled: bool) -> None:
        """Handler para shuffle"""
        self.service.is_shuffle = enabled
```

### controllers/library_controller.py
```python
from services.music_service import MusicService
from models.music import Music

class LibraryController:
    def __init__(self, music_service: MusicService):
        self.service = music_service
    
    def load_music_library(self, path: str) -> list[Music]:
        """Carrega biblioteca de um caminho"""
        return self.service.get_musics_from_path(path)
    
    def search_music(self, musics: list[Music], query: str) -> list[Music]:
        """Filtra músicas por nome/artista"""
        query_lower = query.lower()
        return [
            m for m in musics 
            if query_lower in m.title.lower() or 
               query_lower in m.artist.lower()
        ]
```


---

## 🔗 Como Conectar Tudo - main_window.py

```python
from PySide6.QtWidgets import QApplication
from components.interface import SpotifyInterface
from services.player_service import PlayerService
from services.music_service import MusicService
from services.storage_service import StorageService
from controllers.player_controller import PlayerController
from controllers.library_controller import LibraryController

class MainController(SpotifyInterface):
    def __init__(self):
        super().__init__()
        
        # Services (lógica)
        self.player_service = PlayerService(self.player.music_player)
        self.music_service = MusicService()
        self.storage_service = StorageService("data/save.json")
        
        # Controllers (orquestra)
        self.player_controller = PlayerController(self.player_service)
        self.library_controller = LibraryController(self.music_service)
        
        # Conectar sinais
        self.player.play_btn.clicked.connect(
            lambda: self.player_controller.handle_play_music(self.current_music)
        )
        self.player.pause_btn.clicked.connect(
            self.player_controller.handle_pause
        )
        
        # Carregar config
        config = self.storage_service.load_config()
        self.player.volume_slider.setValue(config["volume"])
```

---

## 📝 Guia de Implementação (6 passos)

### 1️⃣ Criar Models
- [ ] Criar `models/music.py` com `@dataclass Music`
- [ ] Criar `models/playlist.py` 
- [ ] Criar `models/enums.py` com RepeatMode

### 2️⃣ Criar Services
- [ ] Refatorar `services/music_service.py` (remove UI)
- [ ] Criar `services/player_service.py`
- [ ] Criar `services/storage_service.py`

### 3️⃣ Criar/Refatorar Controllers
- [ ] Refatorar `controllers/player_controller.py`
- [ ] Refatorar `controllers/library_controller.py`
- [ ] Injetar services nos controllers

### 4️⃣ Refatorar Components
- [ ] Remover lógica de `components/`
- [ ] Apenas emitem sinais/slots
- [ ] Components não conhecem Services

### 5️⃣ Adicionar Testes
- [ ] Criar `tests/test_models.py`
- [ ] Criar `tests/test_services.py`
- [ ] Criar `tests/test_controllers.py`
- [ ] Rodar: `pytest`

### 6️⃣ Config e Utils
- [ ] Criar `config/constants.py`
- [ ] Criar `utils/formatters.py`
- [ ] Criar `utils/validators.py`

---

## ⚡ Comandos Úteis

```bash
# Rodar testes
pytest

# Rodar com coverage
pytest --cov=services --cov=controllers --cov=models

# Rodar teste específico
pytest tests/test_services.py::test_next_music -v

# Rodar aplicação
python app.py
```

---

## 📌 Regras Importantes

| Lugar | Pode? | Exemplo |
|-------|-------|---------|
| **Components** | Emitir sinais ✅ | `self.button.clicked.connect(handler)` |
| **Components** | Lógica ❌ | Não fazer `if`, loops, cálculos |
| **Controllers** | Chamar Services ✅ | `self.service.play(music)` |
| **Controllers** | Lógica UI ❌ | Não manipular widgets direto |
| **Services** | Lógica pura ✅ | `next()`, `shuffle()`, etc |
| **Services** | Importar PySide6 ❌ | Services não conhecem UI |

---

## 🚀 Resultado Final

✅ Código modular e testável
✅ Separação clara de responsabilidades
✅ Fácil de debugar
✅ Fácil de expandir
✅ Sem banco de dados (apenas JSON)

---

## 📚 Resumo: Antes vs Depois

**ANTES (Problema):**
```
PlayerController {
  - Manipula UI
  - Salva dados
  - Lógica de negócio
  - Estado
}
```

**DEPOIS (Solução):**
```
PlayerService {
  - Apenas lógica: play(), next(), pause()
}

PlayerController {
  - Apenas orquestração: "chama service, avisa component"
}

Components {
  - Apenas UI: recebe signals, renderiza
}
```

---

**Pronto para começar? Segue a implementação passo a passo!** 🎉
