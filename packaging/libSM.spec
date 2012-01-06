
Name:       libSM
Summary:    X.Org X11 libSM runtime library
Version:    1.2.0
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xorg-macros)


%description
X11 Session Management library.


%package devel
Summary:    X.Org X11 libSM development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The X.org X11 SM  development package.


%prep
%setup -q -n %{name}-%{version}


%build

%reconfigure --disable-static \
    --with-libuuid

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/libSM.so.6
%{_libdir}/libSM.so.6.0.1
%exclude /usr/share/doc/libSM/SMlib.xml
%exclude /usr/share/doc/libSM/xsmp.xml


%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/X11/SM
%{_includedir}/X11/SM/SM.h
%{_includedir}/X11/SM/SMlib.h
%{_includedir}/X11/SM/SMproto.h
%{_libdir}/libSM.so
%{_libdir}/pkgconfig/sm.pc

