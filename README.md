# Just a simple windows worm.

## Italiano

Questo è un semplice worm per windows scritto in python.

### Funzioni.
1. E' scritto in python ed è semplice da modificare.
2. Prima di exploitare i target fa una scansione della rete per trovare porte 445 aperte.
3. Exploita smbghost che garantisce **NT AUTHORITY\SYSTEM**

### Difetti
1. Per il momento exploita solo smbghost (CVE-2020-0796).
2. Per il momento compromette SMB v3.11 con compressione attiva.

### Da fare
1. Aggiungere più exploit.

### Crediti
SMBGhost exploit: https://github.com/chompie1337/SMBGhost_RCE_PoC

Se volte contribuire al progetto fate pure, approverò quasi tutte le pull requests.

## English

### Functions.
1. It is written in python and is easy to modify.
2. Before exploiting targets it scans the network for open 445 ports.
3. Exploits smbghost which guarantees **NT AUTHORITY\SYSTEM**.

### Flaws
1. For the time being it only exploits smbghost (CVE-2020-0796).
2. For the time being it compromises SMB v3.11 with active compression.

### To do
1. Add more exploits.

### Credits
SMBGhost exploit: https://github.com/chompie1337/SMBGhost_RCE_PoC

If you want to contribute to the project go ahead, I will approve almost all pull requests.
