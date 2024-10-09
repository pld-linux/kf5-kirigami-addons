#
# Conditional build:
%bcond_with	tests	# test suite

%define		qt_ver		5.15.2
%define		kf_ver		5.102.0
%define		kfname		kirigami-addons
Summary:	Kirigami addons library
Summary(pl.UTF-8):	Biblioteka Kirigami addons
# not strictly part of framework, but closely bound to KF5 (and cmake config is named KF5KirigamiAddons)
Name:		kf5-kirigami-addons
# keep 0.11.x here for Qt5/KF5 support
Version:	0.11.0
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/kirigami-addons/%{kfname}-%{version}.tar.xz
# Source0-md5:	dfb9ba7a8f57c96d9bc1237399829bd3
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Network-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-controls2-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.20
BuildRequires:	kf5-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf5-ki18n-devel >= %{kf_ver}
BuildRequires:	kf5-kirigami2-devel >= %{kf_ver}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Quick-controls2 >= %{qt_ver}
Requires:	kf5-dirs
Obsoletes:	kirigami-addons < 0.11.0-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kirigami Addons is an additional set of visual components that work
well on mobile and desktop and are guaranteed to be cross-platform. It
uses Kirigami under the hood to create its components and should look
native with any QtQuick Controls style.

%description -l pl.UTF-8
Kirigami Addons to dodatkowy zbiór komponentów graficznych dobrze
działających na urządzeniach przenośnych jak i stacjonarnych, z
gwarantowaną przenośnością między platformami. Pod spodem wykorzystuje
Kirigami do tworzenia komponentów i powinien wyglądać zgodnie z
dowolnym stylem kontrolek QtQuick.

%package devel
Summary:	Header files for Kirigami addons development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających Kirigami addons
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qt_ver}
Obsoletes:	kirigami-addons-devel < 0.11.0-2

%description devel
Header files for Kirigami addons development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających Kirigami addons.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang kirigami-addons

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kirigami-addons.lang
%defattr(644,root,root,755)
# FIXME: permissions
%dir %{_libdir}/qt5/qml/org/kde/kirigamiaddons
%dir %{_libdir}/qt5/qml/org/kde/kirigamiaddons/components
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kirigamiaddons/components/libcomponentsplugin.so
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/components/*.qml
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/components/qmldir
%dir %{_libdir}/qt5/qml/org/kde/kirigamiaddons/dateandtime
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/dateandtime/private
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kirigamiaddons/dateandtime/libdateandtimeplugin.so
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/dateandtime/*.qml
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/dateandtime/qmldir
%dir %{_libdir}/qt5/qml/org/kde/kirigamiaddons/delegates
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kirigamiaddons/delegates/libdelegatesplugin.so
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/delegates/*.qml
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/delegates/qmldir
%dir %{_libdir}/qt5/qml/org/kde/kirigamiaddons/formcard
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/formcard/private
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kirigamiaddons/formcard/libformcardplugin.so
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/formcard/*.qml
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/formcard/qmldir
%dir %{_libdir}/qt5/qml/org/kde/kirigamiaddons/labs
%dir %{_libdir}/qt5/qml/org/kde/kirigamiaddons/labs/components
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kirigamiaddons/labs/components/libcomponentslabsplugin.so
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/labs/components/*.qml
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/labs/components/qmldir
%dir %{_libdir}/qt5/qml/org/kde/kirigamiaddons/labs/mobileform
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/private
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/libmobileformplugin.so
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/*.qml
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/qmldir
%dir %{_libdir}/qt5/qml/org/kde/kirigamiaddons/settings
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kirigamiaddons/settings/libsettingsplugin.so
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/settings/*.qml
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/settings/qmldir
%dir %{_libdir}/qt5/qml/org/kde/kirigamiaddons/sounds
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kirigamiaddons/sounds/libsoundsplugin.so
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/sounds/*.qml
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/sounds/qmldir
%dir %{_libdir}/qt5/qml/org/kde/kirigamiaddons/treeview
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/treeview/private
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/treeview/styles
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kirigamiaddons/treeview/libtreeviewplugin.so
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/treeview/*.qml
%{_libdir}/qt5/qml/org/kde/kirigamiaddons/treeview/qmldir

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/KF5KirigamiAddons
