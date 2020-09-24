#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fsearch
Version  : 0.1beta4
Release  : 2
URL      : https://github.com/cboxdoerfer/fsearch/archive/v0.1beta4.tar.gz
Source0  : https://github.com/cboxdoerfer/fsearch/archive/v0.1beta4.tar.gz
Summary  : A fast file search utility for Unix-like systems based on GTK+3
Group    : Development/Tools
License  : GPL-2.0
Requires: fsearch-bin = %{version}-%{release}
Requires: fsearch-data = %{version}-%{release}
Requires: fsearch-license = %{version}-%{release}
Requires: fsearch-locales = %{version}-%{release}
BuildRequires : autoconf-archive-dev
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libpcre)

%description
[![Build Status](https://travis-ci.org/cboxdoerfer/fsearch.svg?branch=master)](https://travis-ci.org/cboxdoerfer/fsearch)
[![Translation status](https://hosted.weblate.org/widgets/fsearch/-/svg-badge.svg)](https://hosted.weblate.org/engage/fsearch/?utm_source=widget)

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


%prep
%setup -q -n fsearch-0.1beta4
cd %{_builddir}/fsearch-0.1beta4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587148466
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1587148466
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fsearch
cp %{_builddir}/fsearch-0.1beta4/License %{buildroot}/usr/share/package-licenses/fsearch/179ed4834368188595c686f81ba1ba6ab8dd0a19
%make_install
%find_lang fsearch

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fsearch

%files data
%defattr(-,root,root,-)
/usr/share/applications/fsearch.desktop

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fsearch/179ed4834368188595c686f81ba1ba6ab8dd0a19

%files locales -f fsearch.lang
%defattr(-,root,root,-)

