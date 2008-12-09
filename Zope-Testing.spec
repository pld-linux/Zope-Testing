Summary:	Support for different testing frameworks
Summary(pl.UTF-8):	Obsługa różnych szkieletów testowych
Name:		Zope-Testing
Version:	3.7.1
Release:	1
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/z/zope.testing/zope.testing-%{version}.tar.gz
# Source0-md5:	23e9389228c79f4343e6b299d7d51fc0
URL:		http://www.zope.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a number of testing frameworks. It includes a
flexible test runner, and supports both doctest and unittest.

%description -l pl.UTF-8
Ten pakiet udostępnia wiele szkieletów testowych. Zawiera elastyczne
narzędzie do uruchamiania testów, obsługuje zarówno doctest jak i
unittest.

%prep
%setup -q -n zope.testing-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--install-purelib=%{py_sitedir} \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/zope/testing
%{py_sitedir}/zope.testing-*.egg-info
%{py_sitedir}/zope.testing-*-nspkg.pth
