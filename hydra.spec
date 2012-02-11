Name:		hydra
Version:	7.1
Release:	%mkrel 2
Summary:	Network logon cracker
License:	GPLv3
Group:		Monitoring
URL:		http://www.thc.org/thc-hydra/
Source:		http://freeworld.thc.org/releases/hydra-%{version}-src.tar.gz
Patch0:		hydra-7.1-src-fix-services-list.patch
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	subversion-devel
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
BuildRequires:	firebird-devel
BuildRequires:	ssh-devel
BuildRequires:	idn-devel
BuildRequires:	ncpfs-devel
BuildRequires:	gtk+2-devel
BuildRequires:	imagemagick
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
A very fast network logon cracker which support many different services.

%package gui
Summary:	GUI for %{name}
License:	GPLv3
Requires:	%{name} = %{version}-%{release}

%description gui
GUI for %{name}.

%package pwinspector
Summary: PW-Inspector reads passwords and prints those which meet the requirements
Group: Networking/Other
Provides: hydra-pwinspector = %{version}-%{release}

%description pwinspector
PW-Inspector reads passwords in and prints those which meet the requirements.
The return code is the number of valid passwords found, 0 if none was found.
Use for security: check passwords, if 0 is returned, reject password choice.
Use for hacking: trim your dictionary file to the pw requirements of the target.
Usage only allowed for legal purposes.

%prep
%setup -q -n hydra-%{version}-src
%patch0 -p1 -b .services
chmod 644 LICENSE

%build
%configure2_5x --disable-xhydra
%make
cd hydra-gtk
%configure2_5x
%make

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 hydra %{buildroot}%{_bindir}
install -m 755 pw-inspector %{buildroot}%{_bindir}
install -m 755 hydra-gtk/src/xhydra %{buildroot}%{_bindir}

install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 hydra.1 xhydra.1 pw-inspector.1 %{buildroot}%{_mandir}/man1

#XDG menu and icons for GUI
install -d -m 755 %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
convert -size 32x32 xhydra.png %{buildroot}%{_iconsdir}/xhydra.png
convert -size 48x48 xhydra.png %{buildroot}%{_liconsdir}/xhydra.png
convert -size 16x16 xhydra.png %{buildroot}%{_miconsdir}/xhydra.png

install -d -m 755 %{buildroot}%{_datadir}/pixmaps
convert -size 64x64 xhydra.png %{buildroot}%{_datadir}/pixmaps/xhydra.png

install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-xhydra.desktop << EOF
[Desktop Entry]
Name=XHydra
Comment=Network logon cracker
Exec=%{_bindir}/xhydra
Icon=xhydra
Terminal=false
Type=Application
StartupNotify=true
Categories=Tools;Monitor;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES INSTALL LICENSE* README
%{_bindir}/hydra
%{_mandir}/man1/hydra.1*

%files gui
%defattr(-,root,root)
%{_bindir}/xhydra
%{_mandir}/man1/xhydra.1*
%{_datadir}/applications/mandriva-xhydra.desktop
%{_datadir}/pixmaps/xhydra.png
%{_iconsdir}/xhydra.png
%{_liconsdir}/xhydra.png
%{_miconsdir}/xhydra.png

%files pwinspector
%defattr(-,root,root)
%{_bindir}/pw-inspector
%{_mandir}/man1/pw-inspector.1*
