echo "antes de empezar se le informa que se instalaran distintos modulos de python de ser necesario, ¿desea continuar? [y/n]"
read x

if [ "${x,,}" = "y" ]; then
	python3 -m venv --help >/dev/null 2>&1
	if [ $? -eq 0 ]; then
		mkdir TP2-IDS
		mv static templates app.py README.md requirements.txt TP2-IDS/
		cd TP2-IDS
		python3 -m venv .venv
		source .venv/bin/activate
		pip install -r requirements.txt
		echo "instalacion completada"
	else
		echo "venv no instalado, instalelo y vuelva a intentar"
	fi
fi
