#
# Conditional build:
%bcond_with	tests		# build with tests
#
# TODO:
# - runtime Requires if any

%define		qtver		5.15.2
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
# Source0-md5:	27d23279ee0ad5252a862c2671bc05ad
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Quick-controls2-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	catdoc
BuildRequires:	cmake >= 3.20
BuildRequires:	kf5-extra-cmake-modules >= 5.102.0
BuildRequires:	kf5-kirigami2-devel >= 5.102.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
%{_libdir}/qt5/qml/org/kde/kirigamiaddons

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/KF5KirigamiAddons
