#!/bin/bash
clear

BLACK='\e[30m'
RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m'
BLUE='\e[34m'
PURPLE='\e[35m'
CYAN='\e[36m'
WHITE='\e[37m'
NC='\e[0m'
echo""
echo -e "${GREEN}                                                                "                                                                                  
echo "
██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝
██║  ██║█████╗  ██║  ██║███████╗█████╗  ██║     
██║  ██║██╔══╝  ██║  ██║╚════██║██╔══╝  ██║     
██████╔╝███████╗██████╔╝███████║███████╗╚██████╗
╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝                                       
"
echo "                                                               "                                                                    
echo -e "${GREEN}                                          ~@~ Coded By Kryp3ton ~@~ ${NC}"
echo ""
echo -e "${GREEN}  Instagram.com/Kryp3ton | github.com/Kryp3ton/Dedsec-2.0 ${NC} "
echo ""
echo "---------------------------------------------------------------------------------------"
echo ""
echo -e "${RED}[!] Questo tool viene eseguito come amministratore [!]${NC}"
echo ""
echo -e "${CYAN}[>] Premi Enter per installare Ctrl+C per terminare.${NC}"
read INPUT
echo ""

if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/DEDSEC"
    BIN_DIR="$PREFIX/usr/bin/"
    pkg install -y git python2
else
    INSTALL_DIR="/usr/share/doc/DEDSEC"
    BIN_DIR="/usr/bin/"
fi

echo "[✔] Controllo le directory...";
if [ -d "$INSTALL_DIR" ]; then
    echo "[!] La directory DEDSEC esiste gia... vuoi rimpiazzarla ? [y/n]:" ;
    read mama
    if [ "$mama" = "y" ]; then
        rm -R "$INSTALL_DIR"
    else
        exit
    fi
fi

echo "[✔] Download in corso ...";
echo "";
git clone https://github.com/Kryp3ton/Dedsec-2.0.git "$INSTALL_DIR";
echo "#!/bin/bash
python $INSTALL_DIR/dedsec.py" '${1+"$@"}' > DEDSEC;
chmod +x DEDSEC;
sudo cp DEDSEC /usr/bin/;
rm DEDSEC;


if [ -d "$INSTALL_DIR" ] ;
then
    echo "";
    echo "[✔] Download avvenuto con successo !!! [✔]";
    echo "";
    echo "[✔]=======================================================================================[✔]";
    echo "[✔] ✔✔✔ Tutto completato correttamente... Puoi eseguire i tool scrivendo DEDSEC !! ✔✔✔ [✔]";
    echo "[✔]=======================================================================================[✔]";
    echo "";
else
    echo "[✘] Download fallito !!! [✘]";
    exit
fi