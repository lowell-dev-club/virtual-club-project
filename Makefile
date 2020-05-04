init:
	pip3 install -r requirements.txt

clean:
	pystarter clean

test:
	pytest

run: clean
	python3 run.py