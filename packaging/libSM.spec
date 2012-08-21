Summary: X.Org X11 SM runtime library
Name: libSM
Version: 1.2.1
Release: 1
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires: xorg-x11-xtrans-devel >= 1.0.3-4
BuildRequires: libICE-devel
BuildRequires: libuuid-devel

%description
The X.Org X11 SM (Session Management) runtime library.

%package devel
Summary: X.Org X11 SM development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libICE-devel

%description devel
The X.Org X11 SM (Session Management) development package.

%prep
%setup -q

%build

%reconfigure --with-libuuid --disable-static \
           LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# we %%doc these ourselves, later, and only the text versions
rm -rf $RPM_BUILD_ROOT%{_docdir}

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog
%{_libdir}/libSM.so.6
%{_libdir}/libSM.so.6.*

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/X11/SM
%{_includedir}/X11/SM/SM.h
%{_includedir}/X11/SM/SMlib.h
%{_includedir}/X11/SM/SMproto.h
%{_libdir}/libSM.so
%{_libdir}/pkgconfig/sm.pc
