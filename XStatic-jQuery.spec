#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-jQuery
Version  : 3.3.1.1
Release  : 23
URL      : https://files.pythonhosted.org/packages/b5/c8/b254c4b7b9421086bbb00cc04fa13d002db206dd832940864cc54723453c/XStatic-jQuery-3.3.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b5/c8/b254c4b7b9421086bbb00cc04fa13d002db206dd832940864cc54723453c/XStatic-jQuery-3.3.1.1.tar.gz
Summary  : jQuery 3.3.1 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-jQuery-python = %{version}-%{release}
Requires: XStatic-jQuery-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
--------------
        
        jQuery javascript library packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package `XStatic`.

%package python
Summary: python components for the XStatic-jQuery package.
Group: Default
Requires: XStatic-jQuery-python3 = %{version}-%{release}
Provides: xstatic-jquery-python

%description python
python components for the XStatic-jQuery package.


%package python3
Summary: python3 components for the XStatic-jQuery package.
Group: Default
Requires: python3-core

%description python3
python3 components for the XStatic-jQuery package.


%prep
%setup -q -n XStatic-jQuery-3.3.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1561578360
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
