.PHONY : env
env: 
	conda env update --file environment.yml --prune --name ligo

.PHONY : html
html : 
	myst build --html

.PHONY : clean
clean : 
	rm -f figures/* audio/* _build/* 