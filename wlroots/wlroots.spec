Name:           wlroots
Version:        0.4.1
Release:        1%{?dist}
Summary:        A modular Wayland compositor library

License:        MIT
URL:            https://github.com/swaywm/wlroots
Source0:        https://github.com/swaywm/wlroots/archive/0.4.1/wlroots-0.4.1.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  wget
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdrm) >= 2.4.95
BuildRequires:  pkgconfig(libinput) >= 1.7.0
BuildRequires:  pkgconfig(libsystemd) >= 237
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
#BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(wayland-server) >= 1.16
BuildRequires:  pkgconfig(xkbcommon)

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
%{_bindir}/ls /builddir/build/SOURCES
#%{_bindir}/wget https://github.com/swaywm/wlroots/archive/0.4.1/wlroots-0.4.1.tar.gz -O %{_sourcedir}/%{name}-%{version}.tar.gz
#%{_bindir}/ls /builddir/build/SOURCES
%autosetup -v -n %{name}-%{version}

# Remove all .gitignore files
%{_bindir}/find %{_builddir}/%{name}-%{version} -name '.gitignore' -delete

%build
%meson -Dxcb-errors=disabled
%meson_build


%install
%meson_install
# rm -rf $RPM_BUILD_ROOT


%check
%meson_test


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%{_libdir}/libwlroots.so.1.2.0
%{_libdir}/libwlroots.so.1
%{_libdir}/libwlroots.so

%license LICENSE
%doc README.md


%files devel
%{_libdir}/libwlroots.so
%{_libdir}/pkgconfig/wlroots.pc
%{_includedir}/wlr

%doc examples


%changelog
* Thu Feb 28 2019 Michael Bitard <bitard.michal@gmail.com> - 0.4.1-1
- RPM release of wlroots 0.3

* Sun Feb 03 2019 Aurelien Rouene <aurelien@rouene.fr> - 0.3-1
- RPM release of wlroots 0.3

* Wed Jan  9 2019 Aurelien Rouene <aurelien@rouene.fr> - 0.2-1
- RPM release of wlroots 0.2
