Name:           sway
Version:        1.0
Release:        1%{?dist}
Summary:        i3-compatible Wayland compositor

License:        MIT
URL:            https://github.com/swaywm/sway
Source0:        https://github.com/swaywm/sway/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  clang
BuildRequires:  meson
BuildRequires:  wlroots-devel >= 0.5.0
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  libevdev-devel
BuildRequires:  pcre-devel
BuildRequires:  json-c-devel
BuildRequires:  pango-devel
BuildRequires:  cairo-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  scdoc
BuildRequires:  libxkbcommon-devel
BuildRequires:  systemd-devel

Requires:       wlroots >= 0.5.0
Requires:       cairo
Requires:       pango
Requires:       gdk-pixbuf2

Provides:       sway = %{version}-%{release}

%description
sway is a work in progress i3-compatible Wayland compositor.


%prep
%{_bindir}/ls /builddir/build/SOURCES
%autosetup -n %{name}-%{version}


%build
%meson --auto-features=auto -Dman-pages=disabled -Dwerror=false
%meson_build


%install
%meson_install
# rm -rf $RPM_BUILD_ROOT


%check
%meson_test


%files
%{_bindir}/sway
%{_bindir}/swaybar
%{_bindir}/swaybg
%{_bindir}/swaymsg
%{_bindir}/swaynag
%{_datadir}/backgrounds/sway/*
%{_datadir}/bash-completion/completions/*
%{_datadir}/fish/completions/*
%{_datadir}/zsh/site-functions/*
%{_datadir}/wayland-sessions/sway.desktop

#%{_mandir}/man1/*.1.gz
#%{_mandir}/man5/*.5.gz

%config %{_sysconfdir}/sway/config
%config %{_sysconfdir}/sway/security.d/00-defaults

%license LICENSE
%doc README.*


%changelog
* Tue Mar  12 2019 Michaël Bitard <bitard.michael@gmail.com> - 1.0
- RPM release of sway 1.0

* Tue Feb  19 2019 Michaël Bitard <bitard.michael@gmail.com> - 1.0r3-1
- RPM release of sway 1.0-rc3

* Sun Feb  3 2019 Aurelien Rouene <aurelien@rouene.fr> - 1.0r1-1
- RPM release of sway 1.0-rc1

* Wed Jan  9 2019 Aurelien Rouene <aurelien@rouene.fr> - 1.0b2-2
- Incrementing release

* Wed Jan  9 2019 Aurelien Rouene <aurelien@rouene.fr> - 1.0b2-1
- RPM release of sway 1.0-beta.2
