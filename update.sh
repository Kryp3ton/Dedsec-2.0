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
echo -e "${GREEN}  Instagram.com/Kryp3ton | github.com/Kryp3ton/Ded-Sec/ ${NC} "
echo ""
echo "---------------------------------------------------------------------------------------"
echo ""
echo -e "${RED}[!] Questo tool viene eseguito come amministratore [!]${NC}"
echo ""
echo -e "${CYAN}[>] Premi Enter per eseguire un update Ctrl+C per terminare.${NC}"
read INPUT
echo ""

clear

sudo chmod +x /etc/

clear

sudo chmod +x /usr/share/doc

clear

sudo rm -rf /usr/share/doc/DEDSEC_toolbox/

clear

cd /etc/

clear

sudo rm -rf /etc/DEDSEC_toolbox

clear

mkdir DEDSEC_toolbox

clear

cd DEDSEC_toolbox

clear

git clone https://github.com/Kryp3ton/Dedsec_hackingtoolbox.git

clear


cd DEDSEC

clear

sudo chmod +x install.sh

clear

./install.sh

clear