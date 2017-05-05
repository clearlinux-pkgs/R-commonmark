#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-commonmark
Version  : 1.2
Release  : 4
URL      : https://cran.r-project.org/src/contrib/commonmark_1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/commonmark_1.2.tar.gz
Summary  : High Performance CommonMark and Github Markdown Rendering in R
Group    : Development/Tools
License  : BSD-2-Clause
Requires: R-commonmark-lib
BuildRequires : clr-R-helpers

%description
No detailed description available

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
export LANG=C
export SOURCE_DATE_EPOCH=1493664211

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1493664211
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library commonmark
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library commonmark


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
/usr/lib64/R/library/commonmark/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/commonmark/libs/commonmark.so
