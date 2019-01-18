%global gitver 1.0-beta.2


Name:           sway
Version:        1.0b2
Release:        1%{?dist}
Summary:        i3-compatible Wayland compositor

License:        MIT
URL:            https://github.com/swaywm/sway
Source0:        %{url}/archive/%{gitver}.tar.gz

BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  clang
BuildRequires:  meson
BuildRequires:  wlroots-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  pcre-devel
BuildRequires:  json-c-devel
BuildRequires:  pango-devel
BuildRequires:  cairo-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  pam-devel
BuildRequires:  scdoc
BuildRequires:  libxkbcommon-devel
BuildRequires:  systemd-devel

Requires:       wlroots
Requires:       libwayland-client
Requires:       libwayland-server
Requires:       libwayland-cursor
Requires:       libxkbcommon
Requires:       cairo
Requires:       pango
Requires:       gdk-pixbuf2

Provides:       sway = %{version}-%{release}

%description
sway is a work in progress i3-compatible Wayland compositor.


%prep
%autosetup -n %{name}-%{gitver}


%build
%meson --auto-features=auto
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
%{_bindir}/swayidle
%{_bindir}/swaylock
%{_bindir}/swaymsg
%{_bindir}/swaynag
%{_datadir}/backgrounds/sway/*
%{_datadir}/bash-completion/completions/*
%{_datadir}/fish/completions/*
%{_datadir}/zsh/site-functions/*
%{_datadir}/wayland-sessions/sway.desktop

%{_mandir}/man1/*.1.gz
%{_mandir}/man5/*.5.gz

%config %{_sysconfdir}/pam.d/swaylock
%config %{_sysconfdir}/sway/config
%config %{_sysconfdir}/sway/security.d/00-defaults

%license LICENSE
%doc README.*


%changelog
* Wed Jan  9 2019 Aurelien Rouene <aurelien@rouene.fr> - 1.0b2-1
- RPM release of sway 1.0-beta.2
