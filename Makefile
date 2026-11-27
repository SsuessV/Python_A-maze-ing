


install: requirements.txt
	pip install -r requirements.txt

run:
	python3 maze_generator.py 

clean:
	rm -rf __pycache__
