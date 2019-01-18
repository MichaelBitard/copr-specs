Name:           wlroots
Version:        0.2
Release:        2%{?dist}
Summary:        A modular Wayland compositor library

License:        MIT
URL:            https://github.com/swaywm/wlroots
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  clang
BuildRequires:  meson
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  egl-wayland-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  libdrm-devel
BuildRequires:  libinput-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libgudev-devel
BuildRequires:  pixman-devel
BuildRequires:  libcap-devel
BuildRequires:  systemd-devel

Provides:       wlroots = %{version}-%{release}

%description
Pluggable, composable, unopinionated modules for building a Wayland compositor;
or about 50,000 lines of code you were going to write anyway.


%package devel
Summary:        Development files of wlroots

Requires:       %{name}%{?_isa} == %{version}-%{release}
Requires:       wayland-devel
Requires:       wayland-protocols-devel
Requires:       egl-wayland-devel
Requires:       mesa-libEGL-devel
Requires:       mesa-libGLES-devel
Requires:       mesa-libgbm-devel
Requires:       libdrm-devel
Requires:       libinput-devel
Requires:       libxkbcommon-devel
Requires:       libgudev-devel
Requires:       pixman-devel
Requires:       systemd-devel

Provides:       pkgconfig(wlroots) = %{version}


%description devel
Pluggable, composable, unopinionated modules for building a Wayland compositor;
or about 50,000 lines of code you were going to write anyway.


%prep
%autosetup

# Remove all .gitignore files
%{_bindir}/find %{_builddir}/%{name}-%{version} -name '.gitignore' -delete


%build
%meson --auto-features=auto
%meson_build


%install
%meson_install
# rm -rf $RPM_BUILD_ROOT


%check
%meson_test


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%{_libdir}/libwlroots.so.0.0.0
%{_libdir}/libwlroots.so.0
%{_libdir}/libwlroots.so

%license LICENSE
%doc README.md


%files devel
%{_libdir}/libwlroots.so
%{_libdir}/pkgconfig/wlroots.pc
%{_includedir}/wlr

%doc examples


%changelog
* Wed Jan  9 2019 Aurelien Rouene <aurelien@rouene.fr> - 0.2-1
- RPM release of wlroots 0.2
