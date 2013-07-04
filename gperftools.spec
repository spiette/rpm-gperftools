# To Build: 
#
# sudo yum -y install rpmdevtools && rpmdev-setuptree
#
# sudo yum -y install libunwind-devel
#
# wget https://gperftools.googlecode.com/files/gperftools-2.0.tar.gz -O ~/rpmbuild/SOURCES/gperftools-2.0.tar.gz
# wget https://raw.github.com/nmilford/rpm-gperftools/master/gperftools.spec -O ~/rpmbuild/SPECS/gperftools.spec
# rpmbuild -bb ~/rpmbuild/SPECS/gperftools.spec

%define	prefix /usr

Name:     gperftools
Summary:  Performance tools for C++
Version:  2.0
Release:  1
Group:    Development/Libraries
URL:      http://code.google.com/p/gperftools/
License:  BSD
Vendor:   Google Inc. and others
Source:   https://gperftools.googlecode.com/files/%{name}-%{version}.zip
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: libunwind-devel
Obsoletes: google-perftools
Prefix: %prefix

%description
The %name packages contains some utilities to improve and analyze the
performance of C++ programs.  This includes an optimized thread-caching
malloc() and cpu and heap profiling utilities.

%package devel
Summary: Performance tools for C++
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The %name-devel package contains static and debug libraries and header
files for developing applications that use the %name package.


%prep
%setup

%build
CXXFLAGS=`echo -DTCMALLOC_LARGE_PAGES| sed -e 's/-Wp,-D_FORTIFY_SOURCE=2//g'`
./configure --prefix=%{_prefix} --exec-prefix=%{_exec_prefix} --bindir=%{_bindir} --sbindir=%{_sbindir} --sysconfdir=%{_sysconfdir} --datadir=%{_datadir} --includedir=%{_includedir} --libdir=%{_libdir} --libexecdir=%{_libexecdir} --localstatedir=%{_localstatedir} --sharedstatedir=%{_sharedstatedir} --mandir=%{_mandir} --infodir=%{_infodir}
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%docdir %{prefix}/share/doc/%{name}-%{version}
%{prefix}/share/doc/%{name}-%{version}/*

%{_libdir}/*.so.*
%{_bindir}/pprof
%{_mandir}/man1/pprof.1*

%files devel
%defattr(-,root,root)

%{_includedir}/google
%{_includedir}/gperftools
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jul 04 2013 Nathan Milford <nathan@milford.io>- 2.0-1
- Two Point Oh
* Mon Apr 20 2009  <opensource@google.com>
- Change build rule to use a configure line more like '%configure'
- Change install to use DESTDIR instead of prefix for configure
- Use wildcards for doc/ and lib/ directories
* Fri Mar 11 2005  <opensource@google.com>
- First draft

