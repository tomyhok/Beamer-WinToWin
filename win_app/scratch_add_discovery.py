import re

with open(r'C:\Projects\beamer\win_app\kvm_bridge_win.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add QComboBox and QTimer import
content = content.replace('QCheckBox,', 'QCheckBox,\n    QComboBox,\n    QTimer,')

# Add discovery init
content = content.replace(
    'self.announcer = Announcer(self._announced_port, self.bridge.paired.emit, logger=LOGGER)',
    'self.announcer = Announcer(self._announced_port, self.bridge.paired.emit, logger=LOGGER)\n        self.discovery = pairing.Discovery(logger=LOGGER)'
)

# Add UI to _pairing_block
ui_code = """
        self.find_button = QPushButton("Find a PC to pair with")
        self.find_button.setProperty("vernier", "primary")
        self.find_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.find_button.clicked.connect(self._start_discovery)
        module.body.addWidget(self.find_button, 0, Qt.AlignmentFlag.AlignLeft)

        self.discovery_block = QWidget()
        discovery_layout = QVBoxLayout(self.discovery_block)
        discovery_layout.setContentsMargins(0, 8, 0, 0)
        
        self.pc_list = QComboBox()
        self.pc_list.currentIndexChanged.connect(self._on_pc_selected)
        discovery_layout.addWidget(QLabel("Select discovered PC:"))
        discovery_layout.addWidget(self.pc_list)
        
        self.manual_address = QLineEdit()
        self.manual_address.setPlaceholderText("Or enter PC address manually")
        self.manual_address.textChanged.connect(self._on_manual_address)
        discovery_layout.addWidget(self.manual_address)
        
        self.client_code = QLineEdit()
        self.client_code.setPlaceholderText("6-digit code")
        discovery_layout.addWidget(self.client_code)
        
        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self._connect_to_pc)
        self.connect_button.setProperty("vernier", "primary")
        discovery_layout.addWidget(self.connect_button)
        
        self.discovery_block.setVisible(False)
        module.body.addWidget(self.discovery_block)
        
        self.discovery_timer = QTimer(self)
        self.discovery_timer.timeout.connect(self._poll_discovery)
"""
content = content.replace('layout.addWidget(module)', ui_code + '\n        layout.addWidget(module)')

# Add methods
methods_code = """
    def _start_discovery(self) -> None:
        self.discovery_block.setVisible(True)
        self.find_button.setVisible(False)
        self.discovery.start()
        self.discovery_timer.start(1000)

    def _poll_discovery(self) -> None:
        pcs = self.discovery.pcs()
        current_data = [self.pc_list.itemData(i) for i in range(self.pc_list.count())]
        for pc in pcs:
            if pc not in current_data:
                self.pc_list.addItem(f"{pc.get('name', 'Unknown PC')} ({pc.get('address')})", pc)

    def _on_pc_selected(self, index: int) -> None:
        if index >= 0:
            pc = self.pc_list.itemData(index)
            if pc:
                self.manual_address.setText(pc.get("address", ""))

    def _on_manual_address(self, text: str) -> None:
        if self.pc_list.currentIndex() >= 0:
            pc = self.pc_list.itemData(self.pc_list.currentIndex())
            if pc and text != pc.get("address"):
                self.pc_list.setCurrentIndex(-1)

    def _connect_to_pc(self) -> None:
        code = self.client_code.text().strip()
        if not code:
            return
            
        address = self.manual_address.text().strip()
        if not address:
            return
            
        # find matching pc in pcs if possible
        pc = None
        for p in self.discovery.pcs():
            if p.get("address") == address:
                pc = p
                break
                
        if not pc:
            # Create a fake pc dict for manual connection
            pc = {"address": address, "reply_port": pairing.PAIRING_PORT, "pairing": pairing.PAIRING_VERSION, "pair_id": "manual"}
            self.discovery.find(address)
            
        def _do_pair():
            try:
                token, name = self.discovery.pair(pc, code, pairing.machine_name())
                self.bridge.paired.emit(token, name, address)
            except Exception as e:
                LOGGER.error(f"Pairing failed: {e}")
                
        import threading
        threading.Thread(target=_do_pair, daemon=True).start()
"""

content = content.replace('def _show_paired(', methods_code + '\n    def _show_paired(')

with open(r'C:\Projects\beamer\win_app\kvm_bridge_win.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Discovery UI added.")
