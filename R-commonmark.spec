#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-commonmark
Version  : 1.7
Release  : 38
URL      : https://cran.r-project.org/src/contrib/commonmark_1.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/commonmark_1.7.tar.gz
Summary  : High Performance CommonMark and Github Markdown Rendering in R
Group    : Development/Tools
License  : BSD-2-Clause
Requires: R-commonmark-lib = %{version}-%{release}
BuildRequires : R-rlang
BuildRequires : R-xml2
BuildRequires : buildreq-R
BuildRequires : util-linux

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
%setup -q -c -n commonmark

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571812355

%install
export SOURCE_DATE_EPOCH=1571812355
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library commonmark
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library commonmark
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library commonmark
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc commonmark || :


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
