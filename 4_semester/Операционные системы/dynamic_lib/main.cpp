#include <iostream>
#include <fstream>
#include <vector>
#include <dlfcn.h>

typedef void (*set_key_func)(int);
typedef void (*crypt_func)(unsigned char*, const unsigned char*, int);

int main(int argc, char* argv[]) {
    if (argc != 6) {
        std::cerr << "Usage: " << argv[0] << " <lib.so> <n> <e/d> <input> <output>\n";
        return 1;
    }

    const char* lib_path = argv[1];
    int n = std::atoi(argv[2]);
    char mode = argv[3][0];
    const char* input_file = argv[4];
    const char* output_file = argv[5];

    void* handle = dlopen(lib_path, RTLD_LAZY);
    if (!handle) {
        std::cerr << "Cannot load library: " << dlerror() << '\n';
        return 1;
    }

    set_key_func set_key = (set_key_func)dlsym(handle, "set_key");
    crypt_func encrypt = nullptr;
    crypt_func decrypt = nullptr;

    if (mode == 'e') {
        encrypt = (crypt_func)dlsym(handle, "encrypt");
    } else if (mode == 'd') {
        decrypt = (crypt_func)dlsym(handle, "decrypt");
    } else {
        std::cerr << "Invalid mode. Use 'e' or 'd'.\n";
        dlclose(handle);
        return 1;
    }

    if (!set_key || (mode == 'e' && !encrypt) || (mode == 'd' && !decrypt)) {
        std::cerr << "Failed to load functions: " << dlerror() << '\n';
        dlclose(handle);
        return 1;
    }

    set_key(n);

    std::ifstream fin(input_file, std::ios::binary);
    if (!fin) {
        std::cerr << "Cannot open input file: " << input_file << '\n';
        dlclose(handle);
        return 1;
    }

    fin.seekg(0, std::ios::end);
    size_t len = fin.tellg();
    fin.seekg(0, std::ios::beg);

    std::vector<unsigned char> src(len);
    fin.read(reinterpret_cast<char*>(src.data()), len);
    fin.close();

    std::vector<unsigned char> dst(len);

    if (mode == 'e') {
        encrypt(dst.data(), src.data(), len);
    } else {
        decrypt(dst.data(), src.data(), len);
    }

    std::ofstream fout(output_file, std::ios::binary);
    if (!fout) {
        std::cerr << "Cannot open output file: " << output_file << '\n';
        dlclose(handle);
        return 1;
    }

    fout.write(reinterpret_cast<char*>(dst.data()), len);
    fout.close();

    dlclose(handle);
    return 0;
}