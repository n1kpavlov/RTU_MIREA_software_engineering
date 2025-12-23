#include <cstdint>

static int key = 0;

extern "C" {
    void set_key(int n) {
        key = n % 8;
    }

    void encrypt(unsigned char* dst, const unsigned char* src, int len) {
        for (int i = 0; i < len; ++i) {
            dst[i] = (src[i] >> key) | (src[i] << (8 - key));
        }
    }

    void decrypt(unsigned char* dst, const unsigned char* src, int len) {
        for (int i = 0; i < len; ++i) {
            dst[i] = (src[i] << key) | (src[i] >> (8 - key));
        }
    }
}