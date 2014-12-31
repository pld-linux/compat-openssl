Summary:	OpenSSL Toolkit libraries for the "Secure Sockets Layer" (SSL v2/v3)
Name:		compat-openssl
Version:	0.9.7m
Release:	9
License:	Apache-like
Group:		Libraries
Source0:	openssl-compat-%{version}.tar.xz
# Source0-md5:	2c13cb0bba2f731f1e80ef514befd82b
BuildRequires:	/sbin/ldconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Conflicts:	openssl < 0.9.7m-9
ExclusiveArch:	%{x8664} %{ix86} alpha ppc sparc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_check_so	1
%define		no_install_post_strip		1
%define		no_install_post_chrpath		1
%define		_enable_debug_packages		0

%description
The OpenSSL Project is a collaborative effort to develop a robust,
commercial-grade, full-featured, and Open Source toolkit implementing
the Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS
v1) protocols with full-strength cryptography world-wide. The project
is managed by a worldwide community of volunteers that use the
Internet to communicate, plan, and develop the OpenSSL tookit and its
related documentation.

OpenSSL is based on the excellent SSLeay library developed by Eric A.
Young and Tim J. Hudson. The OpenSSL toolkit is licensed under an
Apache-style licence, which basically means that you are free to get
and use it for commercial and non-commercial purposes subject to some
simple license conditions.

This package contains shared libraries only, install openssl-tools if
you want to use openssl cmdline tool.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%ifarch alpha
cp -a alpha/* $RPM_BUILD_ROOT%{_libdir}
%endif

%ifarch %{x8664}
cp -a amd64/* $RPM_BUILD_ROOT%{_libdir}
%endif

%ifarch sparc
cp -a sparc/* $RPM_BUILD_ROOT%{_libdir}
%endif

%ifarch %{ix86}
cp -a i[34]86/* $RPM_BUILD_ROOT%{_libdir}
%endif

%ifarch ppc
cp -a ppc/* $RPM_BUILD_ROOT%{_libdir}
%endif

/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcrypto.so.*.*.*
%attr(755,root,root) %{_libdir}/libssl.so.*.*.*
