Summary:	zope.testing package used in Zope 3
Name:		Zope-Testing
Version:	3.5.0
Release:	0.1
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://download.zope.org/distribution/zope.testing-%{version}.tar.gz
# Source0-md5:	3e482a31cc6c6dac8d7abd0b0e146da4
URL:		http://www.zope.org/Products/ZopeInterface/
BuildRequires:	python
BuildRequires:	python-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zope.testing package used in Zope 3.

%prep
%setup -q -n zope.testing-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%{py_postclean}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/zope/testing
%{py_sitescriptdir}/zope*egg*
%{py_sitescriptdir}/zope*pth
