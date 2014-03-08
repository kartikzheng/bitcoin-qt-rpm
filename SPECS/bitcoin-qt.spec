Name:		bitcoin	
Version:	0.8.6
Release:	1%{?dist}
Summary:	Installs the Bitcoin-Qt Wallet

License:	MIT
URL:		https://bitcoin.org
Source0:	https://bitcoin.org/bin/%{version}/%{name}-%{version}-linux.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-root

Requires: qt-devel, boost-devel, db4-devel, zlib-devel

%description
Bitcoin-Qt Wallet

%prep
%setup -q -n %{name}-%{version}-linux

%build

%install
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"
mkdir -p %{buildroot}%{_bindir}
cp -R bin/64/* %{buildroot}%{_bindir}

%clean
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"

%files
%doc README.md COPYING
%{_bindir}/*

%changelog
* Fri Mar 8 2014 Adrian Hannigan <ahannigan01@gmail.com> 0.8.6-1
- Initial RPM
