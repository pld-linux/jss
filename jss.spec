Summary:	JSS - Network Security Services for Java
Summary(pl):	JSS - Network Security Services for Java - us³ugi bezpieczeñstwa sieciowego dla Javy
Name:		jss
Version:	3.4.1
Release:	1
License:	NPL 1.1
Group:		Development/Languages/Java
Source0:	ftp://ftp.mozilla.org/pub/mozilla.org/security/jss/releases/JSS_3_4_1_RTM/src/%{name}-%{version}-src.tar.gz
# Source0-md5:	29689ea36b27584feb22d291404506ea
URL:		http://www.mozilla.org/projects/security/pki/jss/
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	nspr-devel >= 2.0
BuildRequires:	nss-devel
BuildRequires:	perl-base
BuildRequires:	sed >= 4.0
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
A Java interface to NSS that supports most of the security standards
and encryption technologies supported by NSS. JSS also provides a pure
Java interface for ASN.1 types and BER/DER encoding.

%description -l pl
Interfejs Javy do biblioteki NSS obs³uguj±cy wiêkszo¶æ standardów
bezpieczeñstwa i technologii szyfrowania obs³ugiwanych przez NSS. JSS
udostêpnia tak¿e czysto javowy interfejs do typów ASN.1 i kodowania
BER/DER.

%prep
%setup -q -n %{name}-%{version}-src

sed -i -e 's/-O/-O -source 1.4/' mozilla/security/jss/build_java.pl
sed -i -e 's,/classic,/server,' mozilla/security/coreconf/jdk.mk

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

install mozilla/dist/Linux*/lib/libjss3.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc mozilla/security/jss/jss.html
%attr(755,root,root) %{_libdir}/libjss3.so
%{_javadir}/jss.jar
%{_javadir}/xpclass.jar
