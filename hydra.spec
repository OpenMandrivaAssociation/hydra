Name:		hydra
Version:	7.5
Release:	1
Summary:	Network logon cracker
License:	GPLv3
Group:		Monitoring
URL:		http://www.thc.org/thc-hydra/
Source0:	http://freeworld.thc.org/releases/hydra-%{version}.tar.gz
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: subversion-devel
BuildRequires: mysql-devel
BuildRequires: postgresql-devel
BuildRequires: firebird-devel
BuildRequires: ssh-devel
BuildRequires: idn-devel
BuildRequires: ncpfs-devel
BuildRequires: gtk+2.0-devel

%description
A very fast network logon cracker which support many different services.

%package gui
Summary:    GUI for %{name}
Summary:	Network logon cracker
License:	GPLv3
Requires:   %{name} = %{version}-%{release}

%description gui
GUI for %{name}.

%prep
%setup -q
chmod 644 LICENSE

%build
%configure2_5x --disable-xhydra
%make
cd hydra-gtk
%configure2_5x
%make

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 hydra %{buildroot}%{_bindir}
install -m 755 hydra-gtk/src/xhydra %{buildroot}%{_bindir}

install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 hydra.1 xhydra.1 pw-inspector.1 %{buildroot}%{_mandir}/man1

%files
%doc CHANGES INSTALL LICENSE* README
%{_bindir}/hydra
%{_mandir}/man1/hydra.1*
%{_mandir}/man1/pw-inspector.1*

%files gui
%{_bindir}/xhydra
%{_mandir}/man1/xhydra.1*
