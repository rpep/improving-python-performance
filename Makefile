all: build run plot

build: clean
	python setup.py build_ext --inplace

run:
	python test.py

plot:
	python plot.py

clean:
	python setup.py clean --all
