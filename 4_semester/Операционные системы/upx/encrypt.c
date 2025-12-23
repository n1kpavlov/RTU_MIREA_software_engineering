#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/mman.h>

const unsigned char mask = 0xAA;

#define UPX_OFFSET 4841
#define UPX_SIZE 28

void apply_mask(unsigned char *data, size_t size) {
    for (size_t i = 0; i < size; i++) {
        data[i] ^= mask;
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <binary>\n", argv[0]);
        return 1;
    }

    int fd = open(argv[1], O_RDWR);
    if (fd == -1) {
        perror("open");
        return 1;
    }

    off_t file_size = lseek(fd, 0, SEEK_END);
    if (file_size == -1) {
        perror("lseek");
        close(fd);
        return 1;
    }

    // отображаем файл в память
    unsigned char *data = mmap(NULL, file_size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (data == MAP_FAILED) {
        perror("mmap");
        close(fd);
        return 1;
    }

    // шифруем
    apply_mask(data + UPX_OFFSET, UPX_SIZE);

    msync(data, file_size, MS_SYNC);
    munmap(data, file_size);
    close(fd);

    return 0;
}
