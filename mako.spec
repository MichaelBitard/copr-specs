Name:		mako
Version:	1.2
Release:	3%{?dist}
Summary:	A lightweight Wayland notification daemon

License:	MIT
URL:		https://wayland.emersion.fr/mako
Source0:	https://github.com/emersion/mako/archive/v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	clang
BuildRequires:	meson
BuildRequires:	scdoc
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols-devel
BuildRequires:	pango-devel
BuildRequires:	cairo-devel
BuildRequires:	systemd-devel

Requires:	libwayland-client
Requires:	libwayland-server
Requires:	cairo
Requires:	pango

Provides:	mako = %{version}-%{release}

%description
A lightweight notification daemon for Wayland.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%files
%{_bindir}/mako
%{_bindir}/makoctl
%{_mandir}/man1/mako.1.gz
%{_mandir}/man1/makoctl.1.gz

%doc README.md
%license LICENSE


%changelog
* Mon Jan 14 2019 Aurelien Rouene <aurelien@rouene.fr> - 1.2-3
- Removing useless service unit

* Fri Jan 11 2019 Aurelien Rouene <aurelien@rouene.fr> - 1.2-2
- Adding license, man files, service unit

* Fri Jan 11 2019 Aurelien Rouene <aurelien@rouene.fr> - 1.2-1
- RPM release of mako 1.2
