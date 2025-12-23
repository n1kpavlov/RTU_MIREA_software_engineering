all: lib.so main.exe

lib.so: lib.cpp
	g++ -shared -fPIC -o lib.so lib.cpp

main.exe: main.cpp
	g++ -o main.exe main.cpp -ldl

clean:
	rm -f lib.so main.exe