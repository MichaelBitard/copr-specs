%global debug_package %{nil}

Name:           i3blocks
Version:        1.4
Release:        2%{?dist}
Summary:        A minimalist scheduler for your status bar scripts

License:        GPL-3.0
URL:            https://github.com/vivien/i3blocks
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  rubygem-ronn

Recommends:     acpi
Recommends:     lm_sensors

Provides:       i3blocks = %{version}-%{release}

%description
A minimalist scheduler for your status line scripts

i3blocks executes your command lines and generates a status line from their
output. Commands are scheduled at configured time intervals, upon signal
reception or on clicks.

The generated line is meant to be displayed by the i3 window manager through
its i3bar component, as an alternative to i3status.


%prep
%autosetup

%build
make %{?_smp_mflags}


%install
export PREFIX=/usr
%make_install
# rm %{_builddir}/%{name}-%{version}/debugsourcefiles.list


%files
%{_bindir}/i3blocks
%{_libexecdir}/%{name}/*

%{_mandir}/man1/i3blocks.1.gz

%config %{_sysconfdir}/i3blocks.conf

%license COPYING
%doc CHANGELOG.md
%doc README.md


%changelog
* Mon Jan 14 2019 Aurelien Rouene <aurelien@rouene.fr> - 1.4-2
- Adding acpi and lm_sensors as recommended packages

* Mon Jan 14 2019 Aurelien Rouene <aurelien@rouene.fr> - 1.4-1
- RPM release of i3blocks v1.4
