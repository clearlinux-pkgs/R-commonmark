#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: fae1327
#
Name     : R-commonmark
Version  : 1.9.1
Release  : 70
URL      : https://cran.r-project.org/src/contrib/commonmark_1.9.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/commonmark_1.9.1.tar.gz
Summary  : High Performance CommonMark and Github Markdown Rendering in R
Group    : Development/Tools
License  : BSD-2-Clause
Requires: R-commonmark-lib = %{version}-%{release}
BuildRequires : R-xml2
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
syntax. This package uses the 'cmark' reference implementation for converting
    markdown text into various formats including html, latex and groff man. In
    addition it exposes the markdown parse tree in xml format. Also includes opt-in
    support for GFM extensions including tables, autolinks, and strikethrough text.

%package lib
Summary: lib components for the R-commonmark package.
Group: Libraries

%description lib
lib components for the R-commonmark package.


%prep
%setup -q -n commonmark
pushd ..
cp -a commonmark buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1706633623

%install
export SOURCE_DATE_EPOCH=1706633623
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/commonmark/DESCRIPTION
/usr/lib64/R/library/commonmark/INDEX
/usr/lib64/R/library/commonmark/LICENSE
/usr/lib64/R/library/commonmark/Meta/Rd.rds
/usr/lib64/R/library/commonmark/Meta/features.rds
/usr/lib64/R/library/commonmark/Meta/hsearch.rds
/usr/lib64/R/library/commonmark/Meta/links.rds
/usr/lib64/R/library/commonmark/Meta/nsInfo.rds
/usr/lib64/R/library/commonmark/Meta/package.rds
/usr/lib64/R/library/commonmark/NAMESPACE
/usr/lib64/R/library/commonmark/NEWS
/usr/lib64/R/library/commonmark/R/commonmark
/usr/lib64/R/library/commonmark/R/commonmark.rdb
/usr/lib64/R/library/commonmark/R/commonmark.rdx
/usr/lib64/R/library/commonmark/help/AnIndex
/usr/lib64/R/library/commonmark/help/aliases.rds
/usr/lib64/R/library/commonmark/help/commonmark.rdb
/usr/lib64/R/library/commonmark/help/commonmark.rdx
/usr/lib64/R/library/commonmark/help/paths.rds
/usr/lib64/R/library/commonmark/html/00Index.html
/usr/lib64/R/library/commonmark/html/R.css
/usr/lib64/R/library/commonmark/tests/testthat.R
/usr/lib64/R/library/commonmark/tests/testthat/test-extensions.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/commonmark/libs/commonmark.so
/usr/lib64/R/library/commonmark/libs/commonmark.so.avx2
/usr/lib64/R/library/commonmark/libs/commonmark.so.avx512
