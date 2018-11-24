%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}

Name:       harbour-ytplayer
Summary:    Native YouTube client for SailfishOS
Version:    0.5.8
Release:    5
Group:      Qt/Qt
License:    BSD-3-Clause
URL:        https://github.com/tworaz/sailfish-ytplayer
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   nemo-qml-plugin-notifications-qt5
Requires:   pyotherside-qml-plugin-python3-qt5
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(sailfishapp) >= 0.0.10
BuildRequires:  desktop-file-utils
BuildRequires:  zip
BuildRequires:  python3-base
BuildRequires:  git

%description
YTPlayer is an unofficial YouTube client for SailfishOS


%prep
%setup -q -n %{name}-%{version}

%build
%qtc_qmake5
%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(0644,root,root,-)
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_datadir}/%{name}/bin/youtube-dl
%{_datadir}/%{name}/licenses
%{_datadir}/%{name}/languages
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/86x86/apps/%{name}.png
