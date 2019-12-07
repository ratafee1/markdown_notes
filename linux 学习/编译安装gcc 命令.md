# 编译安装gcc 命令

 xz -d *.xz





MPFR=mpfr-2.4.2
GMP=gmp-4.3.2
MPC=mpc-0.8.1



```
tar xzf gcc-6.5.0.tar.gz
cd gcc-6.5.0
./contrib/download_prerequisites
cd ..
mkdir objdir
cd objdir
$PWD/../gcc-6.5.0/configure --prefix=$HOME/GCC-6.5.0 --enable-languages=c,c++,fortran,go
make
make install
```