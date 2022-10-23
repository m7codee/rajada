apt update;
apt upgrade -y;
apt install git -y;
termux-setup-storage;
cd ..;
cd storage/downloads;
git clone https://github.com/m7codee/rajada;
cd rajada;
apt install python3 -y
echo "Metodo de rajada - 10/s";
pip3 install pyaes;
while :
do
python3 rajada.py;
sleep 1      
done

