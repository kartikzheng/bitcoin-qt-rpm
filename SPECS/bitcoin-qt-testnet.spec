Name:		bitcoin
Version:	0.8.6
Release:	testnet%{?dist}
Summary:	Installs the Bitcoin-Qt Wallet (TestNet)

License:	MIT
URL:		https://bitcoin.org
Source0:	https://bitcoin.org/bin/%{version}/%{name}-%{version}-linux.tar.gz
Source1:	bitcoin.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-root

Requires: qt-devel, boost-devel, db4-devel, zlib-devel

%description
Bitcoin-Qt Wallet with default testnet bitcoin.conf

%define whoami %(whoami)

%prep
%setup -q -n %{name}-%{version}-linux

%build

%install
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"
mkdir -p %{buildroot}%{_bindir}
cp -R bin/64/* %{buildroot}%{_bindir}
mkdir -p %{buildroot}/home/%{whoami}/.bitcoin/
sed -i s/^rpcuser=/rpcuser=%{whoami}/ %{SOURCE1}
cp %{SOURCE1} %{buildroot}/home/%{whoami}/.bitcoin/

%clean
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"

%files
%doc README.md COPYING
%{_bindir}/*
%config(noreplace) /home/%{whoami}/.bitcoin/bitcoin.conf

%changelog
* Fri Mar 8 2014 Adrian Hannigan <ahannigan01@gmail.com> 0.8.6-1
- Initial testnet RPM
