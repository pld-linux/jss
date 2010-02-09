Summary:	JSS - Network Security Services for Java
Summary(pl.UTF-8):	JSS - Network Security Services for Java - usługi bezpieczeństwa sieciowego dla Javy
Name:		jss
Version:	4.3.1
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		Development/Languages/Java
Source0:	ftp://ftp.mozilla.org/pub/mozilla.org/security/jss/releases/JSS_4_3_1_RTM/src/%{name}-%{version}.tar.bz2
# Source0-md5:	5b16d2315006338b55653336be4ea750
Patch0:		%{name}-coreconf.patch
URL:		http://www.mozilla.org/projects/security/pki/jss/
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	nspr-devel >= 2.0
BuildRequires:	nss-devel
BuildRequires:	perl-base
BuildRequires:	unzip
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
A Java interface to NSS that supports most of the security standards
and encryption technologies supported by NSS. JSS also provides a pure
Java interface for ASN.1 types and BER/DER encoding.

%description -l pl.UTF-8
Interfejs Javy do biblioteki NSS obsługujący większość standardów
bezpieczeństwa i technologii szyfrowania obsługiwanych przez NSS. JSS
udostępnia także czysto javowy interfejs do typów ASN.1 i kodowania
BER/DER.

%prep
%setup -q -c
%patch0 -p1

install -d mozilla/dist/public
ln -sf /usr/include/nspr mozilla/dist/public/nspr20
ln -sf /usr/include/nss mozilla/dist/public/nss

%build
%{__make} -C mozilla/security/coreconf \
	BUILD_OPT=1 \
	CC="%{__cc}" \
	OPTIMIZER="%{rpmcflags}"
%{__make} -C mozilla/security/jss \
	BUILD_OPT=1 \
	CC="%{__cc}" \
	JAVA_HOME="%{java_home}" \
	OPTIMIZER="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_libdir}}

install mozilla/dist/xpclass.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf xpclass.jar $RPM_BUILD_ROOT%{_javadir}/jss.jar
ln -sf xpclass.jar $RPM_BUILD_ROOT%{_javadir}/jss4.jar

install mozilla/dist/Linux*/lib/libjss4.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc mozilla/security/jss/jss.html
%attr(755,root,root) %{_libdir}/libjss4.so
%{_javadir}/jss*.jar
%{_javadir}/xpclass.jar
