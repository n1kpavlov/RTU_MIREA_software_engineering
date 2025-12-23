#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import stat
import errno
from urllib.parse import quote

import fuse
from fuse import Fuse
import requests

# Использовать FUSE Python API version 0.2
fuse.fuse_python_api = (0, 2)


class default_stat(fuse.Stat):
    def init(self):
        self.st_mode = 0
        self.st_ino = 0
        self.st_dev = 0
        self.st_nlink = 0
        self.st_uid = 0
        self.st_gid = 0
        self.st_size = 0
        self.st_atime = 0
        self.st_mtime = 0
        self.st_ctime = 0


class simple_fuse(Fuse):
    API_ROOT = "http://127.0.0.1:8000/library"
    _data = {}

    # Отключаем кеширование, чтобы сразу видеть изменения
    direct_io = True
    entry_timeout = 0
    attr_timeout = 0

    def getentry(self, path):
        print(path)
        if path in ("", "/", ".", ".."):
            url = self.API_ROOT
        else:
            url = f"{self.API_ROOT}/{quote(path.lstrip('/'))}"
        r = requests.get(url)
        return json.loads(r.content) if r.ok else -errno.ENOENT
    
    def getattr(self, path):
        # Директория-«корень»
        if path in ('/', '.', '..'):
            st = default_stat()
            st.st_mode = stat.S_IFDIR | 0o644
            st.st_nlink = 2
            return st

        name = path.lstrip('/')

        # Если файл есть в буфере
        if name in self._data:
            st = default_stat()
            st.st_mode = stat.S_IFREG | 0o644
            st.st_nlink = 1
            st.st_size = len(self._data[name])
            return st

        entry = self.getentry(path)
        if entry == -errno.ENOENT:
            return -errno.ENOENT

        st = default_stat()
        if 'papka' in entry:
            st.st_mode = stat.S_IFDIR | 0o644
            st.st_nlink = 2
        else:
            st.st_mode = stat.S_IFREG | 0o644
            st.st_nlink = 1
            st.st_size = len(entry.get('file_stih', ''))
        return st

    def readdir(self, path, offset):
        entry = self.getentry(path)
        if entry == -errno.ENOENT or 'papka' not in entry:
            return -errno.ENOENT

        names = set(entry['papka']).union(self._data.keys())
        for name in ['.', '..'] + sorted(names):
            yield fuse.Direntry(name)

    def open(self, path, flags):
        return 0

    def read(self, path, size, offset):
        name = path.lstrip('/')
        self._data.pop(name, None)
        if name in self._data:
            buf = self._data[name]
            return buf[offset:offset + size]

        entry = self.getentry(path)
        if entry == -errno.ENOENT or 'file_stih' not in entry:
            return -errno.ENOENT

        data = entry['file_stih'].encode('utf-8')
        return data[offset:offset + size]

    def write(self, path, buf, offset):
        name = path.lstrip('/')
        old = self._data.get(name)
        if old is None:
            entry = self.getentry(path)
            old = entry.get('file_stih', '').encode('utf-8') if entry != -errno.ENOENT else b""

        data = bytearray(old)
        data[offset:offset + len(buf)] = buf
        self._data[name] = bytes(data)

        r = requests.put(
            f"{self.API_ROOT}/{quote(name)}",
            data=self._data[name],
            headers={"Content-Type": "application/octet-stream"}
        )
        return len(buf) if r.ok else -errno.EIO

    def truncate(self, path, size):
        name = path.lstrip('/')
        old = self._data.get(name, b"")
        new = old[:size].ljust(size, b'\x00')
        self._data[name] = new
        requests.put(f"{self.API_ROOT}/{quote(name)}", data=new)
        return 0

    def create(self, path, flags, mode):
        name = path.lstrip('/')
        r = requests.post(f"{self.API_ROOT}/{quote(name)}")
        if r.ok:
            self._data[name] = b""
            return 0
        else:
            return -errno.EIO

    def unlink(self, path):
        name = path.lstrip('/')
        requests.delete(f"{self.API_ROOT}/{quote(name)}")
        self._data.pop(name, None)
        return 0

    def utimens(self, path, times):
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: driverfs.py <mountpoint>")
        sys.exit(1)
    mountpoint = sys.argv[1]

    driver = simple_fuse(
        version="%prog " + fuse.__version__,
        usage=Fuse.fusage,
        dash_s_do="setsingle"
    )
    driver.parse(["-o", "direct_io", mountpoint], errex=1)
    driver.main()