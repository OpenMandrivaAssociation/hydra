Summary:	Network logon cracker
Name:		hydra
Version:	9.4
Release:	1
License:	GPLv3+
Group:		Monitoring
Url:		https://github.com/vanhauser-thc/thc-hydra/
Source0:	https://github.com/vanhauser-thc/thc-hydra/archive/v%{version}/thc-hydra-%{version}.tar.gz
BuildRequires:	firebird-devel
BuildRequires:	mysql-devel
BuildRequires:	ncpfs-devel
BuildRequires:	postgresql-devel
BuildRequires:	subversion-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libidn)
BuildRequires:	pkgconfig(libpcre2-8)
BuildRequires:	pkgconfig(libssh)
BuildRequires:	pkgconfig(openssl)

%description
A very fast network logon cracker which support many different services.

%files
%doc CHANGES INSTALL LICENSE*
%{_bindir}/hydra
%{_mandir}/man1/hydra.1*
%{_mandir}/man1/pw-inspector.1*

#----------------------------------------------------------------------------

%package gui
Summary:	GUI for %{name}
Requires:	%{name} = %{EVRD}

%description gui
GUI for %{name}.

%files gui
%{_bindir}/xhydra
%{_mandir}/man1/xhydra.1*

#----------------------------------------------------------------------------

%prep
%setup -qn thc-%{name}-%{version}
chmod 644 LICENSE

%build
%configure --disable-xhydra
%make_build
cd hydra-gtk
%configure
%make_build

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 hydra %{buildroot}%{_bindir}
install -m 755 hydra-gtk/src/xhydra %{buildroot}%{_bindir}

install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 hydra.1 xhydra.1 pw-inspector.1 %{buildroot}%{_mandir}/man1
