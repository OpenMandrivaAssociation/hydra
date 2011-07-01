Name:		hydra
Version:	6.4
Release:	%mkrel 1
Summary:	Network logon cracker
License:	GPLv3
Group:		Networking/Other
URL:		http://www.thc.org/thc-hydra/
Source:     http://freeworld.thc.org/releases/hydra-%{version}-src.tar.gz
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: subversion-devel
BuildRequires: mysql-devel
BuildRequires: postgresql-devel
BuildRequires: firebird-devel
BuildRequires: ssh-devel
BuildRequires: idn-devel
BuildRequires: ncpfs-devel
BuildRequires: gtk+2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n hydra-%{version}-src
chmod 644 LICENSE

%build
./configure --prefix=%{_prefix} --disable-xhydra
%make CFLAGS="%{optflags}"
cd hydra-gtk
%configure2_5x
%make

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 hydra %{buildroot}%{_bindir}
install -m 755 hydra-gtk/src/xhydra %{buildroot}%{_bindir}

install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 hydra.1 xhydra.1 pw-inspector.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES INSTALL LICENSE* README
%{_bindir}/hydra
%{_mandir}/man1/hydra.1*
%{_mandir}/man1/pw-inspector.1*

%files gui
%defattr(-,root,root)
%{_bindir}/xhydra
%{_mandir}/man1/xhydra.1*

