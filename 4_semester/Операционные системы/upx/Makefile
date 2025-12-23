all: elf.c encrypt.c main.c upx_start.asm upx_end.asm
		nasm -f elf64 upx_start.asm
		nasm -f elf64 upx_end.asm
		gcc -o main.exe upx_start.o main.c upx_end.o
		gcc -o encrypt.exe encrypt.c
		gcc -o elf.exe elf.c
clean:
		rm -f *.exe *.o
