Name:           alacritty
Version:        0.2.5
Release:        1%{?dist}
Summary:        A cross-platform, GPU-accelerated terminal emulator

License:        Apache-2.0
URL:            https://github.com/jwilm/alacritty
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  rust-packaging
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  freetype-devel
BuildRequires:  fontconfig-devel

Requires:       freetype
Requires:       fontconfig
Requires:       xclip

Provides:       alacritty = %{version}-%{release}

%description
Alacritty is the fastest terminal emulator in existence. Using the GPU for
rendering enables optimizations that simply aren't possible in other emulators.


%prep
%autosetup
%cargo_prep


%build
%cargo_build


%install
%cargo_install


%check
%cargo_test


%files
%license LICENSE-APACHE
%doc README.md
%doc CHANGELOG.md


%changelog
* Wed Jan  9 2019 Aurelien Rouene <aurelien@rouene.fr> - 0.2.5-1
- RPM release of alacritty 0.2.5
