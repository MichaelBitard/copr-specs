Name:           swayidle
Version:        1.2
Release:        1%{?dist}
Summary:        Idle management daemon for Wayland

License:        MIT
URL:            https://github.com/swaywm/swayidle
Source0:        https://github.com/swaywm/swayidle/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  clang
BuildRequires:  meson
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  scdoc


%description
This is sway's idle management daemon, swayidle. It is compatible
with any Wayland compositor which implements the KDE idle protocol.


%prep
%autosetup


%build
%meson --auto-features=auto
%meson_build


%install
%meson_install


%check
%meson_test


%files
%{_bindir}/swayidle
%{_datadir}/bash-completion/completions/swayidle
%{_datadir}/fish/completions/swayidle.fish
%{_datadir}/zsh/site-functions/_swayidle

%{_mandir}/man1/swayidle.1.gz

%license LICENSE
%doc README.*


%changelog
* Tue Feb  19 2019 Michaël Bitard <bitard.michael@gmail.com> - 1.2-1
- RPM release of swayidle 1.2
* Sun Feb  3 2019 Aurelien Rouene <aurelien@rouene.fr> - 1.1-1
- RPM release of swayidle 1.1
