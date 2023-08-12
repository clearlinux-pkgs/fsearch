#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : fsearch
Version  : 0.2.3
Release  : 8
URL      : https://github.com/cboxdoerfer/fsearch/archive/0.2.3/fsearch-0.2.3.tar.gz
Source0  : https://github.com/cboxdoerfer/fsearch/archive/0.2.3/fsearch-0.2.3.tar.gz
Summary  : A fast file search utility for Unix-like systems based on GTK+3
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: fsearch-bin = %{version}-%{release}
Requires: fsearch-data = %{version}-%{release}
Requires: fsearch-license = %{version}-%{release}
Requires: fsearch-locales = %{version}-%{release}
Requires: fsearch-man = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : autoconf-archive-dev
BuildRequires : buildreq-meson
BuildRequires : desktop-file-utils
BuildRequires : glib
BuildRequires : glib-bin
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
FSearch is a fast file search utility, inspired by Everything Search Engine. It's written in C and based on GTK 3.

%package bin
Summary: bin components for the fsearch package.
Group: Binaries
Requires: fsearch-data = %{version}-%{release}
Requires: fsearch-license = %{version}-%{release}

%description bin
bin components for the fsearch package.


%package data
Summary: data components for the fsearch package.
Group: Data

%description data
data components for the fsearch package.


%package license
Summary: license components for the fsearch package.
Group: Default

%description license
license components for the fsearch package.


%package locales
Summary: locales components for the fsearch package.
Group: Default

%description locales
locales components for the fsearch package.


%package man
Summary: man components for the fsearch package.
Group: Default

%description man
man components for the fsearch package.


%prep
%setup -q -n fsearch-0.2.3
cd %{_builddir}/fsearch-0.2.3
pushd ..
cp -a fsearch-0.2.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1691798774
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/fsearch
cp %{_builddir}/fsearch-%{version}/License %{buildroot}/usr/share/package-licenses/fsearch/179ed4834368188595c686f81ba1ba6ab8dd0a19 || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang fsearch
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/fsearch
/usr/bin/fsearch

%files data
%defattr(-,root,root,-)
/usr/share/applications/io.github.cboxdoerfer.FSearch.desktop
/usr/share/icons/hicolor/scalable/apps/io.github.cboxdoerfer.FSearch.svg
/usr/share/metainfo/io.github.cboxdoerfer.FSearch.appdata.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fsearch/179ed4834368188595c686f81ba1ba6ab8dd0a19

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fsearch.1

%files locales -f fsearch.lang
%defattr(-,root,root,-)

